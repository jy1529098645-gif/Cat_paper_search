# Methodology — how ranking and realness work

Two questions decide whether you can trust a research tool: *are the results
real?* and *is the best one near the top?* This page answers both in plain
language, describing what the code actually does (see
[`scripts/search_papers.py`](scripts/search_papers.py)).

---

## (a) Ranking — ordering by genuine research fit

Ranking happens in **two stages**, on purpose.

### Stage 1 — the transparent rule-based prior (`rule_score`)

After the five databases are queried in parallel, results are de-duplicated and
each paper gets a `rule_score` — a simple, inspectable number built from signals
anyone can reason about. It is NOT a black box:

- **Title and abstract term matching.** The query is tokenised into terms; each
  term found in the **title** is weighted heavily (×4), each term found in the
  **abstract** counts less (×1.5). A title match is a much stronger signal of fit
  than an abstract mention, so it's scored that way.
- **Exact-phrase bonus.** If the whole query appears verbatim in the title it
  gets a further boost (+5), or a smaller one for the abstract (+3).
- **Query coverage.** What fraction of the query's distinct terms appear anywhere
  in the title or abstract — rewards papers that cover the *whole* question, not
  just one buzzword (weighted ×12).
- **CJK tokenisation.** Chinese/Japanese queries don't split on spaces, so the
  tokeniser also emits individual CJK characters as terms. Without this a Chinese
  query would score near-zero; with it, Chinese-language searches get real
  keyword signal.
- **Recency signal.** Newer papers get a bonus that decays with age (≈0.55/year),
  so recent work surfaces without burying foundational papers.
- **Citation signal.** A `log(1 + citations)` bonus (capped) rewards well-cited
  work without letting a single mega-cited paper dominate. Citation counts come
  from the source APIs; arXiv preprints report 0, and where a source has no count
  it's treated as 0 (shown downstream as N/A).

Because the formula is fixed and the same script runs everywhere, **the raw
ordering is identical no matter which model relays it.**

### Stage 2 — the LLM re-rank by research fit

The `rule_score` is deliberately only a **keyword/recency/citation prior** — the
code's own comments say so. Keyword overlap alone floats "keyword-soup" papers to
the top: the wrong domain, or the wrong *sense* of an ambiguous word (e.g.
"players" matching *football players* or game-theory *players* when you meant
video-game players). So before results are shown, the assistant **re-reads the
candidate set and re-ranks it by genuine fit to your actual question**, leading
with on-target papers and pushing clearly off-target ones to the bottom (or
tagging them `⚠ likely off-target`). This down-ranking of off-target /
ambiguous-term hits is exactly what the keyword prior can't do on its own.

### De-duplication (so the ranking is honest)

The same paper often appears in several databases — and as both a preprint and a
published version. Before scoring, results are collapsed in two passes:

1. **By normalised DOI** — version suffixes are stripped, so `…/abc.v1` and
   `…/abc`, and arXiv `vN` variants, are treated as one paper.
2. **By normalised title** — catches the same work appearing under different DOIs
   (a preprint and its journal version, or two repositories).

When two records merge, the **richer** one is kept (prefers one with a PDF, then
more citations, then one that has an abstract), and the better PDF/abstract/
citation count is carried over. This stops a single paper from occupying three
ranking slots.

---

## (b) The realness guarantee

**What "real, never fabricated" means here:**

- **Search results are real API records.** Every paper in a result list was
  returned by a public scholarly API — OpenAlex, Crossref, arXiv, Semantic
  Scholar, or Europe PMC — and its metadata (title, authors, year, venue, DOI,
  citation count, PDF link) is the API's data, not the model's invention. The
  skill does not write citations from memory. You can confirm this for the
  example set with [`examples/verify_dois.py`](examples/verify_dois.py).
- **Reading reports use only extracted PDF text.** When you deep-read a paper, the
  script resolves and downloads the actual PDF and extracts its text; the report
  (research question, method, findings, limitations) is built **only** from that
  extracted text, with page references where the source supports a claim.
- **Gaps are disclosed, not filled.** If a paper is paywalled with no free copy,
  the skill says so and offers to work from the abstract or another identifier —
  it never invents the contents. If text extraction was truncated, the report
  says it covers only the analysed excerpt.

**What it does NOT cover (be precise about the boundary):**

- It does **not** guarantee a paper is *good*, *correct*, or *not retracted* —
  only that the record is real and the reading reflects the real text. Judging
  quality is still your job.
- Metadata is **only as accurate as the upstream API.** A venue mislabelled or a
  citation count that lags in OpenAlex/Crossref will be relayed faithfully — which
  means it inherits the source's occasional errors. Citation counts are live and
  drift over time.
- The **re-rank is a judgement, not a proof.** Stage 2 improves ordering but is a
  model's assessment of fit; it can still be debatable at the margins.
- "Never fabricated" is about *provenance and grounding*, not omniscience: the
  guarantee is that nothing is made up, not that nothing upstream is ever wrong.

See [`LIMITATIONS.md`](LIMITATIONS.md) for the known failure cases in full.

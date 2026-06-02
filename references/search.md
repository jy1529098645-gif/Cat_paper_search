# Reference: Literature Search & Ranking

How you (Claude) work around `scripts/search_papers.py`. The script handles
retrieval plus a transparent rule-based prior; you handle understanding the
query and judging genuine research fit.

## Pipeline

1. **Understand the query** — work out what the user is really after, and turn it
   into one or more clean search strings.
2. **Retrieve** — run `search_papers.py` with the best string(s).
3. **Re-rank** — read the returned `papers[]` and judge fit to the user's actual
   question, not keyword overlap. The script's `rule_score` is a prior, not the
   verdict.
4. **Present** — a ranked list with a one-line "why" per paper, grouped by theme
   when the request was broad.

---

## Understanding the query

For a focused query, search it directly. For a broad or exploratory one, it pays
to decompose first:

- **Pull out the core concepts** — the main terms the user typed and their
  immediate synonyms, plus any scope limiters (year range, population, domain,
  language) and any method or setting they named.
- **Read the intent** — are they exploring a field, comparing approaches, chasing
  a mechanism, looking for applications, or after a survey? This shapes how wide
  to cast.
- **Branch into directions** — for a well-studied topic, identify the genuinely
  distinct lines of work (a mature field can have six or more; a narrow one only
  a couple) and give each a tight search string. Avoid near-duplicate branches.
- **Search in English** — the major scholarly sources are English-dominated, so
  translate or transliterate non-English terms while keeping proper nouns and
  established technical terms intact. You can still present results in the user's
  language.

For a focused query you can skip straight to one good search string. For a broad
one, run the two to four most promising strings as separate `search_papers.py`
calls and merge the results.

---

## Re-ranking by research fit

The script orders by a keyword/recency/citation prior. Your job is to re-judge
each paper for how well it actually answers the user's question. For each, form a
quick read on:

- **How directly it's on target** — does it squarely address the question, sit
  adjacent to it, or drift off-topic?
- **What kind of paper it is** — an empirical study, a review/survey, a
  framework or tool, a technical method, an application/case, or theory. Match
  this to what the user wants: someone after findings is poorly served by a
  tooling paper, and vice versa.
- **Whether the abstract actually supports relevance** — a missing or threadbare
  abstract should pull a borderline paper down.

Order primarily by that fit judgement, letting paper type and on-target-ness
nudge things up or down, and let recency or citation weight matter more when the
user signals they care about it. Don't reward mere keyword overlap.

## Screening the borderline cases

For papers you're genuinely unsure about, argue both sides before deciding: make
the case to keep it, then the case to drop it (off-target domain, weak support,
mere keyword match, tooling when findings were wanted), and settle on keep /
unsure / drop. Missing abstracts and adjacent-domain papers should lose these
arguments unless they clearly supply needed background. Drop the rejects from the
main list — optionally noting them under a brief "screened out" line with the
reason.

## Sort preferences

If the user signals a preference, bias the final order accordingly:
- **balanced** (default): research fit, lightly helped by recency and citations
- **newest**: year first, then fit
- **most cited**: citation count first, then fit
- **open access**: papers with a `pdf_url` first (these are deep-readable)
- **evidence strength**: density of title/abstract match and recency over fit

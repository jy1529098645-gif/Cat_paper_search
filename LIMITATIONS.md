# Known limitations

A trustworthy tool tells you where its edges are. None of the below is a secret
bug — they're boundaries of the approach, written down so you can plan around
them rather than discover them mid-project. Knowing the limits is part of why you
can trust the parts that work.

## 1. Browsing-based versions can't reliably fetch very large N

On **ChatGPT / DeepSeek** (the portable, browsing-based path), search runs via
the model's web browsing instead of the Python scripts. Browsing can't bulk-fetch
hundreds of records reliably — in practice you hit a **ceiling around ~200
results**, and large requests get slow or partial. For genuinely large result
sets, use the **Python script path** (Claude Code, or any agent that can run
Python with internet, e.g. Cursor), where `search_papers.py` pulls a real
candidate pool from each API.

## 2. The portable (browsing) version is weaker than the script version

Beyond the N ceiling, the browsing version has **lighter coverage** than the
script version: it can't run all five APIs in true parallel, de-duplication and
rule-scoring are approximated rather than executed by code, and rate limits bite
sooner. Every result it returns is still **real** (it says so rather than inventing
when it can't reach a source) — but for the full-power experience, prefer the
Claude Code / Python path.

## 3. OpenAlex / Semantic Scholar rate-limiting (HTTP 429)

The APIs are key-free, which means **shared, throttled** traffic. **Semantic
Scholar** in particular returns **HTTP 429 (rate-limited)** under key-free load.
The script auto-retries with backoff (honouring `Retry-After`), which clears most
skips, and the other four databases carry the search if one drops. If S2 keeps
getting skipped, set a free key — `export S2_API_KEY=...` (from
[semanticscholar.org/product/api](https://www.semanticscholar.org/product/api)) —
and it stops 429-ing. Any skipped source is reported on stderr.

## 4. Paywalled papers can't be deep-read

Deep-read needs a fetchable PDF. If a paper is **paywalled with no open-access
copy** (resolver tries direct URL → arXiv-by-DOI → Unpaywall → OpenAlex → S2 and
finds nothing free), the skill **says so plainly** and offers to work from the
abstract or another identifier. It will **not** fabricate the contents. A 🔒 in
the result list means exactly this. Setting `UNPAYWALL_EMAIL=you@domain` slightly
improves the open-access hit rate.

## 5. Citation counts are sometimes unavailable (shown as N/A / 0)

Not every source reports citations. **arXiv** entries carry **0**, and where a
source omits a count it's treated as 0 (and may show as **N/A** downstream). So a
low or zero count can mean "genuinely uncited" *or* "the source didn't tell us" —
don't read too much into it. Counts that are present are live API values and
**drift over time** (the numbers in the examples will creep upward).

## 6. Ambiguous query terms

A keyword can carry the wrong *sense*: "players" can match football players or
game-theory players when you meant video-game players; "transformer" can mean the
neural-net architecture or electrical hardware. The rule-based score is keyword-
driven and can float these off-target hits up; the downstream LLM re-rank is what
catches them, but at the margins an ambiguous query can still surface a few
off-target papers (which is why clearly off-target ones get tagged rather than
silently dropped). Adding a disambiguating term to your query helps.

## 7. Metadata inherits upstream errors

Titles, venues, years, and DOIs are relayed **faithfully from the source APIs** —
which means the occasional upstream mislabel (wrong venue, a stray duplicate that
slips past de-dup, a preprint vs. published-version mismatch) is passed through
too. The guarantee is that records are **real and not invented**, not that every
upstream field is flawless. Quality, correctness, and retraction status are still
yours to judge.

---

If you hit a failure mode that isn't listed here, that's worth knowing — these
boundaries are meant to be honest and complete, not flattering.

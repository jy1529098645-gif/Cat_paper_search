# Changelog

All notable changes to **Paper Search** are documented here.
This project follows [Semantic Versioning](https://semver.org/).

## [2.0.0] — 2026-06-13

The search → deep-read flow becomes the explicit default, deep-read goes
multi-paper, and search results are now orderable.

### Added
- **`--sort` flag** in `scripts/search_papers.py`:
  `--sort relevance|recency|citations` (default `relevance`).
  - `recency` — newest publication year first
  - `citations` — most cited first
  - `rule_score` is the tie-breaker, so papers missing a year or citation
    count don't shuffle randomly.
- **Batch deep-read.** After a search, the skill now explicitly prompts which
  papers to read and accepts **several picks at once** (e.g. `3, 7, 12` or
  `1-5`). Picked PDFs are fetched in parallel and returned as one report per
  paper, in the order picked — no re-confirming between papers.

### Changed
- `SKILL.md` — flow documented as search → prompt → batch deep-read; `--sort`
  documented in the menu mapping and flags block; trigger description updated.
- `references/deep_read.md` — covers per-paper analysis within a batch
  (parallel fetch, one grounded report each).
- `PORTABLE_PROMPT.md` — same batch deep-read + sort behavior for browsing
  models (ChatGPT / DeepSeek / any browsing agent).
- `README.md` / `README.zh-CN.md` — describe ordering options and multi-pick
  deep read.
- Rebuilt the `paper-search.skill` upload bundle to match the updated sources.

## [1.0.0]

Initial public release of the open-source lite edition.

### Features
- **Search** across five keyless scholarly databases at once (OpenAlex,
  Crossref, arXiv, Semantic Scholar, Europe PMC), deduplicated and ranked by a
  transparent `rule_score` relevance prior, then re-ranked by research fit.
- **Deep-read** a single open-access paper: resolve the PDF (direct URL →
  arXiv-by-DOI → Unpaywall → OpenAlex → Semantic Scholar), extract the text,
  and produce an evidence-aware reading report grounded only in that text.
- **Honesty contract** — real records only, reports built solely from extracted
  text, paywalled papers reported rather than fabricated.
- Multiple distribution paths: Claude Code (git clone), Claude web/desktop
  (`paper-search.skill`), and any browsing model (`PORTABLE_PROMPT.md`).

[2.0.0]: https://github.com/jy1529098645-gif/Cat_paper_search/releases/tag/v2.0.0
[1.0.0]: https://github.com/jy1529098645-gif/Cat_paper_search/releases/tag/v1.0.0

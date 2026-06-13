# Generic AI vs. Paper Search

**The same question, two very different answers — one you can't trust, one you can verify.**

Ask a generic chatbot for academic references and it will often hand you a
beautifully formatted list of papers that *look* real: plausible titles,
plausible authors, a journal you recognise, even a DOI. The problem is that some
of them don't exist. Large language models are documented to **fabricate
citations** — inventing authors, years, and DOIs that resolve to nothing — because
they're predicting fluent text, not retrieving records. (This failure has a name
in the literature: "hallucinated references.") You only find out when you click
the DOI and get a 404, or a librarian does.

Paper Search is built the opposite way: every result is a **real record pulled
from a public scholarly API** (OpenAlex, Crossref, arXiv, Semantic Scholar,
Europe PMC), so every DOI points at a paper that actually exists.

Below is the side-by-side for the query **"CRISPR off-target effects" (since 2020)**.

---

## Column A — what a generic chatbot often does

> ### ⚠️ ILLUSTRATIVE FABRICATION — do NOT cite these
> The two entries below are **fake examples we wrote to show the failure mode.**
> The DOIs are deliberately invalid and **will not resolve.** They are here only
> to demonstrate what a hallucinated citation looks like — never present these as
> real, never cite them.

1. **High-fidelity Cas9 variants eliminate detectable off-target activity in human cells** — Reynolds, J. & Müller, K. · 2021 · *Nature Biotechnology* · DOI `10.1038/s41587-021-99999-9`
   ⚠️ *Fabricated. This DOI does not resolve (404). Plausible-looking, but the paper does not exist.*
2. **A genome-wide survey of CRISPR-Cas12a off-target landscapes across primary cell types** — Alvarez, P., Chen, L. & Osei, B. · 2022 · *Cell Reports* · DOI `10.1016/j.celrep.2022.000000`
   ⚠️ *Fabricated. This DOI does not resolve (404). Invented authors and an invented record.*

This is the trap: nothing above is flagged as uncertain by the model that
produced it. It reads like a citation. It is not one.

---

## Column B — what Paper Search returns

These are the **real records** for the same query, in the skill's actual output
format. Titles link straight to the paper via its DOI; 🟢 marks a free PDF you
can deep-read in full, 🔒 marks no free PDF.

> ## 🔎 5 results for: CRISPR off-target effects
> 1. **[Off-target effects in CRISPR/Cas9 gene editing](https://doi.org/10.3389/fbioe.2023.1143157)** — Congting Guo et al. · 2023 · *Frontiers in Bioengineering and Biotechnology* · cited 534 · 🟢 · [PDF](https://www.frontiersin.org/articles/10.3389/fbioe.2023.1143157/pdf)
> 2. **[Latest Developed Strategies to Minimize the Off-Target Effects in CRISPR-Cas-Mediated Genome Editing](https://doi.org/10.3390/cells9071608)** — Muhammad Naeem et al. · 2020 · *Cells* · cited 410 · 🟢 · [PDF](https://www.mdpi.com/2073-4409/9/7/1608/pdf)
> 3. **[CRISPR/Cas Systems in Genome Editing: Methodologies and Tools for sgRNA Design, Off-Target Evaluation, and Strategies to Mitigate Off-Target Effects](https://doi.org/10.1002/advs.201902312)** — Hakim Manghwar et al. · 2020 · *Advanced Science* · cited 304 · 🟢 · [PDF](https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/advs.201902312)
> 4. **[CRISPR/Cas13 effectors have differing extents of off-target effects that limit their utility in eukaryotic cells](https://doi.org/10.1093/nar/gkac159)** — Yuxi Ai et al. · 2022 · *Nucleic Acids Research* · cited 134 · 🔒
> 5. **[Beyond the promise: evaluating and mitigating off-target effects in CRISPR gene editing for safer therapeutics](https://doi.org/10.3389/fbioe.2023.1339189)** — Rui Lopes et al. · 2024 · *Frontiers in Bioengineering and Biotechnology* · cited 61 · 🟢

Every DOI above was verified to resolve at build time (confirmed registered in
Crossref) — run [`examples/verify_dois.py`](verify_dois.py) to re-check, and see
[`verification-log.md`](verification-log.md) for the captured output. Citation
counts are live API values and drift upward over time.

---

## The point

The difference between Column A and Column B isn't tone or politeness — both read
like confident bibliographies. The difference is **provenance**: Column B comes
from real API records, so every link works and every paper can be opened, while
Column A is fluent text with nothing behind it. With Paper Search you can click
any title and land on the actual paper; with a fabricating chatbot, you can't,
and you often won't know until it's too late.

That's the whole pitch: **real records you can verify, not plausible text you
have to trust.**

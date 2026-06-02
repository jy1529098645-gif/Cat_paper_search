# Reference: Deep Read (single-paper analysis)

You run `scripts/fetch_pdf.py` to resolve an open-access PDF and extract its
text, then produce an evidence-aware reading from the extracted text **only**.
The cardinal rule: never add facts from your own memory of the paper — if the
excerpt doesn't contain it, say so.

## Flow

1. Get an identifier for the paper (DOI, arXiv id, a direct `pdf_url`, or the
   title). Prefer DOI or arXiv id.
2. Run `fetch_pdf.py` (see SKILL.md for flags). It returns the extracted text,
   per-page text, the page count, and whether extraction was truncated.
3. If no PDF resolves, the paper is almost certainly paywalled with no open copy.
   Say so plainly and offer to try a different identifier or work from the
   abstract. Do not fabricate.
4. If extraction was truncated, your reading covers only the analysed excerpt
   (the opening pages). Disclose that.

## What a good reading contains

Working from the extracted text, give the reader a compact, faithful account.
Cover, as the text supports:

- a short plain-language **summary** of what the paper does;
- a **snapshot** — the research question, the study design, what was studied
  (sample/material), and the core claim;
- the **main contribution** and any guiding framework or theory;
- the **key findings**, and an **evidence trail** linking each important
  claim or result to the page it came from;
- how it **relates to the user's question**, with a rough 0–100 relevance read;
- **method notes, practical implications, and limitations/cautions.**

The evidence trail (claim → page number) is the most valuable part — it lets the
reader verify each point against the source.

Two non-negotiables, because this is what makes the reading trustworthy:

- **Use only the supplied text.** Don't pull in numbers, findings, or claims from
  your own knowledge of the paper or its authors.
- **Flag the gaps.** When the excerpt doesn't contain what a section would need —
  common with partial input — say "not covered in the analysed excerpt" rather
  than inventing a plausible-sounding answer. Keep claims conservative and cite
  page numbers where they're clear.

You can render the reading as clean Markdown, but keep every line grounded in the
text.

## Extracting reusable claims (optional, for writing hand-off)

When the reader plans to write from the paper, distil one to three high-value,
reusable claims from it. Make each a precise, typed assertion rather than a
generic summary, and tag it with:

- its **type** — a finding, a method, a framing, or a limitation;
- how strongly the text **supports** it — strongly stated, reasonably implied, or
  speculative;
- the **scope** it holds for (population, context, conditions);
- the **basis** for it (the study design, sample, or metric behind it — don't
  invent specifics);
- your **confidence** in it as stated.

Fewer, sharper claims beat more. Don't assert causal conclusions the text doesn't
make; when the evidence is thin, mark it weak rather than overstating. These
claims feed straight into a writing task (see the synthesis skill) as
pre-vetted, grounded evidence.

## Translation

`fetch_pdf.py` gives you clean per-page text. To produce a translated reading for
a non-English reader, translate the extracted text page by page, keeping
technical terms and proper nouns (method names, gene symbols, model names) in
their original form, and note that the translation covers the analysed excerpt.

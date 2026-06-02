<div align="center">

<img src="assets/cover.png" alt="AcademiCats · Paper Search" width="100%">

<br>

# 🐱 Paper Search · 论文检索

**Find real academic papers across the world's scholarly databases — then read any open-access one in depth. Grounded in real data, never fabricated.**

跨全球学术库检索真实论文，并深度精读任意开放获取 PDF。**有据可查，绝不编造。**

<br>

[![License: MIT](https://img.shields.io/badge/License-MIT-0064F4.svg)](LICENSE)
&nbsp;[![Runs on Claude](https://img.shields.io/badge/runs%20on-Claude-0064F4.svg)](https://claude.com/claude-code)
&nbsp;[![Full product](https://img.shields.io/badge/full%20product-academicats.com-0064F4.svg)](https://academicats.com)

</div>

---

> ### 🪶 This is the **lite, open-source edition** of [**AcademiCats**](https://academicats.com)
> The full product at **[academicats.com](https://academicats.com)** is an AI research workbench that takes you from *finding* papers all the way through *reading, writing, and self-review* — with Google Scholar breadth, Chinese-language sources, saved libraries, a polished UI, and a multi-agent reviewer. This skill is a free, self-contained slice of that workflow you can run on your own Claude.
>
> 这是 [**AcademiCats**](https://academicats.com) 的**开源轻量版**。完整产品在 **academicats.com**——一个从找文献到读、写、自审的 AI 研究工作台。

---

## ✨ What it does

🔍 **Search that means it** — one question fans out across five scholarly databases (OpenAlex, Crossref, arXiv, Semantic Scholar, Europe PMC), de-duplicates, and ranks by genuine research fit — not just keyword overlap.

📄 **Read, not skim** — pick any open-access paper and it resolves the PDF, extracts the text, and gives you a structured, page-anchored reading: the research question, method, key findings, and limitations.

🛡️ **No made-up papers, no made-up findings** — every result is a real record from a public API, and every reading is built only from the actual extracted text. When a paper is paywalled, it says so — it never invents the contents.

<br>

## 🎬 Demo

Just ask Claude, in plain language:

> *"Find me papers since 2020 on CRISPR off-target effects, then deep-read the most relevant open-access one."*

Behind the scenes it runs a real search and hands back a ranked shortlist:

```
# 6 papers for: CRISPR off-target effects
 #  year  cites  OA  score   title
 1  2023    537  Y   56.4  Off-target effects in CRISPR/Cas9 gene editing
 2  2020    451  Y   54.7  Latest Developed Strategies to Minimize the Off-Target Effects…
 3  2026      0  -   46.0  Decoding the role of chromatin context in off-target effects…
 4  2023      7  Y   45.5  Systematic identification of CRISPR off-target effects by CROss-seq
 …
```

…then opens the open-access PDF and reads it back to you with findings tied to page numbers — grounded entirely in the paper's own text.

<br>

## 🚀 Get started in 60 seconds

```bash
# 1. drop this skill where Claude Code can find it
cp -r Cat_paper_search ~/.claude/skills/paper-search

# 2. one tiny dependency (for reading PDFs)
python -m pip install pypdf
```

Then just talk to Claude: *"find recent papers on …"*, *"summarise this arXiv paper …"*. The skill triggers itself — no commands to memorize. Everything runs on your own Claude; all data sources are free and need no API keys.

<br>

## 💙 Why people like it

|  | Paper Search (this skill) | [AcademiCats full product →](https://academicats.com) |
|---|:---:|:---:|
| Real papers, honest reading | ✅ | ✅ |
| Scholarly databases | 5 (key-free) | 14+ incl. Google Scholar & Chinese sources |
| Saved libraries & history | — | ✅ |
| Write & self-review from your sources | — | ✅ Synthesis Lab + Paper Review |
| Polished web & mobile app | — | ✅ |

<div align="center">
<br>

### Want the whole research workflow?
**→ [academicats.com](https://academicats.com) ←**

<br>

Made with 💙 by the [AcademiCats](https://academicats.com) team · [MIT License](LICENSE)

</div>

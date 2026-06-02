<div align="center">

[English](README.md) · **中文**

<img src="assets/cover.png" alt="AcademiCats · Paper Search" width="100%">

<br>

# 🐱 Paper Search · 论文检索

**跨全球学术库检索真实论文，并深度精读任意开放获取 PDF。基于真实数据，绝不编造。**

<br>

[![License: MIT](https://img.shields.io/badge/License-MIT-0064F4.svg)](LICENSE)
&nbsp;[![Runs on Claude](https://img.shields.io/badge/运行于-Claude-0064F4.svg)](https://claude.com/claude-code)
&nbsp;[![Full product](https://img.shields.io/badge/完整产品-academicats.com-0064F4.svg)](https://academicats.com)

</div>

---

> ### 🪶 这是 [**AcademiCats**](https://academicats.com) 的**开源轻量版**
> 完整产品在 **[academicats.com](https://academicats.com)** —— 一个 AI 研究工作台，带你从*找文献*一路走到*读、写、自审*：拥有 Google Scholar 级广度、中文文献源、文献库保存、精致界面和多智能体审稿。本 skill 是这套工作流中一块免费、自包含、可在你自己的 Claude 上运行的切片。

---

## ✨ 它能做什么

🔍 **真正管用的检索** —— 一个问题同时扇出到五大学术库（OpenAlex、Crossref、arXiv、Semantic Scholar、Europe PMC），去重，并按**真实研究契合度**排序，而不只是关键词重叠。

📄 **精读，而非略读** —— 任选一篇开放获取论文，它会解析 PDF、抽取正文，给你一份结构化、**逐条标注页码**的精读：研究问题、方法、核心发现、局限。

🛡️ **不编论文，不编结论** —— 每条结果都是公共 API 的真实记录，每份精读只基于真正抽取到的正文。论文被付费墙挡住时，它会**直说**，绝不杜撰内容。

<br>

## 🎬 演示

直接用大白话问 Claude：

> *"帮我找 2020 年以后关于 CRISPR 脱靶效应的论文，再精读最相关的那篇开放获取论文。"*

它会真实地跑一次检索，给你一份排序好的候选清单：

```
# 6 papers for: CRISPR off-target effects
 #  year  cites  OA  score   title
 1  2023    537  Y   56.4  Off-target effects in CRISPR/Cas9 gene editing
 2  2020    451  Y   54.7  Latest Developed Strategies to Minimize the Off-Target Effects…
 3  2026      0  -   46.0  Decoding the role of chromatin context in off-target effects…
 4  2023      7  Y   45.5  Systematic identification of CRISPR off-target effects by CROss-seq
 …
```

……随后打开那篇开放获取 PDF，把发现逐条标注页码读给你听 —— 完全基于论文自身的正文。

<br>

## 🚀 60 秒上手

```bash
# 1. 把 skill 放到 Claude Code 能发现的位置
cp -r Cat_paper_search ~/.claude/skills/paper-search

# 2. 一个小依赖（用于读 PDF）
python -m pip install pypdf
```

然后直接跟 Claude 说：*"找几篇关于…的最新论文"*、*"总结这篇 arXiv 论文…"*。skill 会**自动触发**，无需记任何命令。全程跑在你自己的 Claude 上，所有数据源免费、无需 API key。

<br>

## 💙 大家为什么喜欢它

|  | Paper Search（本 skill） | [AcademiCats 完整产品 →](https://academicats.com) |
|---|:---:|:---:|
| 真实论文、诚实精读 | ✅ | ✅ |
| 学术数据库 | 5 个（免 key） | 14+，含 Google Scholar 与中文源 |
| 文献库保存与历史 | — | ✅ |
| 据文献写作与自审 | — | ✅ Synthesis Lab + Paper Review |
| 精致的网页与移动端 | — | ✅ |

<div align="center">
<br>

### 想要完整的研究工作流？
**→ [academicats.com](https://academicats.com) ←**

<br>

由 [AcademiCats](https://academicats.com) 团队用 💙 打造 · [MIT 许可证](LICENSE)

</div>

# Verification log

Real captured output of `python examples/verify_dois.py`. Anyone can reproduce
it: clone the repo and run that one command (standard library only, no pip).

```text
Verifying 5 example DOIs against https://doi.org ...

PASS 10.3389/fbioe.2023.1143157  registered (Crossref); resolves -> https://www.frontiersin.org/journals/bioengineering-and-biotechnology/articles/10.3389/fbioe.2023.1143157/full
PASS 10.3390/cells9071608  registered (Crossref); publisher returned 403 to bot
PASS 10.1002/advs.201902312  registered (Crossref); publisher returned 403 to bot
PASS 10.1093/nar/gkac159  registered (Crossref); publisher returned 403 to bot
PASS 10.3389/fbioe.2023.1339189  registered (Crossref); resolves -> https://www.frontiersin.org/journals/bioengineering-and-biotechnology/articles/10.3389/fbioe.2023.1339189/full

All 5 DOIs resolve. Every example paper is a real, published record.
```

Exit code: `0` (non-zero if any DOI fails — so this doubles as a CI guard).

Note on the `403 to bot` lines: those three DOIs (MDPI's *Cells*, Wiley's
*Advanced Science*, Oxford's *Nucleic Acids Research*) are registered and real —
the Crossref registry confirms each one — but their publishers answer automated
clients with HTTP 403. That is the *publisher* blocking the script, not a missing
DOI; opening any of the links in a normal browser loads the article. The two
Frontiers articles allow the bot through and show the final resolved URL.

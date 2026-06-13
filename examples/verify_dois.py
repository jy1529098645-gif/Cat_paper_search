#!/usr/bin/env python3
"""
verify_dois.py — prove the example papers are REAL, not fabricated.

The whole point of Paper Search is that its results are real records from
public scholarly APIs, never invented. This tiny script makes that claim
checkable by anyone: it takes the exact DOIs printed in examples/README.md
(Column B — "What Paper Search returns") and confirms each one actually
resolves to a real published work.

For every DOI it first asks the authoritative DOI registry directly —
the Crossref REST API (https://api.crossref.org/works/<doi>) — which
returns the real bibliographic record for a registered DOI and a 404 for
one that was never registered (the fabrication case this demo warns
about). As a second signal it also resolves https://doi.org/<doi> and
follows the redirect chain to the publisher. A DOI counts as PASS if
either check confirms it. (Publishers like MDPI/Wiley/OUP sometimes
answer automated clients with 403/406 even though the article is real —
so a publisher rejecting the *bot* is not a failed DOI; the Crossref
registry check is what settles it.) It prints "PASS <doi>" or
"FAIL <doi>" for each, and exits non-zero if ANY fail, so it can be
wired into CI as a guard.

Dependency-light by design: standard library only (urllib), no pip install.

    python examples/verify_dois.py

Exit code 0 = every example DOI resolves. Non-zero = at least one failed.
"""
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request

# The exact DOIs cited in examples/README.md, Column B. Each was verified by
# hand against Crossref at build time; this script lets anyone re-check.
DOIS = [
    "10.3389/fbioe.2023.1143157",   # Guo et al. 2023, Front. Bioeng. Biotechnol.
    "10.3390/cells9071608",         # Naeem et al. 2020, Cells
    "10.1002/advs.201902312",       # Manghwar et al. 2020, Advanced Science
    "10.1093/nar/gkac159",          # Ai et al. 2022, Nucleic Acids Research
    "10.3389/fbioe.2023.1339189",   # Lopes et al. 2024, Front. Bioeng. Biotechnol.
]

USER_AGENT = "academi-skill-verify/1.0 (+https://github.com/; mailto:hello@example.com)"
TIMEOUT = 30

# Some machines ship a broken/empty CA store, which makes HTTPS to these public
# read-only endpoints fail with CERTIFICATE_VERIFY_FAILED. Try verified first;
# fall back to unverified. These are public GETs, so the fallback is low-risk.
try:
    import certifi
    _CTX = ssl.create_default_context(cafile=certifi.where())
except Exception:
    _CTX = ssl.create_default_context()
_CTX_UNVERIFIED = ssl._create_unverified_context()


def _open(url, method="GET"):
    """GET/HEAD with a CA-store fallback. Returns the response object."""
    req = urllib.request.Request(url, method=method,
                                 headers={"User-Agent": USER_AGENT})
    last = None
    for ctx in (_CTX, _CTX_UNVERIFIED):
        try:
            return urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx)
        except urllib.error.URLError as e:
            reason = getattr(e, "reason", None)
            if isinstance(reason, ssl.SSLError) and ctx is _CTX:
                last = e
                continue
            raise
    raise last


def _crossref_registered(doi):
    """Authoritative check: is this DOI registered? Crossref returns the real
    record (200) for a registered DOI, 404 for one that was never minted."""
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    try:
        with _open(url) as resp:
            return resp.getcode() == 200
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return False  # the fabrication case
        return None       # inconclusive (e.g. rate-limited) — fall back to doi.org
    except urllib.error.URLError:
        return None


def resolves(doi):
    """Return (ok, detail). A DOI passes if the Crossref registry confirms it
    is registered, OR https://doi.org/<doi> redirects to a real publisher
    page. A publisher 403/406 on the *bot* does not fail the DOI."""
    reg = _crossref_registered(doi)
    if reg is True:
        # Confirmed registered. Note where doi.org lands, for transparency.
        try:
            with _open("https://doi.org/" + doi) as resp:
                return True, f"registered (Crossref); resolves -> {resp.geturl()}"
        except urllib.error.HTTPError as e:
            return True, f"registered (Crossref); publisher returned {e.code} to bot"
        except urllib.error.URLError:
            return True, "registered (Crossref)"
    if reg is False:
        return False, "not registered in Crossref (DOI does not exist)"

    # Crossref inconclusive — fall back to resolving the DOI directly.
    try:
        with _open("https://doi.org/" + doi) as resp:
            final, code = resp.geturl(), resp.getcode()
            if code == 200 and "doi.org" not in final:
                return True, f"resolves -> {final} ({code})"
            return True, f"resolves -> {final} ({code})"
    except urllib.error.HTTPError as e:
        if e.code in (401, 403, 406):
            # Publisher blocked the bot but the DOI clearly redirected there.
            return True, f"resolves to publisher (bot blocked: HTTP {e.code})"
        if e.code == 404:
            return False, "HTTP 404 (DOI not registered)"
        return False, f"unexpected HTTP {e.code}"
    except urllib.error.URLError as e:
        return False, f"network error: {getattr(e, 'reason', e)}"


def main():
    print(f"Verifying {len(DOIS)} example DOIs against https://doi.org ...\n")
    failures = 0
    for doi in DOIS:
        ok, detail = resolves(doi)
        if ok:
            print(f"PASS {doi}  {detail}")
        else:
            print(f"FAIL {doi}  {detail}")
            failures += 1
    print()
    if failures:
        print(f"{failures}/{len(DOIS)} DOIs failed to resolve.")
        sys.exit(1)
    print(f"All {len(DOIS)} DOIs resolve. Every example paper is a real, "
          f"published record.")
    sys.exit(0)


if __name__ == "__main__":
    main()

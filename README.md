Federico Leo Redi — personal academic website for LHCb-focused research.
The deployable static site lives in `public/`; copy its contents to your EOS web root (e.g. `/eos/user/f/fredi/www/`) and share the folder with `a:wwweos` to publish via WebEOS.
Supporting notes sit in `content/` and small helpers in `scripts/`.
Key links: [ORCID](https://orcid.org/0000-0001-9728-8984), [INSPIRE](https://inspirehep.net/authors/Federico.Redi.1), [University of Bergamo](https://www.unibg.it/), [INFN Milan](https://www.mi.infn.it/).
Preview locally with `python -m http.server --directory public` and open `http://localhost:8000/`.
Optional: refresh the recent publications list with `python scripts/fetch_inspire.py` (requires `requests`).

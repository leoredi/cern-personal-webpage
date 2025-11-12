Federico Leo Redi — personal academic website for LHCb-focused research.

## Structure

- `public/` — Final static site ready for deployment to CERN WebEOS
- `content/` — Source markdown files
- `assets/` — Source assets (CSS, images)
- `scripts/` — Build and utility scripts

## Local Development

Serve locally with:
```bash
cd public
python -m http.server
```
Then browse to `http://localhost:8000/`

## Deployment to CERN WebEOS

Simply copy the entire contents of the `public/` directory to your CERN web space.

## Utilities

Update publications: `python scripts/fetch_inspire.py [years_back] [min_citations]` (requires `requests`)

Key links: [ORCID](https://orcid.org/0000-0001-9728-8984), [INSPIRE](https://inspirehep.net/authors/Federico.Redi.1), [University of Bergamo](https://www.unibg.it/).

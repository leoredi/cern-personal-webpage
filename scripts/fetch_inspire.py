#!/usr/bin/env python3
"""Fetch publications from the past 5 years from INSPIRE and write a markdown list.

Usage: python scripts/fetch_inspire.py [years_back] [min_citations]
"""
from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path
from typing import List

import requests

INSPIRE_API = "https://inspirehep.net/api/literature"
AUTHOR_ID = "Federico.Redi.1"
OUTPUT_PATH = Path("content/publications.md")
DEFAULT_YEARS_BACK = 5
DEFAULT_MIN_CITATIONS = 3


def fetch_publications(years_back: int, min_citations: int = 0) -> List[dict]:
    current_year = datetime.now().year
    cutoff_year = current_year - years_back

    params = {
        "q": f"a {AUTHOR_ID}",
        "sort": "mostrecent",
        "size": 1000,  # Set high limit to get all publications
        "fields": "titles,publication_info,earliest_date,citation_count",
    }
    response = requests.get(INSPIRE_API, params=params, timeout=30)
    response.raise_for_status()

    # Filter publications by date and citation count in Python
    all_hits = response.json().get("hits", {}).get("hits", [])
    filtered_hits = []
    for hit in all_hits:
        earliest_date = hit.get("metadata", {}).get("earliest_date", "")
        citation_count = hit.get("metadata", {}).get("citation_count", 0)
        if earliest_date:
            year = int(earliest_date.split("-")[0])
            if year >= cutoff_year and citation_count >= min_citations:
                filtered_hits.append(hit)

    return filtered_hits


def format_entry(hit: dict) -> str:
    metadata = hit.get("metadata", {})
    title = metadata.get("titles", [{}])[0].get("title", "Untitled")
    year = metadata.get("earliest_date", "").split("-")[0]
    record_id = metadata.get("control_number")
    citations = metadata.get("citation_count", 0)
    inspire_url = f"https://inspirehep.net/literature/{record_id}" if record_id else "https://inspirehep.net/"
    return f"- {year} — [{title}]({inspire_url}) — {citations} citations"


def main() -> None:
    years_back = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_YEARS_BACK
    min_citations = int(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_MIN_CITATIONS
    hits = fetch_publications(years_back, min_citations)

    header = f"### Publications (past {years_back} years, ≥{min_citations} citations)"
    lines = [header, ""] + [format_entry(hit) for hit in hits]
    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {len(hits)} entries to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

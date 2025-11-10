#!/usr/bin/env python3
"""Fetch recent publications from INSPIRE and write a markdown list.

Usage: python scripts/fetch_inspire.py [max_items]
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import List

import requests

INSPIRE_API = "https://inspirehep.net/api/literature"
AUTHOR_ID = "Federico.Redi.1"
OUTPUT_PATH = Path("content/publications.md")
DEFAULT_ITEMS = 10


def fetch_publications(limit: int) -> List[dict]:
    params = {
        "q": f"authors:{AUTHOR_ID}",
        "sort": "mostrecent",
        "size": limit,
        "fields": "titles,publication_info,earliest_date",
    }
    response = requests.get(INSPIRE_API, params=params, timeout=30)
    response.raise_for_status()
    return response.json().get("hits", {}).get("hits", [])


def format_entry(hit: dict) -> str:
    title = hit.get("metadata", {}).get("titles", [{}])[0].get("title", "Untitled")
    year = hit.get("metadata", {}).get("earliest_date", "").split("-")[0]
    record_id = hit.get("metadata", {}).get("control_number")
    inspire_url = f"https://inspirehep.net/literature/{record_id}" if record_id else "https://inspirehep.net/"
    return f"- {year} — [{title}]({inspire_url})"


def main() -> None:
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_ITEMS
    hits = fetch_publications(limit)
    lines = ["### Recent publications", ""] + [format_entry(hit) for hit in hits]
    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {len(hits)} entries to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

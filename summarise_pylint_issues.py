#!/usr/bin/env python3
"""Summarize pylint issues by type (error/warning/info) and symbol.
Usage:
    python summarize_pylint_by_type_and_symbol.py pylint_components.json
"""

from collections import Counter, defaultdict
import json
import sys

if len(sys.argv) < 2:
    print("Usage: python summarize_pylint_by_type_and_symbol.py pylint_all.json")
    sys.exit(1)

path = sys.argv[1]

# --- Efficient parsing for large JSON files ---
print(f"Reading {path} ...")
with open(path, encoding="utf-8") as f:
    data = json.load(f)

# --- Count (type, symbol) combinations ---
counts = Counter((item["type"], item["symbol"]) for item in data)

# --- Group results by type for readability ---
grouped = defaultdict(list)
for (issue_type, symbol), count in counts.items():
    grouped[issue_type].append((symbol, count))

# --- Print results ---
for issue_type in sorted(grouped.keys()):
    print(f"\n=== {issue_type.upper()}S ===")
    print(f"{'Symbol':40} Count")
    print("-" * 55)
    for symbol, count in sorted(grouped[issue_type], key=lambda x: -x[1]):
        print(f"{symbol:40} {count}")

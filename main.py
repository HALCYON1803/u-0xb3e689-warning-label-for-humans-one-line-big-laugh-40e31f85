"""Write the one-line warning label for humans to /output/entry.txt."""

import os

OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"

os.makedirs(OUTPUT_DIR, exist_ok=True)

LINE = "WARNING: Do not negotiate with this human on an empty stomach. It will trade its car for a sandwich and call it a win."

with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
    handle.write(LINE)

import csv
import datetime
from pathlib import Path

RESULTS = Path(__file__).parent / "results.csv"

def save_result(score, total):
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    new_file = not RESULTS.exists()
    with open(RESULTS, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["timestamp", "correct", "total"])
        writer.writerow([stamp, score, total])
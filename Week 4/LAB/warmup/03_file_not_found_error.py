# completed warm-up

from pathlib import Path

records_path = Path(__file__).resolve().parents[1] / "records.txt"
with records_path.open(encoding="utf-8") as f:
    print(f.read())

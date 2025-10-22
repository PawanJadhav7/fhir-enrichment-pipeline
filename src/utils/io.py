from pathlib import Path
import json
import pandas as pd

# Project paths
DATA = Path("data")
RAW = DATA / "raw"
PROC = DATA / "processed"
REF = DATA / "reference"
PROC.mkdir(parents=True, exist_ok=True)

def read_fhir_folder(resource: str) -> list[dict]:
    """
    Read all JSON files for a FHIR resource (e.g., Patient, Encounter, Observation)
    from data/raw/<Resource> into a list of dicts.
    """
    base = RAW / resource
    rows: list[dict] = []
    if not base.exists():
        return rows
    for p in sorted(base.glob("*.json")):
        with open(p, "r") as f:
            rows.append(json.load(f))
    return rows

def write_parquet(df: pd.DataFrame, name: str) -> None:
    """Write a DataFrame to data/processed/<name>.parquet."""
    out = PROC / f"{name}.parquet"
    df.to_parquet(out, index=False)
    print(f"[write] {out} ({len(df)} rows)")
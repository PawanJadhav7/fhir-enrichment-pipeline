import pandas as pd
from src.utils.io import REF, PROC, write_parquet

def main():
    enc = pd.read_parquet(PROC / "bronze_encounter.parquet")
    obs = pd.read_parquet(PROC / "bronze_observation.parquet")

    icd = pd.read_csv(REF / "icd10_to_category.csv")     # columns: code,category
    loinc = pd.read_csv(REF / "loinc_to_group.csv")      # columns: loinc,group

    enc2 = (
        enc.merge(icd, how="left", left_on="icd10", right_on="code")
           .drop(columns=["code"])
           .rename(columns={"category": "icd10_category"})
    )

    obs2 = (
        obs.merge(loinc, how="left", on="loinc")
           .rename(columns={"group": "loinc_group"})
    )

    write_parquet(enc2, "silver_encounter_enriched")
    write_parquet(obs2, "silver_observation_enriched")

if __name__ == "__main__":
    main()
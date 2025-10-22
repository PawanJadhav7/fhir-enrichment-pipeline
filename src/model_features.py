import pandas as pd
from src.utils.io import PROC

def main():
    obs = pd.read_parquet(PROC / "silver_observation_enriched.parquet").copy()
    obs["value_num"] = pd.to_numeric(obs["value"], errors="coerce")

    # Example feature: lactate > 2.0 flagged when loinc_group == 'lactate'
    obs["abnormal_flag"] = (
        (obs["loinc_group"] == "lactate") & (obs["value_num"] > 2.0)
    ).astype(int)

    feats = (
        obs.groupby("encounter_id", dropna=False)
           .agg(lactate_high=("abnormal_flag", "max"),
                obs_count=("obs_id", "count"))
           .reset_index()
    )

    feats.to_parquet(PROC / "features_sepsis.parquet", index=False)
    print("[write] data/processed/features_sepsis.parquet")

if __name__ == "__main__":
    main()
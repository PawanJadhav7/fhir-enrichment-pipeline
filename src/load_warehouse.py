import pandas as pd
from src.utils.io import PROC, write_parquet

def main():
    pat = pd.read_parquet(PROC / "bronze_patient.parquet")
    enc = pd.read_parquet(PROC / "silver_encounter_enriched.parquet")
    obs = pd.read_parquet(PROC / "silver_observation_enriched.parquet")
    feats = pd.read_parquet(PROC / "features_sepsis.parquet")

    # Simple star schema artifacts
    patient_dim = pat[["patient_id", "gender", "birthDate"]].drop_duplicates()
    write_parquet(patient_dim, "patient_dim")

    encounter_fact = enc.merge(feats, on="encounter_id", how="left")
    write_parquet(encounter_fact, "encounter_fact")

    write_parquet(obs, "lab_observations")

if __name__ == "__main__":
    main()
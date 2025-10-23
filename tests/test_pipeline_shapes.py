import pandas as pd, pathlib as p

def test_core_outputs_exist():
    base = p.Path("data/processed")
    for name in [
        "bronze_patient","bronze_encounter","bronze_observation",
        "silver_encounter_enriched","silver_observation_enriched",
        "features_sepsis","patient_dim","encounter_fact","lab_observations",
    ]:
        assert (base / f"{name}.parquet").exists()
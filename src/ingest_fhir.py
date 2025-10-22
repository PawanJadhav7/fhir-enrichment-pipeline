from src.utils.io import read_fhir_folder, write_parquet
from src.utils.fhir_utils import flatten_patient, flatten_encounter, flatten_observation

def main():
    patients = flatten_patient(read_fhir_folder("Patient"))
    encounters = flatten_encounter(read_fhir_folder("Encounter"))
    observations = flatten_observation(read_fhir_folder("Observation"))

    write_parquet(patients, "bronze_patient")
    write_parquet(encounters, "bronze_encounter")
    write_parquet(observations, "bronze_observation")

if __name__ == "__main__":
    main()
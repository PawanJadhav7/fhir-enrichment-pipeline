# 🏥 FHIR Enrichment Pipeline

**Goal:** Build a reproducible pipeline that ingests synthetic **FHIR** resources, **validates data quality**, **enriches** with clinical vocab mappings (ICD-10, LOINC), and produces curated **analytics-ready tables** (star schema + features) for sepsis/acute-care use-cases.

**Why it matters:** Shows industry-ready Data Engineering across healthcare (FHIR/HL7), with reproducibility, testing, and CI.

## Stack

-   **Python** (pandas, pyarrow, pandera), **R** (R Markdown)
-   Storage: **Parquet** (local) – optionally Snowflake/Redshift
-   Orchestration: **Makefile** (local); GitHub **Actions** for CI
-   Container: **Docker**
-   Synthetic data: generate with **Synthea** or use included samples

## Pipeline

1.  **Ingest**: parse FHIR JSON (Patient, Encounter, Observation) → bronze parquet (`data/processed/bronze_*`)
2.  **Validate**: schema and DQ checks (not_null, accepted_values, referential integrity)
3.  **Enrich**: map ICD-10 to high-level categories; group LOINC; derive clinically relevant flags (e.g., abnormal labs)
4.  **Model**: produce **star schema** (patient_dim, date_dim, encounter_fact, lab_obs_fact) + **features** for risk signals
5.  **Load**: keep parquet locally; optional load to Snowflake/Redshift (SQL provided)

## Quickstart

```bash
# 0) Clone the repository
git clone https://github.com/PawanJadhav7/fhir-enrichment-pipeline.git
cd fhir-enrichment-pipeline

# 1) Create and activate virtual environment
python -m venv .venv && source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Place synthetic FHIR JSON in data/raw/
# Example: data/raw/Patient/*.json, Encounter/*.json, Observation/*.json

# 4) Run the full pipeline
make all

# 5) (Optional) Run steps individually
make ingest
make dq
make enrich
make features
make star

# 6) View outputs
tree data/processed
```
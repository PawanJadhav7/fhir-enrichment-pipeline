import pandera as pa
import pandas as pd
from src.utils.io import PROC

patient_schema = pa.DataFrameSchema(
    {
        "patient_id": pa.Column(pa.String, nullable=False),
        "gender": pa.Column(pa.String, checks=pa.Check.isin(["male","female","other","unknown",""]), nullable=True),
        "birthDate": pa.Column(pa.String, nullable=True),
    },
    coerce=True,
)

def validate(name: str, schema: pa.DataFrameSchema) -> None:
    df = pd.read_parquet(PROC / f"{name}.parquet")
    schema.validate(df, lazy=True)
    print(f"[dq] {name} OK ({len(df)} rows)")

def main():
    validate("bronze_patient", patient_schema)

if __name__ == "__main__":
    main()
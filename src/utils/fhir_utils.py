import pandas as pd

def flatten_patient(objs: list[dict]) -> pd.DataFrame:
    rows = []
    for o in objs:
        rows.append({
            "patient_id": o.get("id"),
            "gender": (o.get("gender") or "").lower(),
            "birthDate": o.get("birthDate")
        })
    return pd.DataFrame(rows)

def flatten_encounter(objs: list[dict]) -> pd.DataFrame:
    rows = []
    for o in objs:
        rows.append({
            "encounter_id": o.get("id"),
            "patient_id": (o.get("subject") or {}).get("reference", "").replace("Patient/",""),
            "class": (o.get("class") or {}).get("code"),
            "start": (o.get("period") or {}).get("start"),
            "end": (o.get("period") or {}).get("end"),
            "icd10": (o.get("diagnosis", [{}])[0]
                        .get("condition", {})
                        .get("coding", [{}])[0]
                        .get("code"))
        })
    return pd.DataFrame(rows)

def flatten_observation(objs: list[dict]) -> pd.DataFrame:
    rows = []
    for o in objs:
        coding = (o.get("code") or {}).get("coding", [{}])[0]
        vq = o.get("valueQuantity", {}) or {}
        rows.append({
            "obs_id": o.get("id"),
            "patient_id": (o.get("subject") or {}).get("reference","").replace("Patient/",""),
            "encounter_id": (o.get("encounter") or {}).get("reference","").replace("Encounter/",""),
            "loinc": coding.get("code"),
            "display": coding.get("display"),
            "value": vq.get("value"),
            "unit": vq.get("unit"),
            "effectiveDateTime": o.get("effectiveDateTime")
        })
    return pd.DataFrame(rows)
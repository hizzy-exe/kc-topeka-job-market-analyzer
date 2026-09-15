from __future__ import annotations
from pathlib import Path
import pandas as pd
import config

def clean_raw_data(input_path: Path | None = None, output_path: Path | None = None) -> Path:
    input_path = input_path or config.RAW_JOBS_CSV
    output_path = output_path or config.CLEANED_JOBS_CSV

    if not input_path.exists():
        raise FileNotFoundError(f"Raw data missing: {input_path}")

    print("Cleaning and normalizing data...")
    df = pd.read_csv(input_path)

    df["Job_Title"] = df["Job_Title"].astype(str).str.strip()
    df["Company_Employer"] = df["Company_Employer"].astype(str).str.strip().replace({"": "Unknown / Agency"})
    df["Location"] = df["Location"].astype(str).str.strip()
    df["Work_Mode"] = df["Work_Mode"].fillna("On-site").astype(str).str.strip()
    df["Skills_Required"] = df["Skills_Required"].fillna("General Tech").astype(str)

    for col in ("Salary_Min", "Salary_Max", "Salary_Estimate"):
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Fill missing estimate with average of min/max when possible
    if "Salary_Estimate" in df.columns and "Salary_Min" in df.columns and "Salary_Max" in df.columns:
        mask = df["Salary_Estimate"].isna()
        df.loc[mask, "Salary_Estimate"] = (df["Salary_Min"] + df["Salary_Max"]) / 2

    df = df[df["Job_Title"].str.len() > 2].copy()

    if "job_id" in df.columns:
        df = df.drop_duplicates(subset=["job_id"], keep="first")

    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved → {output_path} ({len(df)} rows)")
    return output_path
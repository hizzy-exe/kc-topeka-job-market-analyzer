from __future__ import annotations
from pathlib import Path
from typing import Any
import pandas as pd
import config

def run_market_analysis(input_path: Path | None = None) -> dict[str, Any]:
    input_path = input_path or config.CLEANED_JOBS_CSV
    if not input_path.exists():
        raise FileNotFoundError(f"Cleaned data not found: {input_path}")

    print("Running market analysis...")
    df = pd.read_csv(input_path)
    results = {}

    # Salary
    salary_df = df.dropna(subset=["Salary_Estimate"])
    if not salary_df.empty:
        results["salary_by_title"] = (
            salary_df.groupby("Job_Title")["Salary_Estimate"]
            .agg(["mean", "median", "count"])
            .round(0)
            .sort_values("count", ascending=False)
            .head(12)
            .to_dict(orient="index")
        )
        results["overall_salary"] = {
            "mean": float(salary_df["Salary_Estimate"].mean()),
            "median": float(salary_df["Salary_Estimate"].median()),
            "count_with_salary": int(len(salary_df)),
            "pct_with_salary": round(100 * len(salary_df) / len(df), 1),
        }
    else:
        results["salary_by_title"] = {}
        results["overall_salary"] = {}

    # Work mode
    results["work_mode_breakdown"] = df["Work_Mode"].value_counts(normalize=True).round(4).to_dict()

    # Skills
    all_skills = []
    for val in df["Skills_Required"].dropna():
        for s in str(val).split(","):
            skill = s.strip()
            if skill and skill.lower() != "general tech":
                all_skills.append(skill)
    results["top_skills"] = pd.Series(all_skills).value_counts().head(12).to_dict() if all_skills else {}

    # Employers & Locations
    results["top_employers"] = df["Company_Employer"].value_counts().head(12).to_dict()
    results["location_counts"] = df["Location"].value_counts().head(12).to_dict()

    results["summary_stats"] = {
        "total_postings": int(len(df)),
        "unique_titles": int(df["Job_Title"].nunique()),
        "unique_employers": int(df["Company_Employer"].nunique()),
        "unique_locations": int(df["Location"].nunique()),
    }
    return results
import os
import pandas as pd

def run_market_analysis():
    print("Computing metrics and skill tallies...")
    input_path = os.path.join("data", "processed", "cleaned_job_postings.csv")
    
    df = pd.read_csv(input_path)
    
    # Metric 1: Salary Benchmarks by Job Title
    salary_summary = df.groupby("Job_Title")["Salary_Estimate"].mean().to_dict()
    
    # Metric 2: Market Density of Remote vs On-Site Roles
    work_mode_breakdown = df["Work_Mode"].value_counts(normalize=True).to_dict()
    
    # Metric 3: Technical Skills frequency profiling
    all_skills = []
    df["Skills_Required"].dropna().str.split(", ").apply(all_skills.extend)
    skills_series = pd.Series(all_skills).value_counts().head(5).to_dict()
    
    return salary_summary, work_mode_breakdown, skills_series

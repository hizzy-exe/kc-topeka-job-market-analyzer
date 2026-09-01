import os
import pandas as pd

def run_market_analysis():
    print("Computing metrics and employer tallies...")
    input_path = os.path.join("data", "processed", "cleaned_job_postings.csv")
    
    df = pd.read_csv(input_path)
    
    # 1. Salary Benchmarks
    salary_summary = df.groupby("Job_Title")["Salary_Estimate"].mean().to_dict()
    
    # 2. Work Mode Split
    work_mode_breakdown = df["Work_Mode"].value_counts(normalize=True).to_dict()
    
    # 3. Technical Skills
    all_skills = []
    df["Skills_Required"].dropna().str.split(", ").apply(all_skills.extend)
    skills_series = pd.Series(all_skills).value_counts().head(5).to_dict()
    
    # NEW METRIC 4: Identify Top Active Hiring Employers!
    top_employers = df["Company_Employer"].value_counts().head(5).to_dict()
    
    return salary_summary, work_mode_breakdown, skills_series, top_employers

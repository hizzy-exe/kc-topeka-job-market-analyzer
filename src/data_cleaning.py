import os
import pandas as pd

def clean_raw_data():
    print("Transforming and filtering data records...")
    input_path = os.path.join("data", "raw", "raw_job_postings.csv")
    output_path = os.path.join("data", "processed", "cleaned_job_postings.csv")
    
    if not os.path.exists(input_path):
        raise FileNotFoundError("Raw data missing. Run collection module first.")
        
    df = pd.read_csv(input_path)
    
    # Standardizing texts and cleaning whitespace anomalies
    df["Job_Title"] = df["Job_Title"].str.strip()
    df["Location"] = df["Location"].str.strip()
    
    # Standardizing numeric outputs and checking outliers
    df["Salary_Estimate"] = pd.to_numeric(df["Salary_Estimate"], errors="coerce")
    df = df.dropna(subset=["Salary_Estimate", "Job_Title"])
    
    df.to_csv(output_path, index=False)
    print("Cleaned records saved to processed layer: " + output_path)

if __name__ == "__main__":
    clean_raw_data()

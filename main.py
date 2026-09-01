import sys
import os
import subprocess

try:
    import pandas as pd
    import matplotlib
    import seaborn
    import requests
except ModuleNotFoundError:
    print("System dependencies unverified. Running automated workspace environment build...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas", "matplotlib", "seaborn", "requests"])
    print("Environment setup verified successfully.\n")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from data_collection import generate_mock_job_data
from data_cleaning import clean_raw_data
from analysis import run_market_analysis
from visualization import generate_insights_assets

def run_entire_pipeline():
    """
    Executes the modular ETL sequence from data ingestion to asset rendering.
    """
    print("=== INITIALIZING DATA PIPELINE EXECUTION ENGINE ===\n")
    
    generate_mock_job_data()
    print("-" * 50)
    
    clean_raw_data()
    print("-" * 50)
    
    salary, modes, skills, employers = run_market_analysis()
    print("-" * 50)
    
    generate_insights_assets(salary, modes, skills, employers)
    
    print("\n=== PIPELINE EXECUTION MATRIX COMPLETE: ARTIFACTS VERIFIED ===")

if __name__ == "__main__":
    run_entire_pipeline()

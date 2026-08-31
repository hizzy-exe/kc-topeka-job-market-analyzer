import sys
import os
import subprocess

# --- AUTOMATIC ENV FIXER ---
# This forces Wing 101's exact Python instance to install Pandas if missing
try:
    import pandas as pd
    import matplotlib
    import seaborn
except ModuleNotFoundError:
    print("Missing required libraries. Launching auto-installer inside Wing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas", "matplotlib", "seaborn"])
    print("Installation complete! Restarting pipeline...\n")
# ---------------------------

# Connect the internal source path variables to the running python instance
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from data_collection import generate_mock_job_data
from data_cleaning import clean_raw_data
from analysis import run_market_analysis
from visualization import generate_insights_assets

def run_entire_pipeline():
    print("=== STARTING KC-TOPEKA MARKET ANALYSIS PIPELINE ===\n")
    
    # 1. Extraction / Collection
    generate_mock_job_data()
    print("-" * 50)
    
    # 2. Transformation / Cleaning
    clean_raw_data()
    print("-" * 50)
    
    # 3. Calculation / Analysis
    salary, modes, skills = run_market_analysis()
    print("-" * 50)
    
    # 4. Production Reporting & Charting
    generate_insights_assets(salary, modes, skills)
    
    print("\n=== PIPELINE PROCESS COMPLETE: CHECK YOUR OUTPUTS DIRECTORY ===")

if __name__ == "__main__":
    run_entire_pipeline()

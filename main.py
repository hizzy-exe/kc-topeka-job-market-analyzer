import sys
import os
import subprocess

# --- AUTOMATIC ENV FIXER (UPDATED) ---
try:
    import pandas as pd
    import matplotlib
    import seaborn
    import requests  # <-- Added the missing live-web module here!
except ModuleNotFoundError:
    print("Missing web or data libraries. Launching auto-installer inside Wing...")
    # This instructs Python to download everything including requests
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas", "matplotlib", "seaborn", "requests"])
    print("Installation complete! Restarting pipeline...\n")
# -------------------------------------

# Connect the internal source path variables to the running python instance
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from data_collection import generate_mock_job_data
from data_cleaning import clean_raw_data
from analysis import run_market_analysis
from visualization import generate_insights_assets


def run_entire_pipeline():
    print("=== STARTING KC-TOPEKA MARKET ANALYSIS PIPELINE ===\n")
    
    generate_mock_job_data()
    print("-" * 50)
    
    clean_raw_data()
    print("-" * 50)
    
    # Updated: Destructure the 4 outputs from our calculations engine
    salary, modes, skills, employers = run_market_analysis()
    print("-" * 50)
    
    # Updated: Forward all 4 metrics to your final text builder
    generate_insights_assets(salary, modes, skills, employers)
    
    print("\n=== PIPELINE PROCESS COMPLETE: CHECK YOUR OUTPUTS DIRECTORY ===")

if __name__ == "__main__":
    run_entire_pipeline()

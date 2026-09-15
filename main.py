#!/usr/bin/env python3
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from src.data_collection import collect_jobs
from src.data_cleaning import clean_raw_data
from src.analysis import run_market_analysis
from src.visualization import generate_insights_assets

def run_entire_pipeline():
    print("=" * 60)
    print("  KC-TOPEKA JOB MARKET ANALYZER – REAL ETL PIPELINE")
    print("=" * 60)
    print()

    print("[1/4] EXTRACT – Fetching live data from Adzuna...")
    collect_jobs()
    print("-" * 50)

    print("[2/4] TRANSFORM – Cleaning records...")
    clean_raw_data()
    print("-" * 50)

    print("[3/4] ANALYZE – Computing metrics...")
    analysis = run_market_analysis()
    print("-" * 50)

    print("[4/4] LOAD – Generating charts & report...")
    generate_insights_assets(analysis)

    print()
    print("=" * 60)
    print("  PIPELINE COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    run_entire_pipeline()
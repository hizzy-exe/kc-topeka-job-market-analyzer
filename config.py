import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DATA_RAW_DIR = BASE_DIR / "data" / "raw"
DATA_PROCESSED_DIR = BASE_DIR / "data" / "processed"
OUTPUT_CHARTS_DIR = BASE_DIR / "output" / "charts"
OUTPUT_REPORTS_DIR = BASE_DIR / "output" / "reports"

for d in [DATA_RAW_DIR, DATA_PROCESSED_DIR, OUTPUT_CHARTS_DIR, OUTPUT_REPORTS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

ADZUNA_APP_ID = os.getenv("ADZUNA_APP_ID", "")
ADZUNA_APP_KEY = os.getenv("ADZUNA_APP_KEY", "")

COUNTRY = "us"
RESULTS_PER_PAGE = 50
MAX_PAGES = 4

SEARCH_QUERIES = [
    {"what": "data analyst OR data scientist OR business analyst", "where": "Kansas City", "label": "kc_data"},
    {"what": "software engineer OR python developer OR data engineer", "where": "Kansas City", "label": "kc_eng"},
    {"what": "data analyst OR data scientist OR python", "where": "Topeka", "label": "topeka"},
    {"what": "software engineer OR developer", "where": "Overland Park", "label": "op"},
]

TARGET_SKILLS = [
    "python", "sql", "tableau", "power bi", "powerbi", "excel",
    "aws", "azure", "gcp", "spark", "airflow", "dbt",
    "machine learning", "pandas", "numpy", "scikit-learn",
    "docker", "kubernetes", "snowflake", "databricks", "looker"
]

RAW_JOBS_CSV = DATA_RAW_DIR / "raw_job_postings.csv"
CLEANED_JOBS_CSV = DATA_PROCESSED_DIR / "cleaned_job_postings.csv"
EXECUTIVE_SUMMARY = OUTPUT_REPORTS_DIR / "executive_summary.txt"
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
DATA_PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")
OUTPUT_CHARTS_DIR = os.path.join(BASE_DIR, "output", "charts")
OUTPUT_REPORTS_DIR = os.path.join(BASE_DIR, "output", "reports")

TARGET_LOCATIONS = ["Kansas City", "Topeka", "Overland Park", "Olathe"]
TARGET_ROLES = ["Data Analyst", "Business Analyst", "Software Engineer", "Python Developer", "Data Scientist", "Financial Analyst"]

for directory in [DATA_RAW_DIR, DATA_PROCESSED_DIR, OUTPUT_CHARTS_DIR, OUTPUT_REPORTS_DIR]:
    os.makedirs(directory, exist_ok=True)

# KC–Topeka Job Market Analyzer

An automated end-to-end **Extract, Transform, Load (ETL)** pipeline that collects, cleans, and analyzes live job postings for data science, data engineering, and software roles across the Kansas City and Topeka metropolitan areas.

The pipeline pulls real-time data from the Adzuna Jobs API, normalizes the records, extracts in-demand skills and work-mode signals, and produces summary statistics, visualizations, and an executive report.

## Features

- Live data collection from the Adzuna API with retry logic and rate limiting
- Structured cleaning and deduplication of job postings
- Automated extraction of technical skills and work-mode classification (Remote / Hybrid / On-site)
- Salary distribution analysis and employer/location rankings
- Generation of charts and a plain-text executive summary report

## Project Structure

kc-topeka-job-market-analyzer/
├── main.py                 # Pipeline orchestrator
├── config.py               # Configuration and path management
├── visualization.py        # Chart and report generation
├── src/
│   ├── data_collection.py  # API extraction
│   ├── data_cleaning.py    # Data transformation
│   └── analysis.py         # Market analysis
├── data/
│   ├── raw/                # Raw API output
│   └── processed/          # Cleaned datasets
├── output/
│   ├── charts/             # Generated visualizations
│   └── reports/            # Executive summary
├── .env.example
├── requirements.txt
└── README.md

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/hizzy-exe/kc-topeka-job-market-analyzer.git
   cd kc-topeka-job-market-analyzer

2. Create and activate a virtual environment (recommended):
   python -m venv venv
   source venv/bin/activate    #Windows: venv\Scripts\activate

3. Install Dependencies:
   pip install -r requirements.txt

4. Configure API credentials:
   Copy .env.example to .env
   Obtain free API keys from Adzuna Developer Portal
   Add your credentials

5. Run the full pipeline:
   python main.py

The pipeline executes four stages:

Extract – Fetches live job postings from Adzuna
Transform – Cleans and normalizes the data
Analyze – Computes salary, skill, employer, and work-mode metrics
Load – Generates charts and an executive summary report

Outputs are written to the data/ and output/ directories.
Requirements

Python 3.10+
Adzuna API credentials (free tier is sufficient)
Dependencies listed in requirements.txt

License
This project is provided for educational and portfolio purposes.
  

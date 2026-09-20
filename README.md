# KC–Topeka Job Market Analyzer

An automated end-to-end Extract, Transform, Load (ETL) pipeline that collects, cleans, and analyzes live job postings for data science, data engineering, and software roles across the Kansas City and Topeka metropolitan areas.

The pipeline pulls real-time data from the Adzuna Jobs API, normalizes the records, extracts in-demand skills and work-mode signals, and produces summary statistics, visualizations, and an executive report.


## Features

- Live data collection from the Adzuna API with retry logic and rate limiting
- Structured cleaning and deduplication of job postings
- Automated extraction of technical skills and work-mode classification (Remote / Hybrid / On-site)
- Salary distribution analysis and employer/location rankings
- Generation of charts and a plain-text executive summary report


## Setup

**1. Clone the repository**

git clone https://github.com/hizzy-exe/kc-topeka-job-market-analyzer.git
cd kc-topeka-job-market-analyzer


**2. Create and activate a virtual environment**

python -m venv venv
source venv/bin/activate

On Windows use:
venv\Scripts\activate


**3. Install dependencies**

pip install -r requirements.txt


**4. Configure API credentials**

- Copy `.env.example` to `.env`
- Get free keys from https://developer.adzuna.com/
- Add them to the `.env` file:
ADZUNA_APP_ID=your_app_id_here
ADZUNA_APP_KEY=your_app_key_here


## Usage

Run the full pipeline:
python main.py


The pipeline runs in four stages:

1. Extract – Fetches live job postings from Adzuna
2. Transform – Cleans and normalizes the data
3. Analyze – Computes salary, skill, employer, and work-mode metrics
4. Load – Generates charts and an executive summary report

Outputs are saved in the `data/` and `output/` folders.


## Project Structure

kc-topeka-job-market-analyzer/
├── main.py
├── config.py
├── src/
│   ├── init.py
│   ├── data_collection.py
│   ├── data_cleaning.py
│   ├── analysis.py
│   └── visualization.py
├── data/
│   ├── raw/
│   └── processed/
├── output/
│   ├── charts/
│   └── reports/
├── .env.example
├── requirements.txt
└── README.md


## Requirements

- Python 3.10+
- Adzuna API credentials (free tier works)
- Packages listed in `requirements.txt`

## License

This project is provided for educational and portfolio purposes.

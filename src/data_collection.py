import os
import csv
import random
import requests

APP_ID = "8a8e991f"
APP_KEY = "711536fcb2d234beaf4d4f597b97885b"

def generate_mock_job_data():
    """
    Orchestrates the retrieval of regional job market data.
    Attempts to pull live feeds via the Adzuna API, with automatic local failover.
    """
    output_path = os.path.join("data", "raw", "raw_job_postings.csv")
    
    if APP_ID == "YOUR_ADZUNA_APP_ID" or APP_KEY == "YOUR_ADZUNA_APP_KEY":
        print("Default placeholders detected. Activating offline fallback generator...")
        run_fallback_generator(output_path)
        return

    print("Establishing connection to Adzuna web API endpoints...")
    base_url = "https://adzuna.com"
    parameters = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": "Python data analyst developer",
        "where": "Kansas",
        "content-type": "application/json"
    }
    
    try:
        response = requests.get(base_url, params=parameters, timeout=15)
        response.raise_for_status()
        data = response.json()
        job_listings = data.get("results", [])
        
        print(f"Successfully ingested {len(job_listings)} live regional data points.")
        
        with open(output_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Job_Title", "Company_Employer", "Location", "Salary_Estimate", "Skills_Required", "Work_Mode"])
            
            for job in job_listings:
                title = job.get("title", "Unknown Role").strip()
                company_data = job.get("company", {})
                employer = company_data.get("display_name", "Hidden / Staffing Agency").strip()
                loc_data = job.get("location", {})
                loc_display = loc_data.get("display_name", "Kansas City Area").strip()
                salary = job.get("salary_max", job.get("salary_min", 75000))
                
                description = job.get("description", "").lower()
                detected_tools = []
                for tool in ["python", "sql", "tableau", "excel", "powerbi", "aws"]:
                    if tool in description:
                        detected_tools.append(tool.capitalize())
                skills_str = ", ".join(detected_tools) if detected_tools else "General Tech"
                mode = "Remote" if any(x in description for x in ["remote", "work from home"]) else "On-site"
                
                writer.writerow([title, employer, loc_display, salary, skills_str, mode])
        print("Ingested production dataset saved to raw directory layer.")
        
    except Exception as error:
        print(f"API pipeline disruption encountered ({error}). Executing local fallback...")
        run_fallback_generator(output_path)

def run_fallback_generator(output_path):
    """
    Generates structured regional records to maintain down-stream execution schema.
    """
    locations = ["Kansas City, MO", "Kansas City, KS", "Topeka, KS", "Overland Park, KS", "Olathe, KS"]
    roles = ["Data Analyst", "Business Analyst", "Software Engineer", "Python Developer", "Data Scientist", "Financial Analyst"]
    employers = ["Garmin", "T-Mobile", "H&R Block", "Commerce Bank", "Federal Reserve Bank of KC"]
    skills_pool = ["Python", "SQL", "Tableau", "Excel", "PowerBI", "AWS"]
    work_modes = ["Remote", "On-site", "Hybrid"]
    
    with open(output_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Job_Title", "Company_Employer", "Location", "Salary_Estimate", "Skills_Required", "Work_Mode"])
        
        for _ in range(200):
            writer.writerow([
                random.choice(roles),
                random.choice(employers),
                random.choice(locations),
                random.randint(85000, 135000) if any(x in random.choice(roles) for x in ["Scientist", "Engineer"]) else random.randint(60000, 95000),
                ", ".join(random.sample(skills_pool, k=random.randint(2, 4))),
                random.choice(work_modes)
            ])
            
    print("Localized fallback dataset initialized smoothly.")

if __name__ == "__main__":
    generate_mock_job_data()

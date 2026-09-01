
import os
import csv
import random
import requests

APP_ID = "8a8e991f"
APP_KEY = "711536fcb2d234beaf4d4f597b97885b"

def generate_mock_job_data():
    output_path = os.path.join("data", "raw", "raw_job_postings.csv")
    
    # If keys are placeholders, skip the web request entirely to save time
    if APP_ID == "YOUR_ADZUNA_APP_ID" or APP_KEY == "YOUR_ADZUNA_APP_KEY":
        print("Placeholder API credentials detected. Activating offline fallback generator...")
        run_fallback_generator(output_path)
        return

    print("Connecting to live Adzuna web API servers...")
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
        
        print(f"Successfully retrieved {len(job_listings)} live regional jobs.")
        
        with open(output_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Job_Title", "Company_Employer", "Location", "Salary_Estimate", "Skills_Required", "Work_Mode"])
            
            for job in job_listings:
                title = job.get("title", "Unknown Role")
                company_data = job.get("company", {})
                employer = company_data.get("display_name", "Hidden / Staffing Agency")
                loc_data = job.get("location", {})
                loc_display = loc_data.get("display_name", "Kansas City Area")
                salary = job.get("salary_max", job.get("salary_min", 75000))
                
                description = job.get("description", "").lower()
                detected_tools = []
                for tool in ["python", "sql", "tableau", "excel", "powerbi", "aws"]:
                    if tool in description:
                        detected_tools.append(tool.capitalize())
                skills_str = ", ".join(detected_tools) if detected_tools else "General Tech"
                mode = "Remote" if "remote" in description or "work from home" in description else "On-site"
                
                writer.writerow([title, employer, loc_display, salary, skills_str, mode])
        print("Live real-time records saved successfully.")
        
    except Exception as error:
        print(f"API Connection Failure ({error}). Running offline fallback generator...")
        run_fallback_generator(output_path)

def run_fallback_generator(output_path):
    """Generates realistic local data WITH the Employer column to protect the pipeline."""
    locations = ["Kansas City, MO", "Kansas City, KS", "Topeka, KS", "Overland Park, KS", "Olathe, KS"]
    roles = ["Data Analyst", "Business Analyst", "Software Engineer", "Python Developer", "Data Scientist", "Financial Analyst"]
    employers = ["Garmin", "Cerner Corporation", "T-Mobile", "H&R Block", "Commerce Bank", "Federal Reserve Bank of KC"]
    skills_pool = ["Python", "SQL", "Tableau", "Excel", "PowerBI", "AWS"]
    work_modes = ["Remote", "On-site", "Hybrid"]
    
    with open(output_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Job_Title", "Company_Employer", "Location", "Salary_Estimate", "Skills_Required", "Work_Mode"])
        
        for _ in range(200):
            role = random.choice(roles)
            emp = random.choice(employers)
            loc = random.choice(locations)
            mode = random.choice(work_modes)
            salary = random.randint(85000, 135000) if "Scientist" in role or "Engineer" in role else random.randint(60000, 95000)
            skills = ", ".join(random.sample(skills_pool, k=random.randint(2, 4)))
            writer.writerow([role, emp, loc, salary, skills, mode])
            
    print("Clean fallback dataset with Employer tracking generated at: " + output_path)

if __name__ == "__main__":
    generate_mock_job_data()

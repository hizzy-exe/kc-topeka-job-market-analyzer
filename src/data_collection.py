import os
import random
import csv

def generate_mock_job_data():
    print("Extracting/Generating raw localized job data...")
    locations = ["Kansas City, MO", "Kansas City, KS", "Topeka, KS", "Overland Park, KS", "Olathe, KS"]
    roles = ["Data Analyst", "Business Analyst", "Software Engineer", "Python Developer", "Data Scientist", "Financial Analyst"]
    skills_pool = ["Python", "SQL", "Tableau", "Excel", "PowerBI", "R", "Java", "AWS", "Agile", "Finance"]
    work_modes = ["Remote", "On-site", "Hybrid"]
    
    # Path inside the new folder structure
    output_path = os.path.join("data", "raw", "raw_job_postings.csv")
    
    with open(output_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Job_Title", "Location", "Salary_Estimate", "Skills_Required", "Work_Mode"])
        
        for _ in range(200):
            role = random.choice(roles)
            loc = random.choice(locations)
            mode = random.choice(work_modes)
            salary = random.randint(85000, 135000) if "Scientist" in role or "Engineer" in role else random.randint(60000, 95000)
            skills = ", ".join(random.sample(skills_pool, k=random.randint(2, 4)))
            writer.writerow([role, loc, salary, skills, mode])
            
    print("Raw tracking data generated successfully at: " + output_path)

if __name__ == "__main__":
    generate_mock_job_data()

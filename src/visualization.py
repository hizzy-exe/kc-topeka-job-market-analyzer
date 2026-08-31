import os
import matplotlib.pyplot as plt
import seaborn as sns

def generate_insights_assets(salary_data, mode_data, skills_data):
    print("Rendering graphics and compiling summary briefs...")
    
    # Graph 1: Top Local Tech Skills Distribution
    plt.figure(figsize=(8, 4))
    # Assigning hue to the y-axis variable removes the warning completely!
    sns.barplot(x=list(skills_data.values()), y=list(skills_data.keys()), hue=list(skills_data.keys()), palette="viridis", legend=False)
    plt.title("Top In-Demand Skills (KC-Topeka Corridor)")

    plt.xlabel("Job Posting Count")
    plt.tight_layout()
    plt.savefig(os.path.join("output", "charts", "top_skills.png"))
    plt.close()
    
    # Compilation: Executive Performance Text Brief
    report_path = os.path.join("output", "reports", "executive_summary.txt")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("==================================================\n")
        f.write("KANSAS CITY & TOPEKA JOB MARKET ANALYSIS EXECUTIVE SUMMARY\n")
        f.write("==================================================\n\n")
        
        f.write("1. SALARY BENCHMARKS BY TECHNICAL ROLE:\n")
        for role, sal in salary_data.items():
            f.write(f"   - {role}: ${sal:,.2f}\n")
            
        f.write("\n2. WORK MODE INFRASTRUCTURE SPLIT:\n")
        for mode, pct in mode_data.items():
            f.write(f"   - {mode}: {pct*100:.1f}%\n")
            
        f.write("\n3. CORE COMPETENCY DEMAND RANKINGS:\n")
        for skill, count in skills_data.items():
            f.write(f"   - {skill}: Cited in {count} local postings\n")
            
    print("Analytics artifacts exported successfully to output directory.")

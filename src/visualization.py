import os
import matplotlib.pyplot as plt
import seaborn as sns

def generate_insights_assets(salary_data, mode_data, skills_data, employer_data):
    """
    Renders analytical visualizations and exports the structured text brief.
    """
    print("Generating graphical distribution plots and summary briefs...")
    
    plt.figure(figsize=(8, 4))
    sns.barplot(
        x=list(skills_data.values()), 
        y=list(skills_data.keys()), 
        hue=list(skills_data.keys()), 
        palette="viridis", 
        legend=False
    )
    plt.title("Top In-Demand Technical Skills (KC-Topeka Corridor)")
    plt.xlabel("Total Job Posting Volume")
    plt.ylabel("Core Technology Stack")
    plt.tight_layout()
    plt.savefig(os.path.join("output", "charts", "top_skills.png"))
    plt.close()
    
    report_path = os.path.join("output", "reports", "executive_summary.txt")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("==================================================\n")
        f.write("KANSAS CITY & TOPEKA LABOR MARKET INTEL REPORT\n")
        f.write("==================================================\n\n")
        
        f.write("1. REGIONAL SALARY TRACKING BY ARCHEFTYPE:\n")
        for role, sal in salary_data.items():
            f.write(f"   - {role}: ${sal:,.2f}\n")
            
        f.write("\n2. WORK MODE DISTRIBUTION RATIOS:\n")
        for mode, pct in mode_data.items():
            f.write(f"   - {mode}: {pct*100:.1f}%\n")
            
        f.write("\n3. CORE TECHNOLOGY COMPETENCY DEMAND:\n")
        for skill, count in skills_data.items():
            f.write(f"   - {skill}: Referenced in {count} active postings\n")
            
        f.write("\n4. TOP REGIONAL ACQUISITION ENTITIES:\n")
        for employer, count in employer_data.items():
            f.write(f"   - {employer}: {count} open market requisitions\n")
            
    print("Pipeline compilation successful. Artifacts deployed to output storage.")

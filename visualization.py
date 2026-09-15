from __future__ import annotations
from typing import Any
import matplotlib.pyplot as plt
import seaborn as sns
import config

sns.set_theme(style="whitegrid")

def generate_insights_assets(analysis: dict[str, Any]) -> None:
    print("Generating charts and executive report...")

    # Skills chart
    skills = analysis.get("top_skills") or {}
    if skills:
        plt.figure(figsize=(9, 5))
        sns.barplot(x=list(skills.values()), y=list(skills.keys()), palette="viridis")
        plt.title("Top In-Demand Skills (KC–Topeka)")
        plt.xlabel("Mentions in Job Postings")
        plt.tight_layout()
        plt.savefig(config.OUTPUT_CHARTS_DIR / "top_skills.png", dpi=150)
        plt.close()

    # Work mode pie
    modes = analysis.get("work_mode_breakdown") or {}
    if modes:
        plt.figure(figsize=(6, 6))
        plt.pie(
            [v * 100 for v in modes.values()],
            labels=list(modes.keys()),
            autopct="%1.1f%%",
            startangle=90
        )
        plt.title("Work Mode Distribution")
        plt.tight_layout()
        plt.savefig(config.OUTPUT_CHARTS_DIR / "work_mode.png", dpi=150)
        plt.close()

    # Employers chart
    employers = analysis.get("top_employers") or {}
    if employers:
        plt.figure(figsize=(9, 5))
        keys = list(employers.keys())[:10]
        vals = [employers[k] for k in keys]
        sns.barplot(x=vals, y=keys, palette="rocket")
        plt.title("Most Active Hiring Employers")
        plt.xlabel("Number of Postings")
        plt.tight_layout()
        plt.savefig(config.OUTPUT_CHARTS_DIR / "top_employers.png", dpi=150)
        plt.close()

    # Executive report
    with open(config.EXECUTIVE_SUMMARY, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("KANSAS CITY & TOPEKA LABOR MARKET INTEL REPORT\n")
        f.write("Real-time ETL Pipeline (Adzuna API)\n")
        f.write("=" * 60 + "\n\n")

        stats = analysis.get("summary_stats", {})
        f.write("0. PIPELINE SNAPSHOT\n")
        f.write(f"   Total postings     : {stats.get('total_postings', 0)}\n")
        f.write(f"   Unique titles      : {stats.get('unique_titles', 0)}\n")
        f.write(f"   Unique employers   : {stats.get('unique_employers', 0)}\n")
        f.write(f"   Unique locations   : {stats.get('unique_locations', 0)}\n\n")

        overall = analysis.get("overall_salary", {})
        if overall:
            f.write("1. SALARY OVERVIEW\n")
            f.write(f"   Mean salary       : ${overall.get('mean', 0):,.0f}\n")
            f.write(f"   Median salary     : ${overall.get('median', 0):,.0f}\n")
            f.write(f"   Postings with pay : {overall.get('count_with_salary', 0)} "
                    f"({overall.get('pct_with_salary', 0)}%)\n\n")

        f.write("2. WORK MODE DISTRIBUTION\n")
        for mode, pct in analysis.get("work_mode_breakdown", {}).items():
            f.write(f"   - {mode}: {pct*100:.1f}%\n")
        f.write("\n")

        f.write("3. TOP SKILLS\n")
        for skill, count in analysis.get("top_skills", {}).items():
            f.write(f"   - {skill}: {count} postings\n")
        f.write("\n")

        f.write("4. TOP EMPLOYERS\n")
        for emp, count in list(analysis.get("top_employers", {}).items())[:10]:
            f.write(f"   - {emp}: {count} postings\n")
        f.write("\n")

        f.write("5. LOCATION HOTSPOTS\n")
        for loc, count in list(analysis.get("location_counts", {}).items())[:10]:
            f.write(f"   - {loc}: {count} postings\n")

        f.write("\n" + "=" * 60 + "\n")

    print(f"Report saved → {config.EXECUTIVE_SUMMARY}")
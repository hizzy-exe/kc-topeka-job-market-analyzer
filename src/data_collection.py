from __future__ import annotations
import csv
import time
from pathlib import Path
from typing import Any
import requests
from tenacity import retry, stop_after_attempt, wait_exponential
import config

ADZUNA_BASE = "https://api.adzuna.com/v1/api"

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def _fetch_page(session: requests.Session, what: str, where: str, page: int) -> dict[str, Any]:
    url = f"{ADZUNA_BASE}/jobs/{config.COUNTRY}/search/{page}"
    params = {
        "app_id": config.ADZUNA_APP_ID,
        "app_key": config.ADZUNA_APP_KEY,
        "results_per_page": config.RESULTS_PER_PAGE,
        "what": what,
        "where": where,
        "content-type": "application/json",
        "sort_by": "date",
    }
    resp = session.get(url, params=params, timeout=20)
    resp.raise_for_status()
    return resp.json()

def _extract_skills(description: str) -> str:
    if not description:
        return "General Tech"
    desc = description.lower()
    found = []
    for skill in config.TARGET_SKILLS:
        if skill in desc:
            clean = skill.title().replace("Bi", "BI")
            if clean not in found:
                found.append(clean)
    return ", ".join(found[:8]) if found else "General Tech"

def _infer_work_mode(description: str, title: str) -> str:
    text = f"{title} {description}".lower()
    if any(k in text for k in ("remote", "work from home", "wfh", "fully remote")):
        return "Remote"
    if "hybrid" in text:
        return "Hybrid"
    return "On-site"

def collect_jobs() -> Path:
    if not config.ADZUNA_APP_ID or not config.ADZUNA_APP_KEY:
        raise RuntimeError(
            "Missing Adzuna credentials.\n"
            "1. Get free keys at https://developer.adzuna.com/\n"
            "2. Copy .env.example to .env\n"
            "3. Add your ADZUNA_APP_ID and ADZUNA_APP_KEY"
        )

    output_path = config.RAW_JOBS_CSV
    all_rows = []
    seen_ids = set()

    headers = [
        "job_id", "Job_Title", "Company_Employer", "Location",
        "Salary_Min", "Salary_Max", "Salary_Estimate",
        "Skills_Required", "Work_Mode", "Category",
        "Created", "Redirect_URL", "Description_Snippet", "Search_Label"
    ]

    print("Connecting to Adzuna API...")
    session = requests.Session()
    session.headers.update({"User-Agent": "kc-topeka-job-market-analyzer/1.0"})

    total = 0
    for query in config.SEARCH_QUERIES:
        what, where, label = query["what"], query["where"], query["label"]
        print(f"  → Searching '{what}' near '{where}'")

        for page in range(1, config.MAX_PAGES + 1):
            try:
                data = _fetch_page(session, what, where, page)
            except Exception as e:
                print(f"    Page {page} failed: {e}")
                break

            results = data.get("results") or []
            if not results:
                break

            for job in results:
                jid = str(job.get("id", ""))
                if not jid or jid in seen_ids:
                    continue
                seen_ids.add(jid)

                title = (job.get("title") or "Unknown").strip()
                company = (job.get("company") or {}).get("display_name") or "Hidden / Agency"
                loc_data = job.get("location") or {}
                loc = loc_data.get("display_name") or "Unknown"
                sal_min = job.get("salary_min")
                sal_max = job.get("salary_max")
                estimate = sal_max or sal_min
                desc = job.get("description") or ""
                skills = _extract_skills(desc)
                mode = _infer_work_mode(desc, title)
                category = (job.get("category") or {}).get("label") or ""
                created = job.get("created") or ""
                redirect = job.get("redirect_url") or ""

                all_rows.append([
                    jid, title, company.strip(), loc,
                    sal_min, sal_max, estimate,
                    skills, mode, category,
                    created, redirect, desc[:400], label
                ])
                total += 1

            time.sleep(1.2)  # respect rate limits
            if len(results) < config.RESULTS_PER_PAGE:
                break

    if not all_rows:
        raise RuntimeError("No job postings retrieved. Check internet connection, API keys, or try again later.")

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(all_rows)

    print(f"Successfully collected {total} unique live postings → {output_path}")
    return output_path
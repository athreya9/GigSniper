import requests
from scrapers.utils import extract_contacts, compute_score

def scrape_remoteok():
    res = requests.get("https://remoteok.com/remote-jobs.json")
    jobs = res.json()

    leads = []
    # The first item is a legal notice, so we skip it.
    for job in jobs[1:11]:
        contacts = extract_contacts(job.get("description", ""))
        lead_data = {
            "title": job["position"],
            "platform": "RemoteOK",
            "budget_type": "Unknown",
            "posted_days_ago": 0,
            "tags": job.get("tags", []),
            "link": job["url"],
            "contactEmail": contacts.get("email"),
            "contactPhone": contacts.get("phone"),
        }
        lead_data["score"] = compute_score(lead_data)
        leads.append(lead_data)
    return leads

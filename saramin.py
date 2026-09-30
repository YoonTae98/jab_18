import requests
from bs4 import BeautifulSoup


def search_saramin(keyword):

    jobs = []

    url = f"https://www.saramin.co.kr/zf_user/search/recruit?searchword={keyword}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    recruit_list = soup.select("div.item_recruit")

    for item in recruit_list:

        company_tag = item.select_one("strong.company_nm a")

        title_tag = item.select_one("h2.job_tit a")

        location_tag = item.select_one("div.job_condition span")

        if not company_tag or not title_tag:
            continue

        company = company_tag.get_text(strip=True)

        title = title_tag.get_text(strip=True)

        if location_tag:
            location = location_tag.get_text(" ", strip=True)
        else:
            location = ""

        link = title_tag.get("href")

        if link and link.startswith("/"):
            link = "https://www.saramin.co.kr" + link

        job_data = {
            "site": "사람인",
            "company": company,
            "title": title,
            "location": location,
            "link": link
        }

        jobs.append(job_data)

    return jobs
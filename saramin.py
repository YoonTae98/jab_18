import requests
from bs4 import BeautifulSoup
from urllib.parse import quote


def search_saramin(keyword):

    jobs = []

    keyword = quote(keyword)

    url = (
        "https://www.saramin.co.kr/zf_user/search/recruit"
        f"?searchType=search"
        f"&searchword={keyword}"
        f"&search_done=y"
        f"&search_optional_item=n"
        f"&recruitPage=1"
        f"&recruitSort=relation"
        f"&recruitPageCount=30"
    )

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/154.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers)

    print("사람인 상태코드:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")

    recruit_list = soup.select("div.item_recruit")

    print("사람인 검색 결과:", len(recruit_list))

    for item in recruit_list:

        # 회사
        company_tag = item.select_one("strong.corp_name")

        # 제목
        title_tag = item.select_one("h2.job_tit a")

        # 지역
        location_tag = item.select_one(".job_condition")

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

    print("사람인 최종 결과:", len(jobs))

    return jobs
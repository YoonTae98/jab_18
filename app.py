from flask import Flask, render_template, request, send_file
from scrapper import search_incruit
from saramin import search_saramin
from file import save_to_csv

app = Flask(__name__)

@app.route("/")
def hello_world():

    return render_template("index.html")

@app.route("/search")

def search():

    keyword = request.args.get("keyword")
    site = request.args.get("site")

    jobs = []

    # 전체 검색
    if site == "all":

        incruit_jobs = search_incruit(keyword)
        saramin_jobs = search_saramin(keyword)

        jobs = incruit_jobs + saramin_jobs

    # 인크루트만 검색
    elif site == "incruit":

        jobs = search_incruit(keyword)

    # 사람인만 검색
    elif site == "saramin":

        jobs = search_saramin(keyword)

    print("검색 사이트:", site)
    print("검색 결과 개수:", len(jobs))

    return render_template(
        "search.html",
        keyword=keyword,
        site=site,
        jobs=jobs
    )

@app.route("/file")
def file():

    keyword = request.args.get("keyword")
    site = request.args.get("site")

    jobs = []

    # 전체
    if site == "all":

        incruit_jobs = search_incruit(keyword)
        saramin_jobs = search_saramin(keyword)

        jobs = incruit_jobs + saramin_jobs

    # 인크루트
    elif site == "incruit":

        jobs = search_incruit(keyword)

    # 사람인
    elif site == "saramin":

        jobs = search_saramin(keyword)

    save_to_csv(jobs)

    return send_file(
        "downloads.csv",
        as_attachment=True
    )

if __name__ == "__main__":

    app.run(debug=True)
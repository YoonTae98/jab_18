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

    # 인크루트 검색
    incruit_jobs = search_incruit(keyword)

    # 사람인 검색
    saramin_jobs = search_saramin(keyword)

    # 두 사이트 결과 합치기
    jobs = incruit_jobs + saramin_jobs

    return render_template(
        "search.html",
        keyword=keyword,
        jobs=enumerate(jobs)
    )


@app.route("/file")
def file():

    keyword = request.args.get("keyword")

    # 인크루트
    incruit_jobs = search_incruit(keyword)

    # 사람인
    saramin_jobs = search_saramin(keyword)

    # 두 사이트 결과 합치기
    jobs = incruit_jobs + saramin_jobs

    save_to_csv(jobs)

    return send_file(
        "downloads.csv",
        as_attachment=True
    )


if __name__ == "__main__":

    app.run(debug=True)
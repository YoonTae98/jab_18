import csv


def save_to_csv(jobs):

    with open(
        "downloads.csv",
        "w",
        encoding="cp949",
        newline=""
    ) as file:

        csv_writer = csv.writer(file)

        csv_writer.writerow([
            "No",
            "사이트",
            "회사",
            "제목",
            "지역",
            "상세보기"
        ])

        for index, job in enumerate(jobs):

            csv_writer.writerow([
                index + 1,
                job["site"],
                job["company"],
                job["title"],
                job["location"],
                job["link"]
            ])
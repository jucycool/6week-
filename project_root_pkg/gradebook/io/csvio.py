import csv

from ..models import Student


def load_students_from_csv(filename):
    students = []

    with open(filename, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row["name"]
            score_text = row["scores"].strip()

            if score_text:
                scores = [
                    float(score.strip())
                    for score in score_text.split(";")
                ]
            else:
                scores = []

            students.append(Student(name, scores))

    return students

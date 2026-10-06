from pathlib import Path

from .models import Student, GradeBook
from .io.csvio import load_students_from_csv


def run_cli():
    print("=== 성적 계산 프로그램 ===")

    # students.csv는 project_root_pkg 폴더에 있습니다.
    csv_path = Path(__file__).resolve().parent.parent / "students.csv"

    try:
        students = load_students_from_csv(csv_path)
        print("students.csv 파일을 읽었습니다.")
    except FileNotFoundError:
        print("students.csv를 찾지 못해 예시 데이터를 사용합니다.")
        students = [
            Student("Alice", [90, 85, 92]),
            Student("Bob", [70, 75, 68]),
        ]

    grade_book = GradeBook()

    for student in students:
        grade_book.add_student(student)

    print(f"\n전체 반 평균 점수: {grade_book.class_average():.2f}")

    for student in grade_book.students:
        print(
            f"{student.name} - "
            f"평균: {student.average():.1f}, "
            f"학점: {student.grade()}"
        )

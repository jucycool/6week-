from models import Student, GradeBook


def main():
    alice = Student("Alice", [90, 85, 92])
    bob = Student("Bob", [78, 82, 80])

    grade_book = GradeBook()
    grade_book.add_student(alice)
    grade_book.add_student(bob)

    print(f"{alice.name} - 평균: {alice.average():.1f}, 등급: {alice.grade()}")
    print(f"{bob.name} - 평균: {bob.average():.1f}, 등급: {bob.grade()}")

    print(f"\n전체 학생 평균: {grade_book.average():.1f}")


if __name__ == "__main__":
    main()

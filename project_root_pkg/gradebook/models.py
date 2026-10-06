from .utils import mean, letter_grade


class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        return mean(self.scores)

    def grade(self):
        return letter_grade(self.average())


class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def class_average(self):
        if len(self.students) == 0:
            return 0

        total = sum(student.average() for student in self.students)
        return total / len(self.students)

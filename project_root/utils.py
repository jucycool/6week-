# 평균 점수를 계산합니다.
def mean(scores):
    if not scores:
        return 0

    return sum(scores) / len(scores)


# 점수에 따라 학점을 정합니다.
def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

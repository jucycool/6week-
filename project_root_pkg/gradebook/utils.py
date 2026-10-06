def mean(scores):
    """점수 목록의 평균을 계산합니다."""
    if len(scores) == 0:
        return 0

    return sum(scores) / len(scores)


def letter_grade(score):
    """평균 점수에 따라 학점을 반환합니다."""
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

"""Solutions for function decomposition practice."""

def average(numbers):
    return sum(numbers) / len(numbers)


def passed(score, threshold=60):
    return score >= threshold


def summarize(scores):
    passed_count = 0
    for score in scores:
        if passed(score):
            passed_count += 1
    return {"average": average(scores), "passed_count": passed_count}


scores = [72, 55, 91]
print(summarize(scores))
def winner(names: list[str], scores: list[float]) -> str:
    if not names:
        return ""
    best = 0
    for i in range(1, len(scores)):
        if scores[i] > scores[best]:
            best = i
    return names[best]


def average(scores: list[float]) -> float:
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores), 2)


def ranking(names: list[str], scores: list[float]) -> list[str]:
    order = sorted(range(len(names)), key=lambda i: -scores[i])
    return [names[i] for i in order]


def above_average(names: list[str], scores: list[float]) -> list[str]:
    avg = average(scores)
    return [names[i] for i in range(len(names)) if scores[i] > avg]

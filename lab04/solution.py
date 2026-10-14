def winner(names: list[str], scores: list[float]):
    for i in range(len(names)):
        if max(scores) == scores[i]:
            return names[i]
def average(scores: list[float]):
    ave = 0
    if scores == []:
        return 0.0
    else:
        for i in scores:
            ave += i
        return round(ave / len(scores), 2)
def ranking(names: list[str], scores: list[float]):
    lst = []
    
    for i in range(len(names)):
        if scores[i] == max(scores):
            lst.append(names[i])
    while len(lst) != len(names):
        mid = min(scores)
        save = None
        for i in range(len(names)):
            if max(scores) > scores[i] > mid:
                mid = scores[i]
                save = i
            elif scores[i] == min(scores):
                save = i
                mid = 
        lst.append(names[save])
    return lst
def above_average(names: list[str], scores: list[float]):
    ave = 0
    lst = []
    if scores == []:
        return 0.0
    else:
        for i in scores:
            ave += i
        ave = round(ave / len(scores), 2)
        for i in range(len(names)):
            if scores[i] > ave:
                lst.append(names[i])
        return lst
print(ranking(["Аня", "Боря", "Вика"], [7.0, 9.0, 8.0]))

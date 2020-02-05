def retire(age, salary, pct_saved, goal):
    total = 0
    while total*1.35 < goal:
        total += salary*pct_saved
        age += 1

    if age > 100.0:
        return -1

    else:
        return age



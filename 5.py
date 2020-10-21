def task(taskrange, startnumber=10):
    multiplier = 1
    results = []
    while len(results) < 1:
        if all([(startnumber * multiplier) % n == 0 for n in range(1, taskrange)]):
            return(startnumber * multiplier)
        else:
            multiplier += 1


if __name__ == '__main__':
    div_by_10_first = task(10)
    div_by_20_first = task(20, task(10))
    print('result:', div_by_20_first)

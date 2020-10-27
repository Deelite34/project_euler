

class SmallestDivisibleNumber():
    """
    2520 is the smallest number that can be divided by each
    of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by
     all of the numbers from 1 to 20?
    """

    def calculate(self, taskrange, startnumber=10):
        multiplier = 1
        results = []
        while len(results) < 1:
            # check if all elements of list containing bools , that tell us
            # if startnumber * multiplier is divisible
            # by numbers from 1 to taskrange, are True
            if all([(startnumber * multiplier) % n == 0 for n in range(1, taskrange)]):
                return(startnumber * multiplier)
            else:
                multiplier += 1


if __name__ == '__main__':
    task = SmallestDivisibleNumber()
    div_by_10_first = task.calculate(10)
    div_by_20_first = task.calculate(20, div_by_10_first)
    print('result:', div_by_20_first)

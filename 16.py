class PowerDigitSum():
    """
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?
    """

    def calculate(self, input):
        number = str(2**input)
        string = [int(i) for i in number]
        sum_numbers = sum(string)
        return(sum_numbers)


if __name__ == '__main__':
    # Task takes about 50s to calculate
    task = PowerDigitSum()
    print(task.calculate(1000))

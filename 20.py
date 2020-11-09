class FactorialDigitSum():
    """
    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is
    3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
    """

    def factorial(self, input):
        result = 1
        for i in range(1, input + 1):
            result *= i
        return(result)

    def sum_of_digits(self, input):
        helper = str(input)
        result = 0
        for i in helper:
            result += int(i)
        return(result)


if __name__ == '__main__':
    task = FactorialDigitSum()
    factorial_100 = task.factorial(100)
    print(task.sum_of_digits(factorial_100))

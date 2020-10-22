"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is
3025 - 385 = 2640

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
"""


class difference():
    def sum_of_squares(self, task_range):
        return(sum([i**2 for i in range(task_range + 1)]))

    def square_of_sum(self, task_range):
        return(sum(i for i in range(task_range + 1))**2)

    def calculate_result(self, task_range):
        return(self.square_of_sum(task_range) - self.sum_of_squares(task_range))


if __name__ == '__main__':
    task = difference()
    print('result:', task.calculate_result(100))

from math import sqrt

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

class SpecialPythagoreantriplet():
    def calculate(self):
        for i in range(500):
            for y in range(i, 500):
                if all(
                    [i + y + sqrt(i ** 2 + y ** 2) == 1000,  # a + b + c = 1000
                     sqrt(i ** 2 + y ** 2) > y,              # c > b
                     y > i,                                 # b > a
                     i**2 + y**2 == i**2 + y**2]
                ):
                    print(f'a^2 + b^2 = c^2 : {i**2} + {y**2} == {i**2 + y**2}')
                    print(f'a   * b   * c = {i * y * int(sqrt(i ** 2 + y ** 2))}')
                    print(f'a   + b   + c = {i + y + int(sqrt(i ** 2 + y ** 2))}')
                    return(f'numbers are: {i}, {y}, {int(sqrt(i ** 2 + y ** 2))}')


if __name__ == '__main__':
    task = SpecialPythagoreantriplet()
    print('result:', task.calculate())

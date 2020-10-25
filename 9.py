from math import sqrt


def task():
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


print(task())

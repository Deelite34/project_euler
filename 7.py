from math import sqrt
from math import ceil


def is_prime(num):
    divisors = []
    if num % 2 == 0:
        return False
    for i in range(1, ceil(sqrt(num)) + 1 if num > 3 else num, 2):
        if num % i == 0:
            divisors.append(i)
    divisors.append(num)
    if len(divisors) == 2:
        return(True)
    return(False)


def find_x_primes_range(start, end):
    result = []
    for i in range(start, end):
        if is_prime(i):
            result.append(i)
    return(result)


def find_primes_up_to_input(number):
    result = [2]
    start_index = 1
    end_index = 500
    while len(result) < number:
        result += find_x_primes_range(start_index, end_index)
        start_index += 500
        end_index += 500
    return(result)


index = 10000
# print((find_primes_up_to_input(index)))
print((find_primes_up_to_input(index)[10000]))

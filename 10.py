from math import sqrt
from math import ceil


def is_prime(num):
    divisors = []
    if num % 2 == 0:
        return(False)
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


def sum_primes_up_to_input():
    result = [2]
    start_index = 1
    end_index = 5000
    while result[-1] < 2000000:
        result += find_x_primes_range(start_index, end_index)
        start_index += 5000
        end_index += 5000

    for i in reversed(result):  # Removes excesive elements from result list
        if i > 2000000:
            result.remove(i)
        else:
            break
    return(sum(result))


# It took 31.9s to compute everything on my PC, be patient
print(sum_primes_up_to_input())

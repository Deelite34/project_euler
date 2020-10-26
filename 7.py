def is_prime(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    if len(divisors) == 2 and 1 in divisors and i in divisors:
        return(True)
    return(False)


def find_x_primes_range(start, end):
    result = []
    for i in range(start, end):
        if is_prime(i):
            result.append(i)
    return(result)


def find_xth_prime(number):
    result = []
    start_index = 1
    end_index = 1000
    while len(result) < number:
        result += find_x_primes_range(start_index, end_index)
        start_index += 1000
        end_index += 1000
    return(result)


index = 1000

print(find_xth_prime(index))
print(find_xth_prime(index)[100])
print(len(find_xth_prime(index)))

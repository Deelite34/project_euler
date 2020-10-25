def is_prime(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    if len(divisors) == 2 and 1 in divisors and i in divisors:
        return(True)
    return(False)

def find_x_primes(index):
    result = []
    for i in range(index):
        if is_prime(i):
            result.append(i)
    return(result)

print(find_x_primes(10))

helper = 10000
while True:

    if len(find_x_primes(10000)) < 10000:
        print("Retrying...")
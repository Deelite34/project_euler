from math import sqrt
from math import ceil


class Prime10001st():
    """
    By listing the first six prime numbers:
    2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?
    """
    def is_prime(self, num):
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

    def find_x_primes_range(self, start, end):
        result = []
        for i in range(start, end):
            if self.is_prime(i):
                result.append(i)
        return(result)

    def find_primes_up_to_input(self, number):
        result = [2]
        start_index = 1
        end_index = 500
        while len(result) < number:
            result += self.find_x_primes_range(start_index, end_index)
            start_index += 500
            end_index += 500
        return(result)


if __name__ == '__main__':
    index = 10000
    task = Prime10001st()
    # print((find_primes_up_to_input(index))) # full list
    print('result:', task.find_primes_up_to_input(index)[10000])

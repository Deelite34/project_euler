from math import sqrt
from math import ceil

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


class SummationOfPrimes():
    def is_prime(self, num):
        divisors = []
        if num % 2 == 0:
            return(False)
        # check only neccesary divisors to speed up calculations
        # up to square root of number+1 (when possible)
        for i in range(1, ceil(sqrt(num)) + 1 if num > 3 else num, 2):
            print(i)
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

    def sum_primes_up_to_input(self, input):
        result = [2]
        start_index = 1
        end_index = 5000
        while result[-1] < 2000000:
            result += self.find_x_primes_range(start_index, end_index)
            start_index += 5000
            end_index += 5000
        for i in reversed(result): # Remove excesive elements from result list
            if i > input:
                result.remove(i)
            else:
                break
        return(sum(result))


# It took 31.9s to compute everything on my PC, be patient
if __name__ == '__main__':
    task = SummationOfPrimes()
    print('result:', task.sum_primes_up_to_input(2000000))

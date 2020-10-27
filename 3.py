import unittest


class LargestPrimeFactors(unittest.TestCase):
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    
    Implements algorithm from:
    https://people.revoledu.com/kardi/tutorial/BasicMath/Prime/Algorithm-PrimeFactor.html#:~:text=Algorithm%20for%20Prime%20Factorization&text=The%20simplest%20algorithm%20to%20find,until%20the%20number%20becomes%201.&text=Thus%20100%20divided%20by%202%20become%2050.
    """

    def calculate(self, input):
        N = input
        p = 2
        result = []
        while (N >= p**2):
            if N % p == 0:
                result.append(p)
                N = N / p
            else:
                p = p + 1
        result.append(int(N))
        return(result)        # list with all prime factors

    def test_calculate(self):  # uses only the largest prime factor from result
        self.assertEqual(self.calculate(13195)[-1], 29)


if __name__ == '__main__':
    unittest.main(exit=False)
    largest_p_factor = LargestPrimeFactors()
    print(largest_p_factor.calculate(600851475143)[-1])  # last element

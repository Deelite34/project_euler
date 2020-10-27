import unittest


class Multiples(unittest.TestCase):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    """

    def multiples_3_and_5(self, number):
        sum = 0
        for i in range(number):
            if i % 3 == 0 or i % 5 == 0:
                sum += i
        return(sum)

    def test_multiples(self):
        self.assertEqual(self.multiples_3_and_5(10), 23)


if __name__ == '__main__':
    unittest.main(exit=False)
    result = Multiples()
    print('\nSum of multiples of 3 and 5 up to 1000 is: ' +
         f'{result.multiples_3_and_5(1000)}')

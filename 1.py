import unittest


class Multiples(unittest.TestCase):

    def multiples_3_and_5(self, number):
        sum = 0
        for i in range(number):
            if i % 3 == 0 or i % 5 == 0:
                sum += i
        return(sum)

    def test_multiples(self):
        self.assertEqual(self.multiples_3_and_5(10), 23)


if unittest.main(exit=False):
    print('Function test completed successfuly')

result = Multiples()
print('\nSum of multiples of 3 and 5 up to 1000 is: ' +
     f'{result.multiples_3_and_5(1000)}')

import unittest
"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


class CheckPalindrome(unittest.TestCase):

    def __check_palindrome(self, input):
        helper = str(input)
        if len(helper) % 2 == 0:
            length = len(str(input))
            mid_number = int(length / 2)
            if helper[:mid_number] == helper[:mid_number - 1:-1]:
                return(True)

    def find_palindrome(self, number):
        result = []
        for x in range(number, 0, -1):
            for y in range(number, 0, -1):
                number = x * y
                if self.__check_palindrome(number):
                    result.append(number)
        return('Biggest found palindrome: ' + str(sorted(result)[-1]))

    def test_check_palindrome(self):
        self.assertTrue(
            self.__check_palindrome(12344321)
        )

    def test_find_palindrome(self):
        self.assertEqual(
            self.find_palindrome(99),
            'Biggest found palindrome: 9009'
        )


if __name__ == '__main__':
    unittest.main(exit=False)
    task = CheckPalindrome()
    print(task.find_palindrome(999))

class NumberLetterCounts():
    def __init__(self):
        self.num_to_words = {
            0: '',
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            14: 'fourteen',
            15: 'fifteen',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen',
            20: 'twenty',
            30: 'thirty',
            40: 'forty',
            50: 'fifty',
            60: 'sixty',
            70: 'seventy',
            80: 'eighty',
            90: 'ninety'}
        self.result = ''

    def convert_num_to_word(self, input):
        self.result = ''
        if input < 100 and input in self.num_to_words.keys():
            self.result = self.num_to_words[input]
            return(self.result)
        elif input < 100 and input not in self.num_to_words.keys():
            # if we have integer 34, this will append a word
            # equivalent to 0-th element of '34' string + '0' string
            # which is '3' + '0' that gives us '30' string.
            # After that we convert it to integer type
            # and we find a word equivalent to that nunber in the dictionary
            # which is 'thirty'
            self.result += self.num_to_words[int(str(input)[0] + '0')] + ' '

            # does the same, but for the 1-st element of '34' string, that is '4' string
            self.result += self.num_to_words[int(str(input)[1])]
            return(self.result)
        elif input < 1000:
            # counting from 0:
            # <0-th number> hundred
            self.result += self.num_to_words[int(str(input)[0])] + ' hundred'

            
            second_and_third = int(str(input)[1:3])
            # If 1st and 2nd numbers are not 0 and 0, go here
            if second_and_third in self.num_to_words.keys() and second_and_third != 0:
                # converts number on 1st and 2nd(counting from 0)
                # position to string and returns result
                self.result += ' and ' + self.num_to_words[int(str(input)[1:3])]
                return(self.result)

            # if 1st number is not 0
            if(int(str(input)[1]) != 0):
                # adds 1nd number to result, 2 would  be 'twenty '
                self.result += ' and ' + self.num_to_words[int(str(input)[1] + '0')] + ' '

            # adds 2nd number to result. With 321 it would be 'one'
            self.result += self.num_to_words[int(str(input)[2])]

            # This will ensure there are no excess whitespaces
            return(' '.join(self.result.split()))
        elif input == 1000:
            self.result = 'one thousand'
            return(self.result)

    def count_letters(self, input):
        self.result = ''
        length_word = len(''.join(self.convert_num_to_word(input).split(' ')))
        return(length_word)

    def count_letters_range(self, input_range):
        length = 0
        for i in range(1, input_range + 1):
            length += self.count_letters(i)
        return(length)


if __name__ == '__main__':
    task = NumberLetterCounts()
    print(task.count_letters_range(1000))

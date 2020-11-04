class LongestCollatzSequence():
    """
    The following iterative sequence is defined for the set of positive integers:
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)
    Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
    Although it has not been proved yet (Collatz Problem),
    it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?
    NOTE: Once the chain starts the terms are allowed to go above one million.
    """

    def create_chain(self, input):
        chain = [input]
        current_number = input
        while current_number != 1:
            if current_number % 2 == 0:
                current_number = int(current_number / 2)
                chain.append(current_number)
            else:
                current_number = int(3 * current_number + 1)
                chain.append(current_number)
        return(chain)

    def find_longest_chain(self):
        number = 2
        length = 0
        for i in range(2, 1000000):
            print('checking', i)
            found_chain = self.create_chain(i)
            if len(found_chain) > length:
                number = found_chain[0]
                length = len(found_chain)
        return(f'Longest found chain starting with {number},\
                 with length {length}')


if __name__ == '__main__':
    # Task takes about 50s to calculate
    task = LongestCollatzSequence()
    print(task.find_longest_chain())

class CountingSundays():
    """
    You are given the following information, but you may prefer
    to do some research for yourself.

        1 Jan 1900 was a Monday.
        Thirty days has September,
        April, June and November.
        All the rest have thirty-one,
        Saving February alone,
        Which has twenty-eight, rain or shine.
        And on leap years, twenty-nine.
        A leap year occurs on any year evenly divisible by 4, but not on a century
        unless it is divisible by 400.

    How many Sundays fell on the first of the month during the twentieth century
    (1 Jan 1901 to 31 Dec 2000)?
    """

    def __init__(self):
        self.months_len = {
            'January': 31,
            'February': 28,
            'March': 31,
            'April': 30,
            'May': 31,
            'June': 30,
            'July': 31,
            'August': 31,
            'September': 30,
            'October': 31,
            'November': 30,
            'December': 31
        }
        self.months_names = [i for i in self.months_len.keys()]
        self.day_names = ['Monday', 'Tuesday', 'Wednesday',
                          'Thursday', 'Friday', 'Saturday', 'Sunday']

        self.cur_year = 1901       # starting date
        self.cur_month = 'January'
        self.cur_day = 1
        self.leap_year = False

        # index of day name in day_names for this month(first day of the month)
        # Set this mannualy for custom dates
        self.first_day_name_index = 1
        # index of day name in day_names for next month(first day of next month)
        # Set this mannualy for custom dates
        self.next_first_day_name_index = (self.first_day_name_index +
                                          self.months_len[self.cur_month]) % 7

    def give_day(self):
        cur_day_name = self.day_names[((self.cur_day +
                                        self.first_day_name_index) % 7) - 1]
        return(cur_day_name)

    def give_date(self):
        # DD.MM.YYYY format
        return(f'{self.cur_day}.' +
               f'{self.months_names.index(self.cur_month)+1}.' +
               f'{self.cur_year}')

    def next_day(self):
        #print('nastepny dzien')
        if self.cur_day + 1 > self.months_len[self.cur_month]:
            # Go to 29th of february instead of going to next_month()
            if self.cur_month == 'February' and self.cur_day == 28 and\
                    self.leap_year is True:
                self.cur_day += 1
                self.leap_year = False
                return()
            self.next_month()
            return()
        self.cur_day += 1

    def next_year(self):
        """Increases year counter and checks if this is leap year"""
        self.cur_year += 1
        self.leap_year = False
        if self.cur_year % 4 == 0:
            if self.cur_year % 400 == 0:
                self.leap_year = True
                return()
            elif self.cur_year % 100 == 0:
                return()
            self.leap_year = True

    def next_month(self):
        """
        checks for leap year, goes to january,
        and calculates first day name of this and next month
        """
        if self.cur_month == 'December':
            self.next_year()
            self.cur_month = 'January'
            self.first_day_name_index = self.next_first_day_name_index
            self.next_first_day_name_index =\
                (self.first_day_name_index +
                 self.months_len[self.cur_month]) % 7
        else:
            # go to next month
            self.cur_month = self.months_names[
                                    self.months_names.index(self.cur_month) + 1
                                    ]
            self.first_day_name_index = self.next_first_day_name_index

            helper = self.months_len[self.cur_month]
            # Ensure correct day is used after 29th february in leap year
            if self.cur_month == 'February' and self.leap_year is True:
                helper = self.months_len[self.cur_month] + 1

            self.next_first_day_name_index =\
                (self.first_day_name_index + helper) % 7

        self.cur_day = 1

    def calculate_sundays(self):
        counter = 0
        current_date = f'{task.give_date()}'

        while current_date != '31.12.2000':
            current_date = f'{task.give_date()}'
            if self.cur_day == 1 and self.first_day_name_index == 6:
                print(current_date)
                counter += 1
            self.next_day()
        return(counter)


if __name__ == '__main__':
    task = CountingSundays()
    print(f'{task.calculate_sundays()} sundays fell on',
          'the first of the month from 01.01.1901 until 31.12.2000')

import category
import math


class Transaction:

    def __init__(self, date, description, amount, source, cate=category.Category.Other, recurring=False,
                 recurring_date_start='', recurring_date_end=''):
        self.date = date
        self.description = description
        self.amount = amount
        self.source = source
        self.category = cate
        self.recurring = recurring
        if recurring:
            self.recurring_date_start = recurring_date_start
            self.recurring_date_end = recurring_date_end

    def to_list(self):
        return [self.date.strftime("%m/%d/%Y"), self.description, self.find_super_category(), str(self.category.name),
                str(self.amount), self.source]

    def find_super_category(self):
        val = math.floor(self.category.value / 10)
        if val == 1:
            return 'Living'
        elif val == 2:
            return 'Subscription'
        elif val == 3:
            return 'Food'
        elif val == 4:
            return 'Daily'
        elif val == 5:
            return 'Entertainment'
        elif val == 6:
            return 'Transportation'
        elif val == 7:
            return 'Travel'
        elif val == 8:
            return 'Medicare'
        elif val == 9:
            return 'Social'
        elif val == 10:
            return 'Pet'
        elif val == 11:
            return 'Other'

    def to_string(self):
        return ", ".join(self.to_list())

import category
import math


class Transaction:

    def __init__(self, date, description, amount, source, cate=category.Category.其他, recurring=False,
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
            return '住房'
        elif val == 2:
            return 'subscription'
        elif val == 3:
            return '饮食'
        elif val == 4:
            return '生活用品'
        elif val == 5:
            return '文娱'
        elif val == 6:
            return '日常出行'
        elif val == 7:
            return '旅行'
        elif val == 8:
            return '医疗'
        elif val == 9:
            return 'social'
        elif val == 10:
            return '宠物'
        elif val == 11:
            return '其他'

    def to_string(self):
        return ", ".join(self.to_list())

import data_parser
import transaction
import category
from datetime import datetime


class ChaseDataParser(data_parser.DataParser):
    def parse(self):
        for row in self.data:
            amount = float(row[5]) * -1
            if amount < 0:
                continue
            date = datetime.strptime(row[0], '%m/%d/%Y')
            description = row[2]
            category_from_bank = row[3]
            if category_from_bank.lower() == "supermarkets":
                cate = category.Category.Grocery
            else:
                cate = category.Category.其他
            self.transactions.append(transaction.Transaction(date, description, amount, self.data_source, cate=cate))

import data_parser
import transaction
import category
from datetime import datetime


class DiscoverDataParser(data_parser.DataParser):
    def parse(self):
        for row in self.data:
            amount = float(row[3])
            if amount < 0:
                continue
            date = datetime.strptime(row[0], '%m/%d/%Y')
            description = row[2]
            category_from_bank = row[4]
            if category_from_bank.lower() == "supermarkets":
                cate = category.Category.Grocery
            else:
                cate = category.Category.其他
            self.transactions.append(transaction.Transaction(date, description, amount, self.data_source, cate=cate))

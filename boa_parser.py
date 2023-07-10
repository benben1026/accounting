import data_parser
import transaction
from datetime import datetime

class BoaDataParser(data_parser.DataParser):
    def parse(self):
        for row in self.data:
            amount = float(row[4]) * -1
            if amount < 0:
                continue
            date = datetime.strptime(row[0], '%m/%d/%Y')
            description = row[2]
            self.transactions.append(transaction.Transaction(date, description, amount, self.data_source))

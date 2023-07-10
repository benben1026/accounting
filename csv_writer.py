import csv

class CsvWriter:
    def __init__(self, file_name):
        self.file_name = file_name

    def write(self, transactions):
        with open(self.file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Date', 'Description', 'Category', 'Subcategory', 'Amount', 'Paid By'])
            for transaction in transactions:
                writer.writerow(transaction.to_list())
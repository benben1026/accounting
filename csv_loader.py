import csv

class CsvLoader:

    def __init__(self, file_name):
        self.file_name = file_name
        self.schema = []
        self.data = []

    def read(self):
        with open(self.file_name) as csv_file:
            csv_reader = csv.reader(csv_file)
            first_line = True
            for row in csv_reader:
                if first_line:
                    self.schema = row
                    first_line = False
                else:
                    self.data.append(row)


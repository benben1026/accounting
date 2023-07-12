import csv
import category

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

    def read_category_helper(self):
        category_dict = {}
        with open(self.file_name, encoding='utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                cate = category.Category[row[0]]

                for keyword in row[1:]:
                    keyword = keyword.lower()
                    if keyword == '':
                        continue
                    if keyword in category_dict:
                        raise Exception("duplicate keyword detected: " + keyword)
                    else:
                        category_dict[keyword] = cate
        return category_dict

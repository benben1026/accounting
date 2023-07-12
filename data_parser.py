import category


class DataParser:
    def __init__(self, data, data_source, category_dict):
        self.data = data
        self.data_source = data_source
        self.transactions = []
        if category_dict is not None:
            self.category_dict = category_dict
        else:
            self.category_dict = {}

    def parse(self):
        pass

    def guess_category(self, description):
        return category.guess_category_based_on_keyword(self.category_dict, description)

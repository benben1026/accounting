# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import re

import csv_loader
import csv_writer
import chase_parser
import boa_parser
import discover_parser

resource_dir = "./resources"
output_dir = "./output"


def process_file_name(name):
    splits = re.split('\.', name)
    if len(splits) != 2 or splits[1].lower() != 'csv':
        return []
    tokens = re.split('_', splits[0])
    if len(tokens) == 3:
        return tokens
    else:
        return []

def process_and_output_transactions(transactions):
    transactions.sort(key=lambda x: x.date)
    writer = csv_writer.CsvWriter(output_dir + "/testoutput.csv")
    writer.write(transactions)


if __name__ == '__main__':
    file_list = os.listdir(resource_dir)
    print(file_list)

    all_transactions = []

    for file_name in file_list:
        processed_file_name = process_file_name(file_name)
        if len(processed_file_name) == 0:
            continue
        loader = csv_loader.CsvLoader(resource_dir + "/" + file_name)
        loader.read()
        if processed_file_name[0].lower() == 'boa':
            parser = boa_parser.BoaDataParser(loader.data, processed_file_name[2])
        elif processed_file_name[0].lower() == 'discover':
            parser = discover_parser.DiscoverDataParser(loader.data, processed_file_name[2])
        elif processed_file_name[0].lower() == 'chase':
            parser = chase_parser.ChaseDataParser(loader.data, processed_file_name[2])
        else:
            continue
        parser.parse()
        all_transactions += parser.transactions

    process_and_output_transactions(all_transactions)

    for t in all_transactions:
        print(t.to_string())
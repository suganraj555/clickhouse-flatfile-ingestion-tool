import csv

class FlatFileHandler:
    def __init__(self, file_path, delimiter=','):
        self.file_path = file_path
        self.delimiter = delimiter

    def get_columns(self):
        with open(self.file_path, 'r', newline='') as file:
            reader = csv.reader(file, delimiter=self.delimiter)
            return next(reader)

    def read_data(self, selected_columns):
        with open(self.file_path, 'r', newline='') as file:
            reader = csv.DictReader(file, delimiter=self.delimiter)
            return [[row[col] for col in selected_columns] for row in reader]

    def write_data(self, columns, data):
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=self.delimiter)
            writer.writerow(columns)
            writer.writerows(data)

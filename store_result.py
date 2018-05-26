import csv


class StoreResult(object):

    def __init__(self, file_name):
        self.store_file = file_name

    def write_to_csv(self,  data_list):
        with open(self.store_file, "w", encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data_list)

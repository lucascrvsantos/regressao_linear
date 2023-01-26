import csv

class Values:
    def __init__(self, path):
        self.file = path
        self.x, self.y = [], []

    def obter_valores(self):
        with open(self.file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.x.append(row['x'])
                self.y.append(row['y'])
        return self.x, self.y
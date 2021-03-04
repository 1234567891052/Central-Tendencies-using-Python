import csv
from collections import Counter

with open('data.csv', newline='') as data:
    reader = csv.reader(data)
    read_data = list(reader)

read_data.pop(0)
weights = []

for i in range(len(read_data)):
    weight = read_data[0][2]
    weights.append(float(weight))


class centralTendencies():
    def __init__(self, arr):
        self.arr = arr
        self.arr_len = len(self.arr)
        self.arr_sum = sum(self.arr)

    def Mean(self):
        mean = self.arr_sum / self.arr_len
        print('Mean: ' + str(mean))

    def Median(self):
        if self.arr_len % 2 != 0:
            median = self.arr[int(self.arr_len - 1) / 2]
        else:
            median = (self.arr[(int(self.arr_len - 1) // 2) - 1] +
                      self.arr[int(self.arr_len - 1) // 2]) / 2

        print('Median: ' + str(median))

    def Mode(self):
        d = Counter(self.arr)

        weightsDict = {
            '75-85': 0,
            '85-95': 0,
            '95-105': 0,
            '105-115': 0,
            '115-125': 0,
            '125-135': 0,
            '135-145': 0,
            '155-165': 0,
            '165-175': 0
        }

        for w, occurence in d.items():
            if 75 < float(w) < 85:
                weightsDict['75-85'] += occurence
            elif 85 < float(w) < 95:
                weightsDict['85-95'] += occurence
            elif 95 < float(w) < 105:
                weightsDict['95-105'] += occurence
            elif 105 < float(w) < 115:
                weightsDict['105-115'] += occurence
            elif 115 < float(w) < 125:
                weightsDict['115-125'] += occurence
            elif 125 < float(w) < 135:
                weightsDict['125-135'] += occurence
            elif 135 < float(w) < 145:
                weightsDict['135-145'] += occurence
            elif 145 < float(w) < 155:
                weightsDict['145-155'] += occurence
            elif 155 < float(w) < 165:
                weightsDict['155-165'] += occurence
            elif 165 < float(w) < 175:
                weightsDict['165-175'] += occurence

        mode_range, mode_occurence = 0, 0

        for ran, occurence in weightsDict.items():
            if occurence > mode_occurence:
                mode_range, mode_occurence = [
                    int(ran.split('-')[0]), int(ran.split('-')[1])], occurence

        mode = float((mode_range[0] + mode_range[1]) / 2)
        print(f"Mode: {mode:2f}")

    def draw(self):
        self.Mean()
        self.Median()
        self.Mode()


ct = centralTendencies(weights)
ct.draw()

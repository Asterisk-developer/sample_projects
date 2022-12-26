import csv
from itertools import groupby
from operator import itemgetter

with open('testData.csv','r') as csv_file:    
    csv_reader = csv.DictReader(csv_file)

    # for line in csv_reader:
    #     print(line)
    items = sorted(csv_reader,key=itemgetter('Position'))

    for key, value in groupby(items,key=itemgetter('Position')):
        print(key)
        for k in value:
            print(k['Name'])

import csv
from itertools import groupby
from operator import itemgetter
import test
# import pandas as pd

with open('testcsv.csv','r') as csv_file:    
    csv_reader = csv.DictReader(csv_file)

    # for line in csv_reader:
    #     print(line)
    items = sorted(csv_reader,key=itemgetter('SHIP-ID'))

    for key, value in groupby(items,key=itemgetter('SHIP-ID')):
        print(key)
        siteNames=[]
        for k in value:
            siteNames.append(k['SITE-NAME'])
            print(k)
        print(siteNames)
        lcs=test.findstem(siteNames)
        print(lcs)
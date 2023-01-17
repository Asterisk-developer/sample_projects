import csv
from itertools import groupby
from operator import itemgetter

print('hello')
items =[{}]

with open(r'new/testcsv.csv','r') as csv_file:    
    csv_reader = csv.DictReader(csv_file)

    # for line in csv_reader:
    #     print(line)
    items = sorted(csv_reader,key=itemgetter('CITY-NAME'))
    # print('hello',items)

    # for key, value in groupby(items,key=itemgetter('CITY-NAME')):
    #     print(key)
    #     for k in value:
    #         print(k)

fields = ['MIG-ID','SHIP-ID','SITE-NAME','CITY-NAME']

filename = "university_records.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv dict writer object 
    writer = csv.DictWriter(csvfile, fieldnames = fields) 
        
    # writing headers (field names) 
    writer.writeheader() 
        
    # writing data rows 
    writer.writerows(items) 

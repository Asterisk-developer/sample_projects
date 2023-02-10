import csv
from itertools import groupby
from operator import itemgetter


items =[{}]

with open(r'testData.csv','r') as csv_file:    
    csv_reader = csv.DictReader(csv_file)

    # for line in csv_reader:
    #     print(line)
    items = sorted(csv_reader,key=itemgetter('MS4 Ship-to BPID'))   
    for key, value in groupby(items,key=itemgetter('MS4 Ship-to BPID')):
        print(key)
        
        for k in value:
            print(k)

# fields = ['MIG-ID','SHIP-ID','SITE-NAME','CITY-NAME']

# filename = "university_records.csv"
    
# # writing to csv file 
# with open(filename, 'w') as csvfile: 
#     # creating a csv dict writer object 
#     writer = csv.DictWriter(csvfile, fieldnames = fields) 
        
#     # writing headers (field names) 
#     writer.writeheader() 
        
#     # writing data rows 
#     writer.writerows(items) 

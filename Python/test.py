
from collections import defaultdict
import re
import random

def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and all(data[0][i:i+j] in x for x in data):
                    substr = data[0][i:i+j]
    
    return remove_special_chars(substr)

def replace_site_name(max,min,data):    
    for i,j in data.loc[(data['New site name'].str.len()>=min) & (data['New site name'].str.len()<=max)].iterrows():        
        if min == 2:
            data.loc[data['New site ID']==j['New site ID'],'New site name'] = j['New site name'] + '_' + j['City (from ShipToCode or IPSO BPID)']
        elif min == 0:
            data.loc[data['New site ID']==j['New site ID'],'New site name'] = j['City (from ShipToCode or IPSO BPID)']
            
    

def remove_special_chars(str):
    return re.sub(r"^\W+", "", re.sub(r'([^\w\s]|_)+(?=\s|$)', "", str)).lstrip().rstrip()

def check_already_present(generated_items,string_to_check,site_id,data):
    if generated_items.count(string_to_check) >  1:
        new_site_name = string_to_check + '_' + str(random.randint(0,9))        
        check_already_present(generated_items,new_site_name,site_id,data)        
    else:
        data.loc[data['New site ID']==site_id,'New site name']= string_to_check    

  
    
    
 

 

 

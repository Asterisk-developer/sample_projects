import re
import uuid

def long_substr(data):
    substr = ''
    if len(data) == 1:
        return remove_special_chars(data[0])
    elif len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and all(data[0][i:i+j] in x for x in data):
                    substr = data[0][i:i+j]
    
    return remove_special_chars(substr)

def replace_site_name(max,min,data):    
    for i,j in data.loc[(data['New site name'].str.len()>=min) & (data['New site name'].str.len()<=max)].iterrows():        
        if min == 2:
            data.loc[data['New site ID']==j['New site ID'],'New site name'] = j['New site name'] + '_' + j['CITY']
        elif min == 0:
            data.loc[data['New site ID']==j['New site ID'],'New site name'] = j['CITY']
            
    

def remove_special_chars(str):
    return re.sub(r"^\W+", "", re.sub(r'([^\w\s]|_)+(?=\s|$)', "", str)).lstrip().rstrip()

def check_already_present(generated_items,string_to_check,site_id,data,bpid,lcs_with_id):    
    if generated_items.count(string_to_check) >  0:   
        matched_items = [s for s in generated_items if string_to_check in s] 
        append_number = match_check(matched_items)      
        new_site_name = (data.loc[data['New site ID']==site_id,'New site name'].tolist())[0] + '_' + str(append_number)                              
        check_already_present(generated_items,new_site_name,site_id,data,bpid,lcs_with_id)        
    else:                
        if (len(lcs_with_id[bpid]) >= 0) and (data.loc[data['MS4 SHIP TO BPID'] == bpid].shape[0] > 1):
            data.loc[data['MS4 SHIP TO BPID']==bpid,'New site name'] = string_to_check
            data.loc[data['MS4 SHIP TO BPID']==bpid,'New site ID'] = uuid.uuid4()
        else:
            data.loc[data['New site ID']==site_id,'New site name'] = string_to_check      
    
def match_check(items):
    append_number = 2
    for i in items:
        split_str = i.split('_')        
        if (len(split_str) > 1 ):
            if (split_str[1].isnumeric()) and (int(split_str[1]) >= append_number):
                append_number = int(split_str[1])  + 1                            
    return append_number
            

 

 

 

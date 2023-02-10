import pandas as pd
import test
import uuid

d = {}
lcsDict = {}
generated_itsm = []
lcs_with_id ={}

df = pd.read_csv('input_file.csv')
rows_count, columns_count = df.shape
sorted_data = df.loc[0:rows_count, ['MS4 SHIP TO BPID', 'SITE_NAME',
                                    'CITY', 'New site name']].sort_values(by='MS4 SHIP TO BPID')
common_bpid_cnt = sorted_data['MS4 SHIP TO BPID'].value_counts()

for key in common_bpid_cnt.keys():
    filt = sorted_data['MS4 SHIP TO BPID'] == key
    site_names = sorted_data.loc[filt, 'SITE_NAME']    
    d[key] = sorted_data.loc[filt, 'SITE_NAME'].tolist()

for i in range(rows_count):
    df.at[i, 'New site ID'] = uuid.uuid4()

for i in d.keys():    
    lcs = test.long_substr(d[i])    
    df.loc[df['MS4 SHIP TO BPID'] == i, 'New site name'] = lcs
    
    lcs_with_id[i] = lcs

test.replace_site_name(3, 2, df)
test.replace_site_name(1, 0, df)

for i in range(rows_count):
    changing_bpid = df.loc[i,'MS4 SHIP TO BPID']
    generated_itsm = df.loc[df['MS4 SHIP TO BPID'] != changing_bpid,'New site name'].tolist()    
    test.check_already_present(generated_itsm,df.loc[i,'New site name'],df.loc[i,'New site ID'],df,changing_bpid,lcs_with_id)  
   
for i in range(rows_count):
    if((df.loc[i,'SITE_NAME']).lstrip().rstrip() == df.loc[i,'New site name']):        
        df.at[i, 'New site ID'] = df.loc[i,'Site Id']
        df.loc[df['MS4 SHIP TO BPID']==df.loc[i,'MS4 SHIP TO BPID'],'New site ID'] = df.loc[i,'Site Id']
df.to_csv('demo.csv', index=False)


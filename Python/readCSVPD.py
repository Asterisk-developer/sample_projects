import pandas as pd
import test
import uuid
d = {}
lcsDict = {}
generated_itsm = []
lcs_with_id ={}

df = pd.read_csv('testData1.csv')
rows_count, columns_count = df.shape
sorted_data = df.loc[0:rows_count, ['MS4 Ship-to BPID', 'Site name',
                                    'City (from ShipToCode or IPSO BPID)', 'New site name']].sort_values(by='MS4 Ship-to BPID')
common_bpid_cnt = sorted_data['MS4 Ship-to BPID'].value_counts()

for key in common_bpid_cnt.keys():
    filt = sorted_data['MS4 Ship-to BPID'] == key
    site_names = sorted_data.loc[filt, 'Site name']    
    d[key] = sorted_data.loc[filt, 'Site name'].tolist()

for i in range(rows_count):
    df.at[i, 'New site ID'] = uuid.uuid4()

for i in d.keys():
    lcs = test.long_substr(d[i])    
    df.loc[df['MS4 Ship-to BPID'] == i, 'New site name'] = lcs
    if df.loc[df['MS4 Ship-to BPID'] == i].shape[0] ==1:    
        df.loc[df['MS4 Ship-to BPID'] == i,'New site ID'] = df.loc[df['MS4 Ship-to BPID'] == i,'Site ID']
    lcs_with_id[i] = lcs

test.replace_site_name(3, 2, df)
test.replace_site_name(1, 0, df)

for i in range(rows_count):
    changing_bpid = df.loc[i,'MS4 Ship-to BPID']
    generated_itsm = df.loc[df['MS4 Ship-to BPID'] != changing_bpid,'New site name'].tolist()    
    test.check_already_present(generated_itsm,df.loc[i,'New site name'],df.loc[i,'New site ID'],df,changing_bpid,lcs_with_id)  
    

df.to_csv('demo.csv', index=False)



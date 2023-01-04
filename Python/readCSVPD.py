import pandas as pd
import test
import uuid

df = pd.read_csv('testData.csv')
rows_count, columns_count = df.shape
sorted_data = df.loc[0:rows_count, ['MS4 Ship-to BPID', 'Site name','City (from ShipToCode or IPSO BPID)','New site name']].sort_values(by='MS4 Ship-to BPID')
common_bpid_cnt = sorted_data['MS4 Ship-to BPID'].value_counts()
d = {}

for key in common_bpid_cnt.keys():
    filt = sorted_data['MS4 Ship-to BPID'] == key
    site_names = sorted_data.loc[filt, 'Site name']
    d[key] = sorted_data.loc[filt, 'Site name'].tolist()

lcsDict = {}
    
for i in d.keys():    
    lcs=test.long_substr(d[i])
    df.loc[df['MS4 Ship-to BPID'] == i,'New site name'] =lcs
    # df.loc[df['MS4 Ship-to BPID'] == i,'New site ID'] =uuid.uuid4()    

for i in range(rows_count):
    print(uuid.uuid4())
    df.at[i,'New site ID'] = uuid.uuid4()
# print(df)
test.replace_site_name(3,2,df)
test.replace_site_name(1,0,df)
# for i,j in df.loc[(df['New site name'].str.len()>1) & (df['New site name'].str.len()<4)].iterrows():
#     print(j)
#     df.loc[df['New site ID']==j['New site ID'],'New site name'] = j['New site name'] + '_' + j['City (from ShipToCode or IPSO BPID)']
    
# print(df)

df.to_csv('demo.csv')



    

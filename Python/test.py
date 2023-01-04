
from collections import defaultdict

def findstem(arr):
 
    # Determine size of the array
    n = len(arr)
 
    # Take first word from array
    # as reference
    s = arr[0]
    l = len(s)
 
    res = ""
 
    for i in range(l):
        for j in range(i + 1, l + 1):
 
            # generating all possible substrings
            # of our reference string arr[0] i.e s
            stem = s[i:j]
            print('stem',stem)
            k = 1
            for k in range(1, n):
 
                # Check if the generated stem is
                # common to all words
                if stem not in arr[k]:
                    break
 
            # If current substring is present in
            # all strings and its length is greater
            # than current result
            if (k <= n and len(res) < len(stem)):
                print(stem,k)
                res = stem
 
    return res
def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and all(data[0][i:i+j] in x for x in data):
                    substr = data[0][i:i+j]
    
    return substr.lstrip().rstrip()

def testLong(test_list):
    temp = defaultdict(int)
    for sub in test_list:
        for wrd in sub.split():
            temp[wrd] += 1
    res = max(temp, key=temp.get)
    print("Word with maximum frequency : " + str(res))

def replace_site_name(max,min,data,):
    for i,j in data.loc[(data['New site name'].str.len()>=min) & (data['New site name'].str.len()<=max)].iterrows():
        # print(j)
        if min == 2:
            data.loc[data['New site ID']==j['New site ID'],'New site name'] = j['New site name'] + '_' + j['City (from ShipToCode or IPSO BPID)']
        elif min == 0:
            data.loc[data['New site ID']==j['New site ID'],'New site name'] = j['City (from ShipToCode or IPSO BPID)']



# Driver Code
if __name__ == "__main__":
 
    arr = ["pumalanga (White River)","Mpumalanga DC (White River)"]
    
     
    # Function call
    testLong(arr)
    # print(stems)        
    
    
 

 

 

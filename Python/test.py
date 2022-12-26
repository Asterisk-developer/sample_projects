import test1

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
            k = 1
            for k in range(1, n):
 
                # Check if the generated stem is
                # common to all words
                if stem not in arr[k]:
                    break
 
            # If current substring is present in
            # all strings and its length is greater
            # than current result
            if (k + 1 == n and len(res) < len(stem)):
                res = stem
 
    return res
def greet():
    print("hello")
    print("Good morning")
def add(x,y):
    c=x+y
    return c
 
# Driver Code
if __name__ == "__main__":
 
    arr = ["gre", "graceful",
           "disgraceful", "gracefully"]
    data_table = [{'Mig-ID': 'PATB34 FROO 87554', 'SN': 'NLCVNC214L','IPSO-Ship-to-BPID': '1559685', 'Ship-to-BPID': '6438', 'Site-ID': '537fgasgdghj636', 'Site-name': 'Country HQ West','ShiptoCode': 'Bordeaux'}, 
                  {'Mig-ID': 'PATB34 FROO 87554', 'SN': 'NLCVNC2485','IPSO-Ship-to-BPID': '1559685', 'Ship-to-BPID': '6438', 'Site-ID': 'asdasuu276asfdh', 'Site-name': 'Country HQ New', 'ShiptoCode': 'Bordeaux'},
                  {'Mig-ID': 'PATB34 PT00 57422', 'SN': 'NLCVNC300K','IPSO-Ship-to-BPID': '8534', 'Ship-to-BPID': '72653', 'Site-ID': 'asdasuu2SDFasfdh', 'Site-name': 'Country HQ PT', 'ShiptoCode': 'Porto'},
                  {'Mig-ID': 'PATB34 PT00 6324', 'SN': 'NLCVNC3001','IPSO-Ship-to-BPID': '3580985', 'Ship-to-BPID': '72653', 'Site-ID': 'asdasdasdasad', 'Site-name': 'Country HQ PT00', 'ShiptoCode': 'Porto'},
                  {'Mig-ID': 'PATB34 ZAOO 87554', 'SN': 'NLCVNC3002','IPSO-Ship-to-BPID': '1372804', 'Ship-to-BPID': '35212', 'Site-ID': '324HGASDF8763476', 'Site-name': 'Country HQ', 'ShiptoCode': 'Durban'},]
    
    # print(data_table[0]['id'])
    # df =pd.read_csv('nba.csv')
    # print(df)
     
    # Function call
    stems = findstem(arr)
    print(stems )        
    add(1,2)
 
# This code is contributed by ita_c
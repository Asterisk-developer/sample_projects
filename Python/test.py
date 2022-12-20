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
     
    # Function call
    stems = findstem(arr)
    print(stems )        
    add(1,2)
 
# This code is contributed by ita_c
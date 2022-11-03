def expand(s,low,high,pelindromes):

    while low>0 and high<len(s) and s[low]==s[high]:
        p=s[low:high+1]
        if len(p)>1:
            pelindromes.add(p)
        low-=1
        high+=1

def allPelindromes(s):
    pelindromes=set()
    
    for i in range(len(s)):
        expand(s,i,i,pelindromes)
        expand(s,i,i+1,pelindromes)
    print(pelindromes)
allPelindromes("abcbdbzzdz")
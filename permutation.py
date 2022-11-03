
def permutation(s,ans):
    if len(s)==0:
        print(ans,end=" ")
        return
    for i in range(len(s)):
        char=s[i]
        left=s[:i]
        right=s[i+1:]
        result=left+right
        permutation(result,ans+char)

ans=" "
permutation("abc",ans)
def evennoofdigits(nums:list):
    result=0
    for i in range(0,len(nums)):
        k=str(nums[i])
        if len(k)%2==0:
            result+=1
        

    return result 


print(evennoofdigits([12,345,2,6,7896]))


"""
 def __init__(self):
        self.n=0
        self.m=0
        self.mylist=[[""]*self.n]*self.m
        # print(self.mylist)
    
    def createlist(self,n,m):
        for i in range(0,m):
            col=[]
            for j in range(0,n):
                k=input(f"enter the value at{i}:{j}=")
                col.append(k)

            self.mylist.append(col)    

        print(self.mylist)
"""
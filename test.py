def findMaxConsecutiveOnes(nums):
    count=0 #it will store number of consecutive during itretion
    result=0
    for i in range(0,len(nums)):
        if nums[i]==1:
            count+=1

        if nums[i]==0 or i==len(nums)-1:
            print(i)
            # print(max(result,count))
            result=max(result,count)
            count=0
                
    print(result)



findMaxConsecutiveOnes([1,0,1,1,0,1])
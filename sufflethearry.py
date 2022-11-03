def suffleArry(myarry,num):
    result=[]
    list1=myarry[0:num]
    list2=myarry[num:]
    for i in range(0,num):
        result.append(list1[i])
        result.append(list2[i])
    print(result)





suffleArry([1,2,3,5,4,3,2,1],4)
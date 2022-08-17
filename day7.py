# just fake commit 
#list in python  
mylist=["apple","banana","orange"]
print(mylist)
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(len(mylist))

mylist.insert(2,"cherry") 
print(mylist)
mylist.append("papaya")
print(mylist)

if "apple" in mylist:
    print("apple is in the list")

mylist2=["zebra","cow","elephant"]
mylist.extend(mylist2)
# mylist.extend(mylist)
print(mylist)
#comments in python 
# it is done by adding # at the starting of the line 
# there is basically no multiline comment bu we can use them 
"""
hi i am multiline commment  
can be converted into string
hey
"""

print ("my name is",end=" ") # to print next line in same line
#default value of end is \n
print("divyanshu") #can add after the line
# print(end) it will work

# data types in python 
"""
int --> intgers 
float --> decimals numbers 
string -->streams of letters, "anything written in double or string quotes consider as string"
bool --> true, false
"""
#  print(type(True))

# variables in python 
greetings ="hello !"
name = "Divyanshu "
print(greetings,name)
print(greetings + name )

#taking input
# myname= input("enter your name ") it will just take input in string form 
# for input in other form  typecast the input
myname= int (input("enter your roll no") )
print(myname)
print(type(myname))


"""
operator in python 

+ --> add
- --> minus
* --> multiply
/ --> divide
// --> integer division 
% --> it will give reminder     
** --> power

comprision  operators
# it will only give true or false   
<
> 
==
or ||
and &&


"""
a=15
b=4
c="hello"
print(a+b)
print(a-b)
print(a/b) # it will give float for integer typecast
print(a==b) # comprision operator
print(a==c) # it is comparing it will not throw error
#print(a>c) but it will throw error



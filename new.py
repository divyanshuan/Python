from xml.sax import xmlreader


print("Hello World")
x=4
x="Hello"
print(x)
_my_var =[" Ram", "Shyam", "Mohan"]
x, y, z =_my_var
print(x)

x="good"
def myfunc():
    global x
    x="fantastic"

myfunc()
print('Python is' +x)

b="Bytecode Learners"
print(b.upper())
print(b.replace("B", "H"))

list =["Apple", "Banana","Pineapple"

]
print(list)
print(len(list))

list.insert(2,"watermelon")
print(list)

list.pop(0)
print(list)
tuple=tuple(("Apple","Banana",
"Watermelon"))
print(tuple)

set={"Apple", "Banana","Watermelon"}
print(set)

dict={
    "brand":"apple",
    "model":"macbook",
    "year":"2022",

    }
x=dict.values()
dict.update({"year":"2021"})    
print(x)

fruits = ["apple","banana","watermelon"]
for x in fruits:
    if x=="banana":
        # break
          print(x)






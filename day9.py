s="hello world is her"


def lastword (myly):
    mylist= s.split(" ")
    for x in reversed(mylist):
        if x!="":
            return len(x)


m= lastword(s)
print(m)
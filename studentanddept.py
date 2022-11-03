from dataclasses import dataclass


@dataclass 
class Student:
    sid:int
    name:str
    age:int
    d_name:str

s1=Student(1,"divyanshu",26,"CSE")
s2=Student(2,"abhinav",25,"MATHS")
s3=Student(3,"vikash",24,"MATHS")
s4=Student(14,"vishal",27,"ENGLISH")


@dataclass
class Department:
    did:int
    d_name:str
    sid:int

d1=Department(1,"CSE",1)
d2=Department(2,"MATHS",3)
d3=Department(3,"ENGLISH",4)
d4=Department(4,"GEOGRAPHY",5)


def innner_join(stu,dept):
    res=[]
    

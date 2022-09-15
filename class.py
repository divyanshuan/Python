class Time:
    """
    you can create object with three types 
    1. with default value 
    2. with input only in minutes
    3. with input hours and minutes both
    """
    def __init__(self,*args):
        if len(args)==0:
            self.hr=0
            self.min=0
        if len(args)==1:
            self.hr=args[0]//60
            self.min=args[0]%60
        if len(args)==2:
            self.hr=args[0]
            self.min=args[1]

    def gettime(self):
        return (self.hr,self.min)

    
t1=Time()
print(t1.gettime())
t2=Time(140)
print(t2.gettime())
t3=Time(1,23)
print(t3.gettime())


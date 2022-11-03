fibans= [None]*10
fibans[0]=0
fibans[1]=1
def fib(num):
    if fibans[num]!=None:
        return fibans[num]
    else:
        fibans[num]=fib(num-1)+fib(num-2)
        return fibans[num]

for i in range(10):
    print(fib(i))



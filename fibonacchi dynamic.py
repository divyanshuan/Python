def fib(num,fibans):
    if fibans[num]!=None:
        return fibans[num]
    else:
        fibans[num]=fib(num-1,fibans)+fib(num-2,fibans)
        return fibans[num]


if __name__=="__main__":
    n=int(input("Enter the range of fibonacci series: "))
    fibnas=[None for i in range(n)]
    fibnas[0],fibnas[1]=0,1
    print(fib(n-1,fibnas))
    for i in range(len(fibnas)):
        print(fibnas[i])

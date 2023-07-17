def factorial(val):
    temp = 1
    for i in range(1,val+1):
        temp = temp * i
        print(temp)
    return temp
val = factorial(8)
print('factorial is' ,end=" ")
print(val)
         
def fib(n):
    a=1
    b=1
    next=0
    for i in range(0,n):
        if i==0:
            next=1
            print(next,end=" ")
            continue
        print(next,end=" ")
        a=b
        b=next
        next=a+b


fib(10)
    
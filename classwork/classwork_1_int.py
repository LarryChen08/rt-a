import math
def checkprime(x):
    if x <= 1:
        return False
    for i in range(2,int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

def fibonacci(x):
    if x in fib_list:
        return True
    if fib_list[-1] > x:
        return False
    while True:
        a = fib_list[-1] + fib_list[-2]
        if a == x:
            return True
        if a > x:
            return False
        fib_list.append(a)

fib_list = [1,1]
while True:
    x = eval(input('x='))
    if x % 1 == 0:
        print('integer')
        if x % 2 == 0:
            print('even')
        else:
            print('odd')
        if math.sqrt(x) % 1 == 0:
            print('square')
        if checkprime(x):
            print('prime')
        if fibonacci(x):
            print('in fibonacci')
            print(fib_list)
    else:
        print('float')
    
def recursion(x):
    if x % 2 == 0:
        x //= 2
    else:
        x = x * 3 + 1
    if x == 1:
        return 1
    else:
        return recursion(x)
    

n = eval(input('n='))
print(recursion(n))
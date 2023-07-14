def jiaogu(n):
    if n % 2 == 0:
        n /= 2
    else:
        n = 3 * n +1
    return n

while True:
    n = eval(input('a='))
    while n > 1:
        n = jiaogu(n)
        print(n)
def find7(n):
    for p in range(1,k):
        if n % (10 * p) == 7:
            return True
        n //= 10
    if n == 7:
        return True
    return False

a, b = eval(input('a, b='))
cnt = b - a + 1
k = len(str(b))
print(k)
print('---------')
for i in range(a,b+1):
    if find7(i):
        print('过')
        continue
    if i % 7 == 0:
        print('过')
        continue
    print(i)
    cnt -= 1
print(cnt)    
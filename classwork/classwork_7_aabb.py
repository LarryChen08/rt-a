import math
'''
for a in range(9):
    for b in range(9):
        n = a * 1100 + b * 11
        if math.sqrt(n) % 1 == 0:
            print(n)

for i in range(10000):
    n = i
    n1 = n % 10
    n //= 10
    n2 = n % 10
    n //= 10
    n3 = n % 10
    n //= 10
    n4 = n % 10
    if n1 == n2 and n3 == n4 and math.sqrt(i) % 1 == 0:
        print(i)
'''
p = 0
while True:
    p += 1
    i = p * p
    if i >= 1000 and i < 10000:
        n = i
        n1 = n % 10
        n //= 10
        n2 = n % 10
        n //= 10
        n3 = n % 10
        n //= 10
        n4 = n % 10
        if n1 == n2 and n3 == n4 and math.sqrt(i) % 1 == 0:
            print(i)
    if i >= 10000:
        break

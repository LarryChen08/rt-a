n = 0
# 1
while True:
    n += 1
    if n % 7 == 2 and n % 5 == 3 and n % 3 == 2:
        print(n)
        break

# 2
for n in range(1000,0,-1):
    if n % 7 == 2 and n % 5 == 3 and n % 3 == 2:
        print(n)
        break

# 3
cnt = 0
for n in range(1001):
    if n % 7 == 2 and n % 5 == 3 and n % 3 == 2:
        cnt += 1
print(cnt)

# 4
n = 0
cnt = 0
nList = []
while True:
    n += 1
    if n % 7 == 2 and n % 5 == 3 and n % 3 == 2:
        cnt += 1
        nList.append(n)
        if cnt >= 12:
            break
print(cnt, nList)



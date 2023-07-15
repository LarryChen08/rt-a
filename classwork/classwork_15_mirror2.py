def cap(c):
    if 'a' < c < 'z':
        return chr(ord(c) - 32)
    return c

def is_mirror(n):
    for i in range(int(len(n)/2)):
        if cap(n[i]) == cap(n[-i-1]):
            continue
        return False
    return True

n = int(input('n='))
base = -1
cnt = 0
while True:
    base += 1
    num = str(base * base)
    if len(num) <= n:
        if is_mirror(num):
            print(int(num))
            cnt += 1
        continue
    break
print(cnt)

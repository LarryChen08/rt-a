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

def is_mirror2(n):
    n2 = ''
    rev = ''
    for c in n:
        rev = cap(c) + rev
        n2 += cap(c)
    return n2 == rev

n = input('input the word:')
if is_mirror2(n):
    print('This is mirror')
else:
    print('This is not mirror')

    







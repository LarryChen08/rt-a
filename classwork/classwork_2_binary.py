def binary(a):
    bi = ''
    while a != 0:
        bi = str(a%2) + bi
        a //= 2
    return bi

def tens(a):
    te = 0
    for i in range(-1,-(len(a)+1),-1):
        te += (2**(-i-1))*int(a[i])
    return te

n = int(input('n='))
bi_n = binary(n)
bi_n = '0' * (32 - len(bi_n)) + bi_n
bi_n = bi_n[16:] + bi_n[:16]
print(tens(bi_n))

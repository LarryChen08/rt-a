n = eval(input('n='))
for y in range(2 * n - 1):
    outStr = ''
    for x in range(abs(n - 1 - y)):
        outStr += ' '
    for x in range(2 * (n - abs(n - 1 - y)) -1):
        outStr += str(n - abs(n - y - 1) - abs(n - 1 - abs(n - 1 - y) - x))
    print(outStr)




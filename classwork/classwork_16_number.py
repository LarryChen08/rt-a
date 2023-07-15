numbers = '零一二三四五六七八九十百千'

while True:
    n = eval(input('n='))
    res_word = ''
    n %= 10000
    if n // 1000 != 0:
        res_word += numbers[n // 1000] + numbers[12]
        if n % 1000 == 0:
            print(res_word)
            continue
        if (n % 1000) // 100  == 0:
            res_word += numbers[0]
    # 100
    n %= 1000
    if n // 100 != 0:
        res_word += numbers[n // 100] + numbers[11]
        if n % 100 == 0:
            print(res_word)
            continue
        if (n % 100) // 10  == 0:
            res_word += numbers[0]
        if (n % 100) // 10  == 1:
            res_word += numbers[1]
    # 10
    n %= 100
    if n <= 10:
        res_word += numbers[n]
    elif n < 20:
        res_word += numbers[10] + numbers[n % 10]
    elif n % 10 == 0:
        res_word += numbers[n // 10] + numbers[10]
    else:
        res_word += numbers[n // 10] + numbers[10] + numbers[n % 10]
    print(res_word)

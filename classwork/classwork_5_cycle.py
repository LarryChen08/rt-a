hsList = ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
ebList = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
zList =  ['鼠','牛','虎','兔','龙','蛇','马','羊','猴','鸡','狗','猪']
while True:
    y = eval(input('year='))
    if y == 0:
        print('The input is wrong')
        continue
    if y < 0:
        y += 1
    hs = (y - 4) % 10
    eb = (y - 4) % 12
    print(hsList[hs], ebList[eb], zList[eb])



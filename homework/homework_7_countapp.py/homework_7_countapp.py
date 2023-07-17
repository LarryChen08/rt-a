def check_name(line, c):
    chara = nameDic[c]
    for i in range(len(line)):
        for j in range(len(chara)):
            if line[i:i+len(chara[j])] == chara[j]:
                countList[c] += 1
    return



nameDic = {'林黛玉':['林黛玉','黛玉','颦颦','潇湘妃子','泪美人'],
           '薛宝钗':['薛宝钗','宝钗','蘅芜君'],
           '贾元春':['贾元春','元春','贤德妃'],
           '贾探春':['贾探春','探春','玫瑰花'],
           '史湘云':['史湘云','湘云','枕上书'],
           '妙玉':['妙玉','空谷幽兰'],
           '贾迎春':['贾迎春','迎春','二木头'],
           '贾惜春':['贾惜春','惜春','勘破三春'],
           '王熙凤':['王熙凤','熙凤','凤辣子'],
           '贾巧姐':['贾巧姐','巧姐','余音绕梁'],
           '李纨':['李纨','稻香老农'],
           '秦可卿':['秦可卿','情可轻']}

countList = {'林黛玉':0,'薛宝钗':0,'贾元春':0,'贾探春':0,'史湘云':0,'妙玉':0,'贾迎春':0,'贾惜春':0,'王熙凤':0,'贾巧姐':0,'李纨':0,'秦可卿':0}

f = open('hlm.txt','r', encoding = 'gbk')
lineList = f.readlines()
f.close()

for line in lineList:
    for c in nameDic:
        check_name(line, c)

print(countList)
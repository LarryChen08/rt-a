def check_name(line, c):
    chara = nameDic[c]
    for i in range(len(line)):
        for j in range(len(chara)):
            if line[i:i+len(chara[j])] == chara[j]:
                countList[c] += 1
    return

def bubbling(nameList,countList):
    for a in range(len(countList)-1):
        flag = 0
        for i in range(len(countList)-1-a):
            if countList[i] < countList[i+1]:
                countList[i], countList[i+1] = countList[i+1], countList[i]
                nameList[i], nameList[i+1] = nameList[i+1], nameList[i]
                flag = 1        
        if flag == 0:
            return nameList, countList

'''
nameDic = {'林黛玉':['林黛玉','黛玉','颦颦','潇湘妃子','泪美人','林姑娘','林妹妹'],
           '薛宝钗':['薛宝钗','宝钗','蘅芜君','宝姐姐','宝丫头','宝姑娘'],
           '贾元春':['贾元春','元春','贤德妃','大姑娘','大小姐','贾妃','元妃','贵妃','娘娘'],
           '贾探春':['贾探春','探春','玫瑰花','三姑娘','蕉下客'],
           '史湘云':['史湘云','湘云','枕上书','史大姑娘','云姑娘','云妹妹','枕霞旧友'],
           '妙玉':['妙玉','空谷幽兰','槛外人','畸人'],
           '贾迎春':['贾迎春','迎春','二木头','二姑娘','二姐姐','二妹妹','二木头','迎丫头','菱洲'],
           '贾惜春':['贾惜春','惜春','勘破三春','二姐姐','二妹妹','二木头','迎丫头','菱洲'],
           '王熙凤':['王熙凤','熙凤','凤辣子','凤姐','琏二奶奶','凤哥儿','凤丫头','琏二嫂子','凡鸟'],
           '贾巧姐':['贾巧姐','贾巧','余音绕梁','巧哥儿','大姐儿','妞妞','大妞妞'],
           '李纨':['李纨','稻香老农','宫裁','大菩萨','大奶奶'],
           '秦可卿':['秦可卿','情可轻','秦氏','蓉大奶奶','可儿','兼美']}

countList = {'林黛玉':0,'薛宝钗':0,'贾元春':0,'贾探春':0,'史湘云':0,'妙玉':0,'贾迎春':0,'贾惜春':0,'王熙凤':0,'贾巧姐':0,'李纨':0,'秦可卿':0}'''

nameDic = {'曼城':'曼城', '曼联':'曼联', '阿森纳':'阿森纳', '切尔西':'切尔西', '热刺':'热刺', '利物浦':'利物浦'}
countList = {'曼城':0, '曼联':0, '阿森纳':0, '切尔西':0, '热刺':0, '利物浦':0}
f = open('hlm.txt','r', encoding = 'gbk')
lineList = f.readlines()
f.close()

for line in lineList:
    for c in nameDic:
        check_name(line, c)

nameList = list(countList.keys())
countList = list(countList.values())
nameList,countList = bubbling(nameList,countList)
for i in range(len(nameList)):
    print(nameList[i],countList[i])
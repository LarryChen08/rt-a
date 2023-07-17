def count(line):
    for p in range(len(line)):
        for i in wDic:
            if line[p:p+len(i)] == i:
                wDic[i] += 1

f = open('news.txt', 'r', encoding = 'gbk')
lineList = f.readlines()
f.close()

wDic = {'曼城':0, '曼联':0, '阿森纳':0, '切尔西':0, '热刺':0, '利物浦':0}

for line in lineList:
    count(line)

print(wDic)
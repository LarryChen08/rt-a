def cap(word):
    nw = ''
    for c in word:
        if 'A' <= c <= 'Z':
            nw += chr(ord(c) + 32)
            continue
        nw += c
    return nw


def count(line):
    for p in range(len(line)):
        for i in wDic:
            word = cap(line[p:p+len(i)])
            if word == i:
                wDic[i] += 1

wDic = {'manchester city':0, 'manchester united':0, 'arsenal':0, 'chelsea':0, 'liverpool':0,'newcastle':0}

f = open('news2.txt', 'r')
lineList = f.readlines()
f.close()

for line in lineList:
    count(line)

f = open('news3.txt', 'r')
lineList = f.readlines()
f.close()

for line in lineList:
    count(line)

f = open('news4.txt', 'r')
lineList = f.readlines()
f.close()

for line in lineList:
    count(line)

print(wDic)
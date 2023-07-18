import math
def max_list_index(nList):
    max, maxId = nList[0], 0
    for i in range(len(nList)):
        if nList[i] > max:
            max, maxId = nList[i], i
    return maxId


def checkprime(x):
    if x <= 1:
        return False
    for i in range(2,int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

n, m = eval(input('n, m:'))
primeList = []
for i in range(n, m+1):
    if checkprime(i):
        primeList.append(i) 

diffList = []
for j in range(len(primeList)-1):
    diffList.append(primeList[j+1]-primeList[j])
Index = max_list_index(diffList)
print(primeList[Index],primeList[Index+1])

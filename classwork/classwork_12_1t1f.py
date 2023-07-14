
def recursion(ans):
    if len(ans)== 4: 
        resList.append(ans)
    for c in places:
        if c in ans:
            continue
        ans += c
        recursion(ans)
        ans=ans[:-1]
    return

def check(item):
    if (item[0] == 'A') ^ (item[2] == 'B') == 1 and (item[0] == 'C') ^ (item[3] == 'D') == 1 and (item[0] == 'D') ^ (item[2] == 'B'):
        return True
    return False

places = 'ABCD'
resList = []
recursion('')

for item in resList:
    if check(item):
        print(item)

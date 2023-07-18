def change_flag(n):
    for i in range(n, 101, n):
        flagList[i-1] = 1- flagList[i-1]
    return

flagList = [0]*100
for i in range(1,101):
    change_flag(i)

for j in range(len(flagList)):
    if flagList[j] == 1:
        print(j+1)


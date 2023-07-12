import random
import pandas as pd

def win(pNum, cNum):
    if cNum == pNum:
        wList[1] += 1
        print('draw')
    elif (pNum - cNum) % 3 == 2:
        wList[0] += 1
        df.iloc[pNum-1,1] += 1
        print('player win')
    else:
        wList[2] += 1
        print('cpu win')
    return

def check_move():
    score_list = [0,0,0]
    cnt_rep = 0.5
    for i in range(len(record)-1):
        cnt_rep -= 0.1
        if record[i] == record[-1]:
            k = win_dic[record[i+1]]
            n = 0
            score = 1
            while True:
                n += 1
                if n > i:
                    break
                if record[i-n] == record[-1-n]:
                    score += 1
                    continue
                break
            score -= cnt_rep
            score_list[k-1] += score
    return score_list

def gen_c(score_list):
    if score_list == [0,0,0]:
        return random.randint(1,3)
    return score_list.index(max(score_list)) + 1


win_dic = {2:1,3:2,1:3}
nameList = ['stone', 'scissors', 'paper']
wList = [0,0,0]
df = pd.DataFrame([[0,0],[0,0],[0,0]],columns = ['total','win'],index=nameList)
record = []
cnt = 0
while True:
    pNum = eval(input('1:stone, 2:scissors, 3:paper, 4:quit'))
    
    if pNum == 4:
        break
    if not (pNum in [1,2,3]):
        continue
    score_list = check_move()
    cNum = gen_c(score_list)
    print(cNum)
    record.append(pNum)
    df.iloc[pNum-1,0] += 1
    cnt += 1
    print('Computer - ' + nameList[cNum - 1] + '  :  ' + nameList[pNum - 1] + ' - Player')
    win(pNum, cNum)



player_w = int(wList[0]*100/cnt + 0.5)
draw = int(wList[1]*100/cnt + 0.5)
cpu_w = int(wList[2]*100/cnt + 0.5)

print('player win: ' + str(wList[0]) + '\tplayer win rate: ' + str(player_w) + '%')
print('draw: ' + str(wList[1]) + '\tdraw rate: ' + str(draw) + '%')
print('cpu win: ' + str(wList[2]) + '\tcpu win rate: ' + str(cpu_w) + '%')

stone_w = int(df.iloc[0,1]*100/df.iloc[0,0])
scissors_w = int(df.iloc[1,1]*100/df.iloc[1,0])
paper_w = int(df.iloc[2,1]*100/df.iloc[2,0])

print('stone win rate: ' + str(stone_w) + '%')
print('scissors win rate: ' + str(scissors_w) + '%')
print('paper win rate: ' + str(paper_w) + '%')



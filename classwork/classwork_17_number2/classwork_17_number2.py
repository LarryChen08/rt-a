import pygame, time
def sound_num(s):
    sStr = '零一二三四五六七八九十百千万亿兆京'
    for c in s:
        for i in range(len(sStr)):
            if c == sStr[i]:
                soundList[i].play()
                time.sleep(soundList[i].get_length()/2)

def number(a):
    res_word = ''    
    if a[0] =='0':
        res_word += number_list[0]
    a = a.lstrip('0')
    k = len(a)
    a_rs = a.rstrip('0')
    final_0 = len(a) - len(a_rs)
    for i in range(k - final_0):
        if a[i] == '0':
            if a[i + 1] == '0':
                continue
            res_word += number_list[int(a[i])]
            continue
        res_word += number_list[int(a[i])] + index_list[i + 4 - k]
    if len(res_word) >= 2:
        if res_word[0] == number_list[1] and res_word[1] == index_list[2]:
            res_word = res_word[1:]
    return res_word

# ----init----
pygame.mixer.init()
soundList = []
for i in range(11):
    sound = pygame.mixer.Sound(str(i) + '.wav')
    soundList.append(sound)

for i in ('H', 'K', '10K', '100M', 'T', '10KT'):
    sound = pygame.mixer.Sound(str(i) + '.wav')
    soundList.append(sound)
            

number_list = ['零','一','二','三','四','五','六','七','八','九']
index_list = ['千','百','十','']
index2_list = ['','万','亿','兆', '京']

while True:
    n = input('n=')
    if len(n) > 20:
        print('the number is too big')
        continue
    l = len(n) // 4 + ((len(n) % 4) != 0)
    result = ''
    for i in range(l):
        slice_a = n[-4:]
        n = n[:-4]
        num = number(slice_a)
        if num == number_list[0] and l != 1:
            continue
        result = number(slice_a) + index2_list[i] + result
    print(result)
    sound_num(result)



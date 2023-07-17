def check_alpha(c):
    return 'a' <= c <= 'z' or 'A' <= c <= 'Z'


txt = 'This is a book'
wList = []
word = ''
# is alpha
for c in txt:
    if check_alpha(c):
        word += c
    else:
        if word == '':
            continue
        wList.append(word)
        word = ''
if word != '':
    wList.append(word)
print(wList)
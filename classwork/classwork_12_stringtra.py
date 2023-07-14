word = 'Hello world'
w1 = ''
w2 = ''
for c in word:
    c1 = chr(ord(c)+1)
    w1 += c1
    w2 = c1 + w2
print(w1)
print(w2)
w1 = ''
w2 = ''
for p in range(len(word)):
    c = word[p]
    print(p,c)
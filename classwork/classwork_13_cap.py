word = 'Hello world!'
nw = ''

for c in word:
    if 97 <= ord(c) <= 122:
        nw += chr(ord(c) - 32)
        continue
    nw += c
print(nw)
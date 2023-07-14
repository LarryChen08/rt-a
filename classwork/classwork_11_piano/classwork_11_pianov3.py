import pygame, sys
def get_key_index(key, keyList):
    for i in range(len(keyList)):
        if key == ord(keyList[i]):
            return i
    return -1

# ----pygame init----
pygame.init()
pianoImg = pygame.image.load('piano.bmp')
screen = pygame.display.set_mode(pianoImg.get_size())
pygame.display.set_caption('RT-PIANO')

# ----data init----
noteImg = pygame.image.load('note.bmp')
keyList = 'zxcvbnm' + 'qwertyu' + 'sdghj' + '23567'
soundList = []
for noteLevel in '34':
    for noteName in 'cdefgab':
        oggSound = pygame.mixer.Sound(noteName + noteLevel + '.ogg')
        soundList.append(oggSound)
for noteLevel in '34':
    for noteName in 'cdfga':
        oggSound = pygame.mixer.Sound(noteName + noteLevel + 'm.ogg')
        soundList.append(oggSound)
keyFlagList = [0]*24
print(len(soundList))

# ----main loop----
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            i = get_key_index(event.key, keyList)
            if i >= 0:
                soundList[i].play()
                keyFlagList[i] = 1
        elif event.type == pygame.KEYUP:
            i = get_key_index(event.key, keyList)
            if i >= 0:
                keyFlagList[i] = 0
    screen.blit(pianoImg, (0,0))
    for i in range(len(keyFlagList)):
        if keyFlagList[i]:
            if i < 14:
                screen.blit(noteImg, (i * 30 + 2, 80))
                continue
            i += (i > 15) + (i > 18) + (i > 20)
            screen.blit(noteImg, ((i - 14) * 30 + 17, 15))
    pygame.display.update()
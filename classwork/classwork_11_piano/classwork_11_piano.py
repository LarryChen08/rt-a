import pygame, sys
# ----pygame init----
pygame.init()
pianoImg = pygame.image.load('piano.bmp')
screen = pygame.display.set_mode(pianoImg.get_size())
pygame.display.set_caption('RT-PIANO')
keyList = ['z','x','c','v','b','n','m']
soundList = ['c4','d4','e4','f4','g4','a4','b4']
fileList = []
for i in range(7):
    fileList.append(pygame.mixer.Sound(soundList[i] + '.ogg'))


# ----main loop----
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == ord('1'):
                Do.play()
            if event.key == ord('2'):
                Re.play()
    screen.blit(pianoImg,(0,0))
    pygame.display.update()

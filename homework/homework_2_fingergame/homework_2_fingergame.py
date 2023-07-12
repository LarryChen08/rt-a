import pygame, sys, random, time

SCREEN_W, SCREEN_H = 800, 600
LEFT_FINGER_X, RIGHT_FINGER_X, FINGER_Y = 150, 480, 180
NAME_X, NAME_Y = 140, 410
SCORE_X, SCORE_Y = 300, 470
RESULT_X, RESULT_Y = 300, 250

def RT_show_txt(scr, txt, font, x, y, c):
    img = font.render(txt, True, c)
    scr.blit(img, (x, y))
    return

def RT_count_finger(pNum, cNum):
    print(pNum, cNum)
    if (pNum - cNum) % 5 == 1:
        return 1, 0
    if (cNum - pNum) % 5 == 1:
        return 0, 1
    return 0, 0

# ----init----
pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()
bgImg = pygame.image.load('background.jpg')
font = pygame.font.Font('simkai.ttf', 64)

fgLeftList = []
fgRightList = []
for i in range(5):
    img = pygame.image.load('LFinger' + str(i) + '.bmp')
    img.set_colorkey((0,0,0))
    fgLeftList.append(img)
    img = pygame.image.load('RFinger' + str(i) + '.bmp')
    img.set_colorkey((0,0,0))
    fgRightList.append(img)

pScore, cScore = 0, 0
sysStatus = 0
while True:
    cNum = random.randint(0,4)
    pNum = random.randint(0,4)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #print(event.key)
            if ord('1') <= event.key <= ord('5'):
                pNum = event.key - ord('1')
                sysStatus = 1
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()   
    
    screen.blit(bgImg, (0,0))
    screen.blit(fgLeftList[pNum], (LEFT_FINGER_X, FINGER_Y))
    screen.blit(fgRightList[cNum], (RIGHT_FINGER_X, FINGER_Y))

    if sysStatus == 1:
        p, c = RT_count_finger(pNum, cNum)
        pScore += p
        cScore += c
        if p == 1:
            RT_show_txt(screen, 'You Win!', font, RESULT_X, RESULT_Y, (0,255,0))
        if c == 1:
            RT_show_txt(screen, 'You Lose!', font, RESULT_X, RESULT_Y, (255,0,0))
        if p == c:
            RT_show_txt(screen, 'Tie!', font, RESULT_X, RESULT_Y, (0,0,255))
    RT_show_txt(screen, 'PLAYER : COMPUTER', font, NAME_X, NAME_Y, (220,255,0))
    RT_show_txt(screen, str(pScore) + '      ' + str(cScore), font, SCORE_X, SCORE_Y, (220,255,0))

    pygame.display.update()
    if sysStatus == 1:
        time.sleep(1)
        sysStatus = 0
    clock.tick(10)
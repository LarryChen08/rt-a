import pygame, random, sys
SCREEN_W, SCREEN_H = 800, 600
# ----init----
pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
mList = [100]*100
w = SCREEN_W // 100
base = 200
# ----main loop----
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0,0,0))
    # distribute money
    A = random.randint(0,99)
    B = random.randint(0,99)
    mList[A] -= 1
    mList[B] += 1
    mList.sort()
    for i in range(100):
        money = mList[i]
        if money < 0:
            pygame.draw.rect(screen, (255,0,0), (i*w, base, w-1, mList[i]), 0)
        else:
            pygame.draw.rect(screen, (0,255,0), (i*w, SCREEN_H - mList[i] - base, w-1, mList[i]), 0)
    pygame.display.update()
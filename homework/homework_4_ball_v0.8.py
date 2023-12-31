import pygame, sys, random
SCREEN_W, SCREEN_H = 1024, 600

def RT_draw(screen, pixel, x0, y0, scale):
    color = (pygame.color.THECOLORS['black'],
             pygame.color.THECOLORS['gray32'],
             pygame.color.THECOLORS['gray64'],
             pygame.color.THECOLORS['white'],
             pygame.color.THECOLORS['red'],
             pygame.color.THECOLORS['green'],
             pygame.color.THECOLORS['blue'],
             pygame.color.THECOLORS['orange'],
             pygame.color.THECOLORS['brown'],
             pygame.color.THECOLORS['purple'],
             pygame.color.THECOLORS['yellow'],
             pygame.color.THECOLORS['cyan'],
             pygame.color.THECOLORS['sienna'],
             pygame.color.THECOLORS['chocolate'],
             pygame.color.THECOLORS['coral'],
             pygame.color.THECOLORS['darkgreen'])
    for y in range(len(pixel)):
        line = pixel[y]
        for x in range(len(line)):
            if 'A' <= line[x] <= 'F':
                c = color[ord(line[x]) - 55]
            elif '0' <= line[x] <= '9':
                c = color[eval(line[x])]
            else:
                continue
            pygame.draw.rect(screen, c, (int(x*scale+x0), int(y*scale+y0), scale, scale), 0)

# ----pygame init----
pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()

# ----data init----
scale = 4
actList = []

pixel = ['....DD....',
         '..DDAADD..',
         '.DDDAADDD.',
         '.DDDAADDD.',
         'DDDDAADDDD',
         'DDDDAADDDD',
         '.DDDAADDD.',
         '.DDDAADDD.',
         '..DDAADD..',
         '....DD....']
actList.append(pixel)

pixel = ['....DD....',
         '..DDDDDD..',
         '.DDDDDDAD.',
         '.DDDDDAAD.',
         'DDDDDAADDD',
         'DDDDAADDDD',
         '.DDAADDDD.',
         '.DAADDDDD.',
         '..ADDDDD..',
         '....DD....']
actList.append(pixel)

pixel = ['....DD....',
         '..DDDDDD..',
         '.DDDDDDDD.',
         '.DDDDDDDD.',
         'DAAAAAAAAD',
         'DAAAAAAAAD',
         '.DDDDDDDD.',
         '.DDDDDDDD.',
         '..DDDDDD..',
         '....DD....']
actList.append(pixel)

pixel = ['....DD....',
         '..DDDDDD..',
         '.DADDDDDD.',
         '.DAADDDDD.',
         'DDDAADDDDD',
         'DDDDAADDDD',
         '.DDDDAADD.',
         '.DDDDDAAD.',
         '..DDDDDA..',
         '....DD....']
actList.append(pixel)

x, y = 0, 0
spdX, spdY = 3, 1
counter = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    x += spdX
    y += spdY
    if x < 0 or x > SCREEN_W - scale * 10:
        spdX *= -1
    if y < 0 or y > SCREEN_H - scale * 10:
        spdY *= -1
    
    screen.fill((0,64,0))
    if spdX > 0:
        RT_draw(screen, actList[counter // 8 % 4], x, y, scale)
    else:
        RT_draw(screen, actList[- counter // 8 % 4], x, y, scale)
    counter += 1
    pygame.display.update()
    clock.tick(200)

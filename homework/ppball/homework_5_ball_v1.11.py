import pygame, sys, random, time
SCREEN_W, SCREEN_H = 1024, 600
BORDER_W = 10
ACCURACY = 4
G = 0.04
SPEED_Y_MAX = 8
def RT_show_txt(scr, txt, font, x, y, c):
    img = font.render(txt, True, c)
    scr.blit(img, (x, y))


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

class CLS_ball(object):
    def __init__(self, x, y, spdX, spdY, scale):
        self.x, self.y = x, y
        self.spdX, self.spdY = spdX, spdY
        self.scale = scale
        self.w, self.h = 0, 0
        self.interval = 8
        self.counter = 0
        self.picList = []
    def add_pic(self, pixel):
        self.picList.append(pixel)
        self.w = len(pixel[0]) * self.scale
        self.h = len(pixel) * self.scale
    def move(self):
        self.spdY += G
        if self.spdY > SPEED_Y_MAX:
            self.spdY = SPEED_Y_MAX
        self.x += self.spdX
        self.y += self.spdY
        if self.x < BORDER_W:
            self.spdX *= -1
            soundPong2.play()
        if self.y <= BORDER_W or self.y > SCREEN_H - self.h - BORDER_W:
            self.spdY *= -1
            soundPong2.play()
        self.out()
        self.collide(paddle)
    def draw(self, scr):
        RT_draw(scr, self.picList[int(self.counter) // self.interval % len(self.picList)], self.x, self.y, self.scale)
        self.counter += self.spdX * 0.25
    def out(self):
        if self.x > SCREEN_W:
            self.set_new_ball()
    def collide(self, paddle):
        if abs(self.x + self.w - paddle.x) <= ACCURACY:
            if paddle.y <= self.y + self.h//2 and paddle.y + paddle.h >= self.y - self.h//2:
                self.spdX *= -1
                soundPong4.play()
    def set_new_ball(self):
        self.x, self.y = 10, random.randint(10,300)
        self.spdX = random.random()*2 + 2
        self.spdY = random.random()*2 + 1

 
                


class CLS_paddle(object):
    def __init__(self, x, y, w, h, c = (200, 200, 0)):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.spdY = 0
        self.c = c
    def move(self):
        self.y += self.spdY
        if self.y < BORDER_W:
            self.y = BORDER_W
        if self.y > SCREEN_H - self.h - BORDER_W:
            self.y = SCREEN_H - self.h - BORDER_W
    def draw(self, scr):
        pygame.draw.rect(scr, self.c, (self.x, self.y, self.w, self.h), 0)

def draw_field(scr):
    c = pygame.color.THECOLORS['brown']
    pygame.draw.rect(scr, c, (0, 0, SCREEN_W, BORDER_W), 0)
    pygame.draw.rect(scr, c, (0, SCREEN_H - BORDER_W, SCREEN_W, BORDER_W), 0)
    pygame.draw.rect(scr, c, (0, 0, BORDER_W, SCREEN_W), 0)


# ----pygame init----
pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption('RT - PingPong Ball')
clock = pygame.time.Clock()
font64 = pygame.font.Font('simkai.ttf', 64)
# ----data init----
ballList = []
for i in range(100):
    ball = CLS_ball(10,random.randint(10,300),random.random()*16+8,random.random()*8+4,2)
    ballList.append(ball)
paddle = CLS_paddle(SCREEN_W - BORDER_W, 200, 10, 150)

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
for ball in ballList:
    ball.add_pic(pixel)

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
for ball in ballList:
    ball.add_pic(pixel)

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
for ball in ballList:
    ball.add_pic(pixel)

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
for ball in ballList:
    ball.add_pic(pixel)

soundPong1 = pygame.mixer.Sound('pong1.wav')
soundPong2 = pygame.mixer.Sound('pong2.wav')
soundPong3 = pygame.mixer.Sound('pong3.wav')
soundPong4 = pygame.mixer.Sound('pong4.wav')
soundPong5 = pygame.mixer.Sound('pong5.wav')
soundGo = pygame.mixer.Sound('readygo.wav')
pygame.mixer.music.load('plantzombie.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
soundGo.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                paddle.spdY = -2
            elif event.key == pygame.K_DOWN:
                paddle.spdY = 2
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                paddle.spdY = 0
    screen.fill((0, 64, 0))
    draw_field(screen)
    for ball in ballList:
        ball.move()
        ball.draw(screen)
    paddle.move()
    paddle.draw(screen)
    pygame.display.update()
    clock.tick(200)


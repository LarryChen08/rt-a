import pygame, sys, random, time
SCREEN_W, SCREEN_H = 1024, 600
BORDER_W = 10
ACCURACY = 4
G = 0
SPEED_Y_MAX = 4
def RT_show_txt(scr, txt, font, x, y, c):
    img = font.render(txt, True, c)
    scr.blit(img, (x, y))
def set_new_ball(ball,direc):
    ball.x, ball.y = 0 + SCREEN_W * (direc == -1), 10
    ball.spdX = (random.random()*8 + 2)*direc
    ball.spdY = random.random()*6 + 1


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
        if self.y <= BORDER_W or self.y > SCREEN_H - self.h - BORDER_W:
            self.spdY *= -1
            soundPong2.play()
        self.out()
        self.collide(paddle1,0)
        self.collide(paddle2,1)
    def draw(self, scr):
        RT_draw(scr, self.picList[int(self.counter) // self.interval % len(self.picList)], self.x, self.y, self.scale)
        self.counter += self.spdX * 0.25
    def out(self):
        if self.x > SCREEN_W:
            time.sleep(1)
            set_new_ball(ball,1)
        elif self.x + self.w< 0:
            time.sleep(1)
            set_new_ball(ball,-1)
    def collide(self, paddle, num):
        if abs(self.x + self.w * (1 - num) - paddle.x) <= ACCURACY:
            if paddle.y <= self.y + self.h//2 and paddle.y + paddle.h >= self.y - self.h//2:
                self.spdX *= -1
                soundPong4.play()

 
                


class CLS_paddle(object):
    def __init__(self, x, y, w, h, c = (200, 200, 0)):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.spdY = 0
        self.c = c
        self.accY = 0
        self.friction = 0.5
    def move(self):
        self.spdY += self.accY
        self.y += self.spdY
        if self.y < BORDER_W:
            self.y = BORDER_W
            self.spdY = 0
        if self.y > SCREEN_H - self.h - BORDER_W:
            self.y = SCREEN_H - self.h - BORDER_W
            self.spdY = 0
    def draw(self, scr):
        pygame.draw.rect(scr, self.c, (self.x, self.y, self.w, self.h), 0)

def draw_field(scr):
    c = pygame.color.THECOLORS['brown']
    pygame.draw.rect(scr, c, (0, 0, SCREEN_W, BORDER_W), 0)
    pygame.draw.rect(scr, c, (0, SCREEN_H - BORDER_W, SCREEN_W, BORDER_W), 0)
    RT_show_txt(scr, 'PT PINGPONG', font64, 300, 200, (255, 255, 0))


# ----pygame init----
pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption('RT - PingPong Ball')
clock = pygame.time.Clock()
font64 = pygame.font.Font('simkai.ttf', 64)
# ----data init----
ball = CLS_ball(10,10,6,4,3)
paddle1 = CLS_paddle(SCREEN_W - BORDER_W, 200, 10, 150)
paddle2 = CLS_paddle(0, 200, 10, 150)

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
                paddle1.accY = -0.2
            if event.key == pygame.K_w:
                paddle2.accY = -0.2
            elif event.key == pygame.K_DOWN:
                paddle1.accY = 0.2
            elif event.key == pygame.K_s:
                paddle2.accY = 0.2
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                paddle1.spdY = 0
                paddle1.accY = 0
            if event.key in (pygame.K_w, pygame.K_s):
                paddle2.spdY = 0
                paddle2.accY = 0
    screen.fill((0, 64, 0))
    draw_field(screen)
    ball.move()
    ball.draw(screen)
    paddle1.move()
    paddle1.draw(screen)
    paddle2.move()
    paddle2.draw(screen)
    pygame.display.update()
    clock.tick(200)


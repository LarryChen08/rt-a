import pygame, sys, time
def get_key_index(key, keyList):
    for i in range(len(keyList)):
        if key == ord(keyList[i]):
            return i
    return -1

def graph_note(graph_list):
    for i in range(len(graph_list)):
        if graph_list[i]:
            if i < 14:
                screen.blit(noteImg, (i * 30 + 2, 80))
                continue
            i += (i > 15) + (i > 18) + (i > 20)
            screen.blit(noteImg, ((i - 14) * 30 + 17, 15))

def play(rec_name_list, rec_start_list, rec_end_list, rec_play_list):
    t_0 = time.time()
    k = len(rec_name_list)
    time_end = max(rec_end_list)
    rec_graph_list = rec_play_list
    while True:
        t = time.time() - t_0
        if t > time_end:
            return
        for i in range(k):
            if rec_start_list[i] <= t and rec_play_list[i] == 0:
                soundList[rec_name_list[i]].play()
                rec_play_list[i] = 1
                rec_graph_list[i] = 1
            if rec_end_list[i] <= t and rec_graph_list[i] == 1:    
                rec_graph_list[i] = 0
        graph_note(rec_graph_list)





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
record = 0

# ----main loop----
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if record == 0:
                    print('----------')
                    rec_name_list = []
                    rec_start_list = []
                    rec_end_list = []
                    rec_play_list = []
                    timeStart = time.time()
                    record = 1
                elif record == 1:
                    print('************')
                    record = 0
            if event.key == pygame.K_p:
                print(record)
                play(rec_name_list, rec_start_list, rec_end_list, rec_play_list)
            i = get_key_index(event.key, keyList)
            if i >= 0:
                soundList[i].play()
                keyFlagList[i] = 1
                if record == 1:
                    rec_name_list.append(i)
                    rec_start_list.append(time.time()-timeStart)
                    rec_end_list.append(0)
                    rec_play_list.append(0)
        elif event.type == pygame.KEYUP:
            i = get_key_index(event.key, keyList)
            if i >= 0:
                keyFlagList[i] = 0
                if record == 1:
                    for j in range(len(rec_start_list) - 1, -1, -1):
                        if rec_name_list[j] == i:
                            end_index = j
                            break
                    rec_end_list[j] = time.time() - timeStart
                
                    
    screen.blit(pianoImg, (0,0))
    for i in range(len(keyFlagList)):
        if keyFlagList[i]:
            if i < 14:
                screen.blit(noteImg, (i * 30 + 2, 80))
                continue
            i += (i > 15) + (i > 18) + (i > 20)
            screen.blit(noteImg, ((i - 14) * 30 + 17, 15))
    pygame.display.update()


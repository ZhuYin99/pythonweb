
import pygame
from pygame.locals import *
from sys import exit
import numpy as np


background_image_filename = '/home/tarena/桌面/个人笔记/项目/五子棋/timg.jfif'
white_image = '/home/tarena/桌面/个人笔记/项目/五子棋/timg8.jfif'
black_image = '/home/tarena/桌面/个人笔记/项目/五子棋/timg7.jfif'

def checkIsWin(x,y,array):
    count1,count2,count3,count4 = 0,0,0,0
    i = x-1
    while(i>=0):
        if array[i][y] == 1:
            count1+=1
            i -= 1
        else:
            break
    i = x+1
    while i<13:
        if array[i][y] == 1:
            count1+=1
            i += 1
        else:
            break
    j =y-1
    while (j >= 0):
        if array[x][j] == 1:
            count2 += 1
            j -= 1
        else:
            break
    j = y + 1
    while j < 13:
        if array[x][j] == 1:
            count2 += 1
            j += 1
        else:
            break

    i,j = x-1,y-1
    while(i>=0 and j>=0):
        if array[i][j] == 1:
            count3 += 1
            i -= 1
            j -= 1
        else :
            break
    i, j = x + 1, y + 1
    while (i <= 12 and j <= 12):
        if array[i][j] == 1:
            count3 += 1
            i += 1
            j += 1
        else:
            break

    i, j = x + 1, y - 1
    while (i >= 0 and j >= 0):
        if array[i][j] == 1:
            count4 += 1
            i += 1
            j -= 1
        else:
            break
    i, j = x - 1, y + 1
    while (i <= 12 and j <= 12):
        if array[i][j] == 1:
            count4 += 1
            i -= 1
            j += 1
        else:
            break


    if count1>=4 or count2>=4 or count3 >= 4 or count4 >= 4:
        return True
    else:
        return False



pygame.init()
screen = pygame.display.set_mode((490, 557), 0, 32)
background = pygame.image.load(background_image_filename).convert()
white = pygame.image.load(white_image).convert_alpha()
black = pygame.image.load(black_image).convert_alpha()

screen.blit(background, (0,0))
font = pygame.font.SysFont("黑体", 40);

white_list = np.zeros((13,13))
black_list = np.zeros((13,13))

pygame.event.set_blocked([1,4,KEYUP,JOYAXISMOTION,JOYBALLMOTION,JOYBUTTONDOWN,JOYBUTTONUP,JOYHATMOTION])
pygame.event.set_allowed([MOUSEBUTTONDOWN,MOUSEBUTTONUP,12,KEYDOWN])

dot_list = [(52+i*32-white.get_width()/2,122+j*32-white.get_height()/2) for i in range(13 ) for j in range(13)]
start = True
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_r:
                screen.blit(background,(0,0))
                white_list = np.zeros((13,13))
                black_list = np.zeros((13, 13))
                pygame.event.set_blocked(
                    [1, 4, KEYUP, JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN, JOYBUTTONUP,
                     JOYHATMOTION])
                pygame.event.set_allowed([MOUSEBUTTONDOWN, MOUSEBUTTONUP, 12, KEYDOWN])
                dot_list = [(52 + i * 32 - white.get_width() / 2, 122 + j * 32 - white.get_height() / 2) for i in
                            range(13) for j in range(13)]
                start = True
                break
        if event.type == MOUSEBUTTONDOWN:

            # for item in dot_list:
            #     screen.blit(white, item)

            x,y = pygame.mouse.get_pos()
            if 42 <= x <= 446 and 112 <= y <= 516 and ((x - 52) % 32 <= 10 or (x - 52) % 32 >= 22) and (
                        (y - 122) % 32 <= 10 or (y - 122) % 32 >= 22):

                m = int(round((x-52)/32))
                n = int(round((y-112)/32))
                try:
                    if start:
                        start = not start
                        screen.blit(black, dot_list[13*m+n])
                        #print(m,n,'----------')
                        black_list[n][m] = 1
                        if checkIsWin(n,m,black_list):

                            screen.blit(font.render('GAME OVER,Black is win!', True, (0, 0, 0)), (80, 300))
                            pygame.event.set_blocked(
                                [1, 4, KEYUP, JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN, JOYBUTTONUP,
                                 JOYHATMOTION,MOUSEBUTTONDOWN,MOUSEBUTTONUP])
                            pygame.event.set_allowed(QUIT)

                    else:
                        start = not start
                        screen.blit(white, dot_list[13 * m + n])
                        #print(m, n, '----------')
                        white_list[n][m] = 1
                        if checkIsWin(n,m,white_list):
                            screen.blit(font.render('GAME OVER,White is win!', True, (0, 0, 0)), (80, 300))
                            pygame.event.set_blocked(
                                [1, 4, KEYUP, JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN, JOYBUTTONUP,
                                 JOYHATMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP])
                            pygame.event.set_allowed(QUIT)



                    dot_list[13*m+n] = ''

                except :
                    pass

        #         print('This true')


        #     print('---------------black------------------')
        #     for line in black_list:
        #         print(line )
        #     print('---------------white------------------')
        #     for line in white_list:
        #         print(line)


        # m,n = (x-20)%32,(y-90)%32


        # x -= white.get_width()/2
        # y -= white.get_height()/2
        # screen.blit(white,(x,y))

        # # print(dot_list[m*15+n+1])


    pygame.display.update()



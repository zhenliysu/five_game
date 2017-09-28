# -*- coding: utf-8 -*-

import sys
import pygame
import random
from random import *
from numpy import *
#import time
from pygame.locals import *
#from pygame.transform import *

#white = 255,255,255
#blue = 0,0,200
#screen = pygame.display.set_mode((600,500))

#myfont = pygame.font.Font(None,60)
#textImage = myfont.render("Hello Pygame", True, white)
#redRect=redimg.get_rect()
#blueRect=blueImage.get_rect()

FPS = 4
mainClock = pygame.time.Clock()
#position=(1,1)
#position1=(100,1)


pygame.init()
BACKGROUNDCOLOR = (240, 255, 255) 

boardImage=pygame.image.load('chessboard.png')
boardimg = pygame.transform.smoothscale(boardImage, (440,440))
boardwidth,boardheight=boardimg.get_size()

redImage=pygame.image.load('red.png')
redimg = pygame.transform.scale(redImage, (32,32))

blueImage=pygame.image.load('blue.png')
blueimg = pygame.transform.scale(blueImage, (32,32))

my_font=pygame.font.SysFont(None,30)
you=my_font.render('you', True, (255, 0, 0))
computer=my_font.render('computer', True, (0, 0, 200))
youturn=my_font.render('you turn', True, (255, 0, 0))
computerturn=my_font.render('computer turn', True, (0, 0, 200))
restart1=my_font.render('PK', True, (0, 0, 0))
my_font=pygame.font.SysFont(None,25)
Email=my_font.render('zhenli_ysu@126.com', True, (0, 0, 0))




windowSurface=pygame.display.set_mode((boardwidth,boardheight+80))
def init_chessboard():

    pygame.display.set_caption('AI五子棋') 
    windowSurface.fill(BACKGROUNDCOLOR)

    windowSurface.blit(boardimg,(0,80))
    windowSurface.blit(redimg,(1,1))
    windowSurface.blit(you,(40,4))
    windowSurface.blit(blueimg,(100,1))
    windowSurface.blit(computer,(140,4))
    windowSurface.blit(Email,(270,4))
def chessshow(row,column,player):
    row1=row*40+24
    column1=column*40+104
    if player==-1:
        windowSurface.blit(redimg,(row1,column1))
    else:
        windowSurface.blit(blueimg,(row1,column1))

def showdemo():
    for i in range(10):
        for j in range(10):
	    windowSurface.blit(boardimg,(0,80))
	    chessshow(i,j,0)
	    pygame.display.update()
            mainClock.tick(FPS)
def firstplayer():

    if ((random.randint(-10,10))>0):
	ret=-1
	
    else:
   	ret=1

    return ret

def informationshow(mode):
    if mode==-1:
	pygame.draw.rect(windowSurface, (240, 255, 255), (0, 40, 150, 40))
	windowSurface.blit(youturn,(1,40))
    elif mode==1:
	pygame.draw.rect(windowSurface, (240, 255, 255), (0, 40, 150, 40))
	windowSurface.blit(computerturn,(1,40))

def restart():
    pygame.draw.rect(windowSurface, (200,0, 0), (200, 40,100,30))
    windowSurface.blit(restart1,(235,45))	

playing=False

#print chess_state

init_chessboard()

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
	    pygame.quit()
            sys.exit()
	elif event.type==pygame.MOUSEBUTTONDOWN:
	    point_x=event.pos[1]
	    point_y=event.pos[0]

	    if point_x>39 and point_x<71 and point_y>199 and point_y<301:
		chess_state=zeros((10,10))		
		init_chessboard()
		playing=True
		round_index=0

		player1=firstplayer()

		player2=-1*player1

	    if playing==True:
		informationshow(player1)
		if point_x>100 and point_x<500 and point_y>20 and point_y<420:
		    
		    index_x=int((point_x-100)/40)
		    index_y=int((point_y-20)/40)
		    if (round_index%2)==0 and chess_state[index_x][index_y]==0:
			chessshow(index_y,index_x,player1)
			chess_state[index_x][index_y]=player1
			round_index=round_index+1
			informationshow(player2)
		    if  (round_index%2)==1 and chess_state[index_x][index_y]==0:
			chessshow(index_y,index_x,player2)
			chess_state[index_x][index_y]=player2
			round_index=round_index+1
			informationshow(player1)

		




    restart()
    pygame.display.update()
    
    mainClock.tick(FPS) 

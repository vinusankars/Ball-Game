import pygame,sys,random
from pygame.locals import *
from math import *

#classes ===============================================
class vector():
    x,y=10**-10,0
    def __init__(self,x=0,y=0,o=45):
        self.x=x
        self.y=y
        self.o=o
    o=atan(float(y)/x)*180.0/pi
        
class ball(pygame.sprite.Sprite):
    v=vector()
    def __init__(self,r,x,y,i):
        self.r=r
        self.x=x
        self.y=y
        self.i=pygame.image.load(i).convert_alpha()
        self.i=pygame.transform.scale(self.i,(100,100))

    
        

#Main Variables ========================================
winwidth=1120
winheight=920
fps=40

#Colors ================================================
blue=(0,0,255)
red=(255,0,0)
white=(255,255,255)
black=(0,50,100)

pygame.init()
pygame.mouse.set_visible(0)
disp=pygame.display.set_mode((winwidth,winheight))
pygame.display.set_caption('The Ball Game')

#draw ==================================================
disp.fill(white)
ball1=ball(50,0,0,'ball11.png')
ball2=ball(50,0,0,'ball10.png')
background=pygame.image.load('image.png').convert_alpha()
background=pygame.transform.scale(background,(winwidth,winheight+400))

def draw():
    disp.blit(background,(0,0))
    disp.blit(ball1.i,(ball1.x-50,ball1.y-50))
    disp.blit(ball2.i,(ball2.x-50,ball2.y-50))
    pygame.draw.rect(disp,black,(0,0,10,winwidth))
    pygame.draw.rect(disp,black,(0,0,winwidth,10))
    pygame.draw.rect(disp,black,(0,winheight-10,winwidth,winheight))
    pygame.draw.rect(disp,black,(winwidth-10,0,winwidth,winwidth))
    
    ball1.v.x=velocity*cos(ball1.v.o*pi/180.0)
    ball1.v.y=velocity*sin(ball1.v.o*pi/180.0)
    ball2.v.x=velocity*cos(ball2.v.o*pi/180.0)
    ball2.v.y=velocity*sin(ball2.v.o*pi/180.0)

#ball variables ========================================
e=1

#ball main =============================================
ball1.x,ball1.y=50,50
ball2.x,ball2.y=770,470
velocity=10

# main game loop =======================================
while True:
    
    fpsclock=pygame.time.Clock()
    draw()       
    for event in pygame.event.get():   
        if event.type==KEYDOWN:
            
            if event.key==K_RIGHT:
                if ball1.v.y<0:
                    ball1.v.o-=20
                elif ball1.v.y>0:
                    ball1.v.o+=20
                else:
                    ball1.v.x=velocity
                    ball1.v.y=0
                    ball1.v.o=0
                
            if event.key==K_LEFT:
                if ball1.v.y<0:
                    ball1.v.o+=20
                elif ball1.v.y>0:
                    ball1.v.o-=20
                else:                    
                    ball1.v.x=-velocity
                    ball1.v.y=0
                    ball1.v.o=180
            if event.key==K_UP:
                if ball1.v.x<0:
                    ball1.v.o-=20
                elif ball1.v.x>0:
                    ball1.v.o+=20
                else:                    
                    ball1.v.y=-velocity
                    ball1.v.x=0
                    ball1.v.o=90
            if event.key==K_DOWN:
                if ball1.v.x<0:
                    ball1.v.o+=20
                elif ball1.v.x>0:
                    ball1.v.o-=20
                else:
                    ball1.v.y=velocity
                    ball1.v.x=0
                    ball1.v.o=270
    #-----------------------------------            
                
            if event.key==K_d:
                if ball1.v.y<0:
                    ball1.v.o-=5
                elif ball1.v.y>0:
                    ball1.v.o+=5
                else:
                    ball1.v.x=1
                    ball1.v.y=10**-10
                
            if event.key==K_a:
                if ball1.v.y<0:
                    ball1.v.o+=5
                elif ball1.v.y>0:
                    ball1.v.o-=5
                else:
                    ball1.v.x=-1
                    ball1.v.y=10**-10
            if event.key==K_w:
                if ball1.v.x<0:
                    ball1.v.o-=5
                elif ball1.v.x>0:
                    ball1.v.o+=5
                else:
                    ball1.v.y=-1
                    ball1.v.x=10**-10
            if event.key==K_s:
                if ball1.v.x<0:
                    ball1.v.o+=5
                elif ball1.v.x>0:
                    ball1.v.o-=5
                else:
                    ball1.v.y=1
                    ball1.v.x=10**-10
        #-----------------------------------
                
        '''if event.type==KEYUP:
            if event.key==K_RIGHT or event.key==K_LEFT:
                speedx1=0
            if event.key==K_UP or event.key==K_DOWN:
                speedy1=0
            if event.key==K_d or event.key==K_a:
                speedx2=0
            if event.key==K_w or event.key==K_s:
                speedy2=0 '''
        
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
            
    ball1.x+=ball1.v.x
    ball1.y+=ball1.v.y
    ball2.x+=ball2.v.x
    ball2.y+=ball2.v.y
    
    '''if ball1.x>1090 or ball1.x<30:
        speedx1=int(-speedx1*e)
    if ball1.y>890 or ball1.y<30:
        speedy1=int(-speedy1*e)
    if ball2.x>1090 or ball2.x<30:
        speedx2=int(-speedx2*e)
    if ball2.y>890 or ball2.y<30:
        speedy2=int(-speedy2*e)'''
    
    pygame.display.update()
    fpsclock.tick(fps)


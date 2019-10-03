from pygame import *
from math import *
from random import *
import os
#Unit Converter
init()
unitnum=0
mx,my=mouse.get_pos()
screen = display.set_mode((1136,640))
numshiftlist=[')','!','@','#','$','%','^','&','*','(']
comicFont = font.SysFont("Comic Sans MS", 58)
typing=False
optionrects=[]
files=[]
for y in range(50,601,150):
    optionrect=Rect(0,y,400,100)
    optionrects.append(optionrect)
    draw.rect(screen,(255,255,255),optionrect) # option boxes
draw.rect(screen,(255,255,255),(420,50,700,100))#the box
for x in range(420,841,150):
    for y in range(160,481,140):
        draw.rect(screen,(0,255,255),(x,y,120,120))
draw.rect(screen,(0,255,255),(960,200,160,120))#
draw.rect(screen,(255,0,255),(960,340,160,120))#enter
draw.rect(screen,(255,255,0),(960,480,160,120))#scratchpad
pagerects=[]
for x in range(0,361,60):
    pagerect=Rect((x,152,45,45))
    pagerects.append(pagerect)
    draw.rect(screen,(255,255,0),pagerect)

listdir=os.listdir()
for file in listdir:
            if file.endswith('.txt'):
                file=file[:file.find('.')]
                files.append(file)
print(files)
units={}
for i in range(len(files)):
    units[files[i]]=open(str(files[i])+'.txt','r').read().strip().split('\n')
print(units)
#covertrect=(x,y,side,side)

running =True
while running:                   
    for e in event.get():       
        if e.type == QUIT:
            running = False
        if e.type == KEYDOWN:
            if typing :
                if key.get_mods()& KMOD_CAPS and not key.get_mods()& KMOD_SHIFT and e.key >96 and e.key <123:                
                    msg+=chr(e.key-32)
                elif key.get_mods()& KMOD_SHIFT and not key.get_mods()& KMOD_CAPS and e.key >96 and e.key <123:
                    msg+=chr(e.key-32)
                elif key.get_mods()& KMOD_SHIFT and e.key >47 and e.key<60:
                    msg+=numshiftlist[e.key-48]
                elif e.key==32:
                    msg+=' '
                elif e.key>32 and e.key<126:                
                    msg+=chr(e.key)
                elif e.key==8:
                    msg=msg[:-1]
    if e.type==MOUSEBUTTONDOWN:
        for i in range(len(pagerects)):
            if pagerects[i].collidepoint(mx,my) :
                unitnum=i
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()  
    draw.rect(screen,(255,255,255),optionrects[0])
    txtPic = comicFont.render((files[unitnum]), True, (255,0,0))
    screen.blit(txtPic,optionrects[0])   
    display.flip()  
quit()
##            unitname=units[files[i][0]]   
##            toconvert=units[files[i][1]]
##            fromconvert=units[files[i][2]]

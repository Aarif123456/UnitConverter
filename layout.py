#Abdullah Arif
#Paint Project
#importing
from pygame import *
from random import*
from math import*
import os
#setup
display.set_caption("One piece Paint")
screen = display.set_mode((1024,720))
screen.fill((0,255,255))
init()
comicFont = font.SysFont("Comic Sans MS", 15)
#preset variables
FULL=False#starts off not Fullscreen
typing=False#You can use keyboard shortkey does not automaticaly type
palettenum=0#first pallete
oldpalettenum=0
drawcol=(255,0,0)
counts=[]
images=[]
listpics=[]
col=(0,0,0)
toolnewpage=0
toolpage=0
toolnum=0
toolnewnum=0
sublistdir=[]
imageslist={}
trails=[]
names={}
canvassurfacelist=[]
canvaspagenum=0
magicmode=False
mx,my=mouse.get_pos()
dx,dy=mx,my
olddx,olddy=mx,my
mb=mouse.get_pressed()
paletteimages=[]
oldmusicnum=1
musicnum=1
radius=20
fill=1
tool='pencil'
#---------------------------------------------------------------------------------------------------------------------------------------
maindirs=os.listdir('paint')
for i in range(5):#loop for amount of files             
    paletteimages.append(image.load('paint/1 palette/palette'+str(i+1)+'.png'))
for m in range (2,8):#to get all the images
    subdir=os.listdir('paint/'+str(maindirs[m]))
    filecount=0
    tempfilenames=[]
    tempimages=[]
    for file in subdir:
        if file.find('.')>0:
            filecount-=1
    if filecount!=0:
        subdir=subdir[:filecount]#I am assuming the unwanted files don't begin with numbers like Thumbs.db    
    for s in range(len(subdir)):
        listdir=os.listdir('paint/'+str(maindirs[m]+'/'+str(subdir[s])))#list files and folders
        count=0#reset every loop for sub directory
        listpics=[]
        images=[]
        subfilenames=[]        
        for file in listdir:
            if file.endswith('.png')or file.endswith('.jpg'):#want to only count all the pictures
                count+=1
                listpics.append(file)#puts all the images in one file
                if file.find('.')>0:
                   subfilename=file[:file.find('.')]
                   subfilenames.append(subfilename)                   
        tempfilenames.append(subfilenames)#used to get a list of names in the subdirectory
        for i in range(count):#loop foramount of files             
            images.append(image.load('paint/'+str(maindirs[m])+'/'+str(subdir[s])+'/'+listpics[i]))#use to load all needed images            
        tempimages.append(images)
        #using / insead of \ because it works and doesn't mess with strings
    num=maindirs[m].find(' ') 
    imageslist[str(maindirs[m])[num+1:]]=tempimages
    names[str(maindirs[m])[num+1:]]=tempfilenames
#one list for names other for actual images
screen.blit(imageslist['design'][2][0],(300,0))
paletterect=Rect(500,580,145,145)
canvasrect=draw.rect(screen,(255,255,255),(100,100,680,480),0)
#making rects rects(x,y,horizontal length,vertical length)
ctools=[]
for x in range(122,258,45):#undo redo load save fullscreen clear magnify reduce
    for y in range(0,51,50):
        draw.rect(screen,(0,0,0),(x,y,40,40))
        ctools.append(Rect(x,y,40,40))
undorect=ctools[0]
redorect=ctools[1]
loadrect=ctools[2]
saverect=ctools[3]
fullrect=ctools[4]
clearrect=ctools[5]
magnifyrect=ctools[6]
reducerect=ctools[7]
"tool page change rects"
toolnextrect=Rect(100,0,20,15)
draw.rect(screen,(0,0,255),toolnextrect)
toolbackrect=Rect(0,0,20,15)    
draw.rect(screen,(0,0,255),toolbackrect)
toolmenurect=(21,0,78,15)
draw.rect(screen,(0,0,255),toolmenurect)
toolpagerects=[]
x=-20
for i in range(6): 
    x+=20
    toolpagerect=(x,20,15,15)
    toolpagerects.append(Rect(toolpagerect))
    draw.rect(screen,(0,0,255),toolpagerect)
'tool name box'
draw.rect(screen,(0,0,0),(0,37,120,20))
'tool boxes'  
toolsrects=[]
y=18
for i in range (6):
    y+=82
    toolsrects.append(Rect((0,y,80,70)))
def toolpagechange():   
    for i in range(len(imageslist['tools'][toolnewpage])):        
        draw.rect(screen,(255,255,255),(toolsrects[i])) 
        screen.blit(imageslist['tools'][toolnewpage][i],toolsrects[i])
def palettechange(palettenum):        
    draw.rect(screen,(0,255,255),paletterect)
    screen.blit(paletteimages[palettenum],paletterect)
#create tool select function
'tool info'
toolinforect=Rect(0,690,500,30)
draw.rect(screen,(0,0,0),(toolinforect))
'background box'
backgroundrect=Rect(794,0,230,290)
draw.rect(screen,(255,0,0,),(backgroundrect))
'stampbox'
stamprect=(794,300,230,420)
draw.rect(screen,(255,0,0,),(stamprect))#minimium 200,380
#music box
'main box'
musicmainrect=Rect(600,0,130,100)
draw.rect(screen,(0,255,0),(musicmainrect))
'play button'
playrect=Rect(605,10,55,55)
draw.rect(screen,(0,0,0),(playrect))
'stop button'
stoprect=Rect(670,10,55,55)
draw.rect(screen,(0,0,0),(stoprect))
'back arrow'
musicbackrect=Rect(600,75,40,20)
draw.rect(screen,(255,0,0),(600,75,40,20))
'next arrow'
musicnextrect=Rect(690,75,40,20)
draw.rect(screen,(255,0,0),(musicnextrect))
'volume add'
volumeaddrect=Rect(645,75,15,20)
draw.rect(screen,(0,0,255),(645,75,15,20))
'volume minus'
volumeminusrect=Rect(670,75,15,20)
draw.rect(screen,(0,0,255),(670,75,15,20))
#canvas fuction boxes
'magnify'
magnifyrect=Rect(0,58,50,40)
draw.rect(screen,(255,0,255),(0,58,50,40))
'reduce'
reducerect=Rect(55,58,50,40)
draw.rect(screen,(255,0,255),(55,58,50,40))
'add canvas'
addcanvasrect=Rect(0,585,80,40)
draw.rect(screen,(0,0,255),(0,585,80,40))
'delete canvas'
deletecanvasrect=Rect(0,635,80,40)
draw.rect(screen,(0,0,255),(0,635,80,40))
'forward canvas rect'
forwardcanvasrect=Rect(100,585,80,40)
draw.rect(screen,(0,0,255),(100,585,80,40))
'back canvas'
backcanvasrect=Rect(190,585,80,40)
draw.rect(screen,(0,0,255),(190,585,80,40))
'lighten canvas '
lightencanvas=Rect(100,635,80,40)
draw.rect(screen,(0,0,255),(100,635,80,40))
'darken canvas '
darkencanvas=Rect(190,635,80,40)
draw.rect(screen,(0,0,255),(190,635,80,40))
'magic mode'
magicrect=Rect(280,635,80,40)
draw.rect(screen,(0,0,255),(280,635,80,40))
#palette stuff
'palette back'
palettebackrect=Rect(370,635,50,40)
draw.rect(screen,(0,0,255),(370,635,50,40))
'palette next'
palettenextrect=Rect(430,635,50,40)
draw.rect(screen,(0,0,255),(430,635,50,40))
'canvas surface'
canvassurface=screen.subsurface(canvasrect)
canvascopy=canvassurface.convert().copy()
canvassurfacelist.append(canvassurface.convert())
canvassurfacelist[canvaspagenum].set_colorkey((0,0,0))
screen.blit(canvassurfacelist[canvaspagenum],canvasrect)
canvassurfacelist[canvaspagenum].set_alpha(255)
#defining tools
size = 10
def pencil(surface,col,x,y,oldx,oldy):    
    draw.line(surface,col,(oldx,oldy),(x,y),3)
#eraser at the bottom
def eyedrop():    
    global drawcol
    drawcol=screen.get_at((mx,my))
def tonechanger(surface):
    tcol=screen.get_at((mx,my))
    if min(tcol)>10:
        ncol=(tcol[0]-5,tcol[1]-5,tcol[2]-5)    
        time.wait(15)        
        draw.circle(surface,ncol,(mx-size//2,my-size//2),size)
def text(surface,x,y,msg,col):#cahnge so it works with magic mode
    comicFont = font.SysFont("Comic Sans MS", size)
    txtpic=comicFont.render (msg, False, (col))#getting mx,my seperatly to avoid bracket
    draw.rect(surface,(255,255,255),(x,y,txtpic.get_width(),txtpic.get_height()))#create rect and text on new surface until enter pressed
    surface.blit(txtpic,(x,y))#300,300 replaced by mx,my corralation to middle
def fillbucket(surface,col):#not going to be in magic mode becuase it  would take forever
    fillpos=[(dx,dy)]
    oldcol=surface.get_at((dx,dy))
    if oldcol!=col:
        while len(fillpos)>0:
            x,y = fillpos.pop()                                          
            if surface.get_at((x,y))==oldcol:
                surface.set_at((x,y),col)
                fillpos+=[(x+1,y), (x-1,y),(x,y+1),(x,y-1)]
numshiftlist=[')','!','@','#','$','%','^','&','*','(']
msg=''
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
#higlighter blit on cover    
def circlebrush(surface,col,fill,size,x,y):
    draw.circle(surface,(col),(x,y),size,fill)
def rectbrush(surface,col,fill,size,x,y):
    draw.rect(surface, (col),(x,y,size,size),fill)
def linebrush(surface,col,size,x,y,oldx,oldy):
    draw.line(surface,(col),(x,y),(oldx,oldy),size)
def explosionbrush(surface,col,size,x,y):
    draw.line(surface,(col),(x,y),(x+randint(-size,size),y+randint(-size,size)))
#def stampbrush(surface,category,stamp,width):
def colormasher(surface):
    colorrect=Rect(dx-size//2,dy-size//2,size,size)
    col=transform.average_drawcolor(screen,drawcolorrect)
    draw.rect(surface,col,colorrect)
#if sticky mode on dx,dy=dx//10,dy//10
#alpha for highlighter 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ellipse(surface,col,fill,x,y,startx,starty):    
    if abs(x-startx)>size*2 and abs(y-starty)> size*2:
        draw.ellipse(surface,col,(min(x,startx),min(y,starty),abs(x-startx),abs(y-starty)),fill) 
    else:
        draw.ellipse(surface,col,(min(mx,startx),min(my,starty),abs(mx-startx),abs(my-starty)),0)
    #perfect use circle
perfect=False
def rect(surface,col,startx,starty,x,y,fill):    
    if perfect:        
        draw.rect(surface,col,((startx),(starty),(x-startx),(y-starty)),fill)
    else:
        draw.rect(surface,col,((startx),(starty),((x-startx+y-starty)//2),((x-startx+y-starty)//2)),fill)
def polygon(surface,polylist,col,fill):    
    draw.polygon(surface,(0,0,0),polylist,fill)
def line(surface,start,x,y,col):    
    draw.line(surface,(col),start,(x,y), size)
def aaline(surface,start,x,y,col):    
    draw.aaline(surface,(col),start,(x,y))
#perfect ratio
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#category spray
speed=10
def spraycircle(surface,x,y,size,radius,sprayshapecircle,col):#if sprayshapecircle: True or False
    global speed
    for i in range (speed):
        xx=x+randint(-radius,radius)
        yy=y+randint(-radius,radius)            
        if ((xx-x)**2+(yy-y)**2)<radius**2:#equation of circle
            if sprayshapecircle:
                draw.circle(surface,col,(x,y),size)
            else:
                draw.rect(surface,col,(x,y,size,size))                    
def spraysquare(surface,x,y,size,radius,sprayshapecircle,col):
    for i in range (speed):
        x=dx+randint(-radius,radius)
        y=dy+randint(-radius,radius)
        if sprayshapecircle:
            draw.circle(screen,col,(x,y),size)
        else:
            draw.rect(screen,col,(x,y,size,size))
def sprayrain(surface,x,y,size,col):
    for i in range (speed):
        x=mx+randint(-radius,radius)
        y=my+randint(-radius,radius)
        draw.line(screen,col,(x,y),(x+size,y+size))
def sprayshapecirclerect():
    global sprayshapecircle
                 
    if sprayshapecircle:
        sprayshapecircle==False
        time.wait(100)
    else:
        sprayshapecircle==True
        time.wait(100)
def sprayspeed():
    global speed
    if mb[0]==1:
        speed+=1
    if mb[2]==1:
        speed=max(speed-1,1)



def regtoolselection(toolpagenum,toolnum,color):
    toolselectionlist=[]
    if canvasrect.collidepoint(x,y)==True:        
        toolselectionlist=[[pencil(canvassurfacelist[canvaspagenum],drawcolor,dx,dy,olddx,olddy),circlebrush(canvassurfacelist[canvaspagenum],(255,255,255),fill,size,dx,dy),eyedrop(),
    tonechanger(canvassurfacelist[canvaspagenum]),text(canvassurfacelist[canvaspagenum],dx,dy,msg,drawcolor),fillbucket(canvassurfacelist[canvaspagenum],drawcolor)],
    [circlebrush(canvassurfacelist[canvaspagenum],
    (drawcolor),fill,size,dx,dy),rectbrush(canvassurfacelist[canvaspagenum],(drawcolor),fill,size,dx,dy),linebrush(canvassurfacelist[canvaspagenum],(drawcolor),size,dx,dy,olddx,olddy),
    explosionbrush(canvassurfacelist[canvaspagenum],(drawcolor),size,dx,dy),stampbrush(canvassurfacelist[canvaspagenum],category,stamp,width),drawcolormasher()],[circlebrush(
    coverlist[canvaspagenum],(drawcolor),fill,size,dx,dy),rectbrush(coverlist[canvaspagenum],(drawcolor),fill,size,dx,dy),linebrush(coverlist[canvaspagenum],drawcolor,size,dx,dy,olddx,olddy),
    explosionbrush(coverlist[canvaspagenum],(drawcolor),size,dx,dy),stampbrush(coverslist[canvaspagenum],category,stamp,width)],[ellipse(drawcolor),rect(drawcolor),
    polygon(canvassurfacelist[canvaspagenum],polylist,drawcolor,fill),line(canvassurfacelist[canvaspagenum],start,dx,dy,drawcolor),aaline(canvassurfacelist[canvaspagenum],start,x,y,drawcolor)],
    [spraycircle(canvassurfacelist[canvaspagenum],dx,dy,size,radius,sprayshapecircle,drawcolor),spraysquare(canvassurfacelist[canvaspagenum],dx,dy,size,radius,sprayshapecircle,drawcolor),
     sprayrain(canvassurfacelist[canvaspagenum],dx,dy,speed,size,drawcolor)]]
        global tool    
        tool=toolselectionlist[toolpagenum,toolnum]
drawcolor=(0,0,0)
toolpagenum=1
#print(toolselectionlist[toolpage][toolnum])   
#transform.smoothscale()
toolpagechange()
palettechange(palettenum)
running =True
while running:                   
    for e in event.get():       
        if e.type == QUIT:     
            running = False
        if e.type==MOUSEBUTTONDOWN:            
            copy=canvassurface.copy()
            startx,starty = e.pos
            start=e.pos
            if e.button == 4:
               size += 1
            if e.button == 5:
               if size!=1:               
                   size -= 1
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            if toolnextrect.collidepoint(mx,my)==True:#try to make a function so it can be used on other menu too
                if toolnewpage!=5:
                    toolnewpage+=1
            if toolbackrect.collidepoint(mx,my)==True:
                if toolnewpage !=0:
                    toolnewpage-=1
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            for i in range (len(toolpagerects)):
                if toolpagerects[i].collidepoint(mx,my)==True:                
                    toolnewpage=i
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            if toolpage!=toolnewpage:#used to make sure picture are blitted in time 
                toolpagechange() 
                toolpage=toolnewpage
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            if palettenextrect.collidepoint(mx,my)==True:
                if palettenum!=4:
                    palettenum+=1
            if palettebackrect.collidepoint(mx,my)==True:
                if palettenum!=0:
                    palettenum-=1
            if palettenum!=oldpalettenum:
                oldpalettenum=palettenum
                palettechange(palettenum)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            if magicrect.collidepoint(mx,my)==True:
                if magicmode:
                    magicmode=False
                else:
                    magicmode=True
            if addcanvasrect.collidepoint(mx,my)==True:                
                canvassurface=screen.subsurface(canvasrect)                
                canvassurfacelist.append(canvassurface.convert())
                canvassurfacelist[len(canvassurfacelist)-1].fill((255,255,255))
            if deletecanvasrect.collidepoint(mx,my)==True:
                if len(canvassurfacelist)>1:                    
                    del canvassurfacelist[canvaspagenum]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
            else:
                if e.key ==K_f and FULL==False:#turns on fullscreen by pressing f.                    
                    init()
                    copy=screen.copy()
                    display.set_mode((1024,720), FULLSCREEN)
                    screen.blit(copy,(0,0))
                    FULL=True
                if e.key==K_ESCAPE and FULL==True:#turns off fullscreen by pressing Esc
                    init()
                    copy=screen.copy()                    
                    display.set_mode((1024,720))
                    display.set_caption("One piece Paint")
                    screen.blit(copy,(0,0))
                    FULL=False
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#music
    if musicnum!=oldmusicnum:
        init()
        mixer.music.load('paint/4 Music box/Songs/'+str(musicnum)+'.ogg')
        mixer.music.play(-1)
        oldmusicnum=musicnum
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    dx,dy=mx-100,my-100
    draw.rect(screen,drawcol,(735,0,55,20))#visual representation of chosen drawcolor
    draw.rect(screen,(0,0,0),(735,0,55,20),1)#outline for box
    r=drawcol[0]
    g=drawcol[1]
    b=drawcol[2]
    draw.rect(screen,(0,255,0),(280,590,215,40))#box get rederawn every time so  blitted text stays clear and doesn't right on it self    
    mposPic = comicFont.render ('screen mouse pos:'+str(mx) +','+str(my), True, (0,0,0))#getting mx,my seperatly to avoid bracket
    canvasmposPic=comicFont.render ('canvas mouse pos:'+str(mx-100) +','+str(my-100), True, (0,0,0))#add if statement about canvas collidepoint  
    '''for i in range(5):
        txtpic=comicFont.render(txtstr[i],True,(0,0,0))
        screen.blit(txtpic,txtpiclocs[i])
        draw.rect(screen,(0,255,255),((txtpiclocs),(txtpicrects)))'''#txtstr txtpiclocs txtpicrects
    screen.blit(canvasmposPic,(280,610))
    screen.blit(mposPic,(280,590))
    screen.blit((canvascopy),(canvasrect))
    screen.blit(canvassurfacelist[canvaspagenum],canvasrect)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    dx,dy=mx-100,my-100       
    if magicmode==True:        
        for col in trails:            
            if  col[2]!=drawcol[0]:
                if col[2]>drawcol[0]:
                    col[2]-=1
                if col[2]<drawcol[0]:
                    col[2]+=1            
            if col[3]!=drawcol[1]:
                if  col[3]!=drawcol[1]:
                    if col[3]>drawcol[1]:
                        col[3]-=1
                    if col[3]<drawcol[1]:
                        col[3]+=1
            if col[4]!=drawcol[2]:
                if  col[4]!=drawcol[2]:
                    if col[4]>drawcol[2]:
                        col[4]-=1
                    if col[4]<drawcol[2]:
                        col[4]+=1                
            draw.line(canvassurfacelist[canvaspagenum],(col[2],col[3],col[4]),(col[5],col[6]),col[:2],1)    
    if mb[0]==1:         
        if paletterect.collidepoint(mx,my)==True :
            drawcol=screen.get_at((mx,my))
            trails=[]               
        if tool=="pencil":
            #mx,my=mouse.get_pos()                      
            if magicmode==True:                
                trails.append([dx,dy,randint(0,255),randint(0,255),randint(0,255),olddx,olddy,surface,size,radius,sprayshapecircle])
            else:
                draw.line(canvassurfacelist[canvaspagenum],drawcol,(olddx,olddy),(dx,dy),1)
    if toolpage==5:#making it a function gives some errors plus there is no point since it is only being used once
        screen.set_clip(canvasrect)
        if mb[0]==1:#select if category crop
            angle=0                  
            croprect=Rect(startx,starty,mx-startx,my-starty)                
            croprect.normalize()
            cropselected=screen.subsurface(croprect).copy()
            draw.rect(screen,(0,0,0),croprect,1)
            cx,cy=cropselected.get_size()
        if mb[2]==1:
            if tool=='cropmove':
                screen.blit(cropcopy,(canvasRect))  
                draw.rect(screen,(255,255,255),(croprect))                          
                screen.blit(cropselected,(mx-cx/2,my-cy/2))
                croprect=Rect(mx-cx/2,my-cy/2,cx,cy)                    
                cropcopy = canvassurface.copy()                        
                time.wait(200)
            if tool=='cropcopy':
                screen.blit(copy,(canvasrect))
                screen.blit(cropselected,(mx-cx/2,my-cy/2))
                time.wait(200)
            if tool=='crop':
                draw.rect(screen,(255,255,255),canvasrect)
                screen.blit(cropselected,(croprect))
                cropcopy = canvassurface.copy()                    
            if tool=='croprotate':
                screen.blit(cropcopy,(canvasRect))  
                draw.rect(screen,(255,255,255),(croprect))
                cropselected=transform.rotate(cropselected,90)
                screen.blit(cropselected,(croprect))   
                time.wait(200)
            if tool =='cropvertical':
                screen.blit(cropcopy,(canvasRect))  
                draw.rect(screen,(255,255,255),(croprect))
                cropselected=transform.flip(cropselected, False, True)
                screen.blit(cropselected,(croprect))   
                time.wait(200)
            if tool =='crophorizontal':
                screen.blit(cropcopy,(canvasrect))  
                draw.rect(screen,(255,255,255),(croprect))
                cropselected=transform.flip(cropselected, True, False)
                screen.blit(cropselected,(croprect))   
                time.wait(200)
        screen.set_clip(None)        
        tool=regtoolselection(0,0,drawcolor)
            
    olddx,olddy,=dx,dy    
    display.flip()
font.quit()
del comicFont
quit() 

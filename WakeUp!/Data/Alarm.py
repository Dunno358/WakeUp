import pygame
from pygame.locals import *
import time
import os
from datetime import datetime

print(50*'*','Starting Alarm!',50*'*')

print("Initializing Data...")
pygame.init()
pygame.mixer.init()
running = True
isSound = True
clock = pygame.time.Clock()
disks="ABEFGHIJKLMNOPRSTUWYZDC"

green = (0,255,0)
purple = (100,15,161)
lt_blue = (150,255,255)
blue = (81,132,184)
dark_blue = (50,50,250)
lt_red = (185,0,0)
red = (225,0,0)
dr_red = (150,0,0)
white = (255,255,255)
black = (0,0,0)
lt_purple = (127,0,255)
gray = (169,169,169)
dark_green = (0,71,49)
orange = (255, 102, 0)
dark_gray = (43,45,47)
darker_gray=(31,31,31)

now = str(datetime.now())
nowDay = now[8:-16]
nowMonth = now[5:-19]
nowHour = now[11:-10]

print("Initialized!")

def findFile(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
def decipher(textin):
    deciphered = ""
    for char in textin:
        char = ord(char) - 1
        deciphered += chr(char)
    return deciphered

class Write1(pygame.sprite.Sprite):
    def __init__(self,size,text,color,center):
        pygame.sprite.Sprite.__init__(self)
        self.textObject = pygame.font.Font(r"{}WakeUp!\Fonts\TrajanPro\TrajanPro-Regular.ttf".format(dirPath),size)
        self.writeText = self.textObject.render(text,True,color)
        self.textRect = self.writeText.get_rect()
        self.textRect.center = center
class Write2(pygame.sprite.Sprite):
    def __init__(self,size,text,color,center):
        pygame.sprite.Sprite.__init__(self)
        self.textObject = pygame.font.Font(r"{}WakeUp!\Fonts\arrow\Arrow.ttf".format(dirPath),size)
        self.writeText = self.textObject.render(text,True,color)
        self.textRect = self.writeText.get_rect()
        self.textRect.center = center

def alarmScreen():
    global screen,isSound
    size = (800,600)
    name = "WakeUp!-Alarm"
    screen = pygame.display.set_mode(size,0,32)
    screen.fill(red)
    pygame.display.set_caption(name)
    mainTitle = Write1(16,"WakeUp!",black,[400,20])
    screen.blit(mainTitle.writeText,mainTitle.textRect)
    alarmClock = pygame.image.load(r"{}WakeUp!\Picts\Rects\alarmClock2.png".format(dirPath))
    screen.blit(alarmClock,(340,140))

    #Text
    mainText = Write2(30,"You have planned an alarm for now!",black,[400,100])
    screen.blit(mainText.writeText,mainText.textRect)

    metaAlarm = open(r"{}WakeUp!\Data\userData\Meta\alarmMeta.txt".format(dirPath),"r")
    metaAlarm2 = open(r"{}WakeUp!\Data\userData\Meta\alarmMeta2.txt".format(dirPath),"r")

    metaAlarmText = metaAlarm.read().splitlines()
    metaAlarmText2 = metaAlarm2.read().splitlines()
    metaAlarmTextToWrite=[]

    wrongLines = 0
    preIt = 0
    it = 0

    if len(metaAlarmText) != 0 and len(metaAlarmText2) != 0:
        notey=340
        #Find alarm number/index
        for x in metaAlarmText2:
            if x[1:3] == nowDay and x[4:6] == nowMonth and x[11:16] == nowHour:
                break
            else:
                preIt += 1
                wrongLines += int(x[0])
        #Get lines of note to write
        for x in range(int(metaAlarmText2[preIt][0])):
            metaAlarmTextToWrite.append(metaAlarmText[x+wrongLines])
        #Write note on screen
        notex=340
        for x in metaAlarmTextToWrite:
            write = Write1(16,decipher(x),black,[notex,notey])
            screen.blit(write.writeText,write.textRect)
            notex += 165
            it +=1
            if it%2==0:
                notex = 390
                notey += 20
        #Remove used values 
        for x in range(int(metaAlarmText2[preIt][0])):
            metaAlarmText.pop(0+wrongLines)
        metaAlarmText2.remove(metaAlarmText2[preIt])

        metaAlarmClear = open(r"{}WakeUp!\Data\userData\Meta\alarmMeta.txt".format(dirPath),"w")
        metaAlarmClear2 = open(r"{}WakeUp!\Data\userData\Meta\alarmMeta2.txt".format(dirPath),"w")

        for x in metaAlarmText:
            metaAlarmClear.write(x+"\n")
        metaAlarmClear.close()
        for x in metaAlarmText2:
            metaAlarmClear2.write(x+'\n')
        metaAlarmClear2.close()

    else:
        mainText2 = Write2(30,"Guess you have something important to do",black,[400,340])
        screen.blit(mainText2.writeText,mainText2.textRect)

        metaAlarmClear = open(r"{}WakeUp!\Data\userData\Meta\alarmMeta.txt".format(dirPath),"w")
        metaAlarmClear.close()
        metaAlarmClear2 = open(r"{}WakeUp!\Data\userData\Meta\alarmMeta2.txt".format(dirPath),"w")
        metaAlarmClear2.close()
    

    metaAlarm.close()
    metaAlarm2.close()

    pygame.display.flip() 
def isSoundOn():
    global isSound
    preIt = 0
    soundMeta = open(r"{}WakeUp!\Data\userData\wav\specmeta.txt".format(dirPath),"r")
    soundMetaText = soundMeta.read().splitlines()
    if len(soundMetaText) > 0:
        for x in soundMetaText:
            if x[1:3] == nowDay and x[4:6] == nowMonth and x[11:16] == nowHour:
                break
            else:
                preIt += 1

        if soundMetaText[preIt][0] == "T":
            isSound = True
        else:
            isSound = False
        soundMetaText.remove(soundMetaText[preIt])

        soundMetaClear = open(r"{}WakeUp!\Data\userData\wav\specmeta.txt".format(dirPath),"w")

        for x in soundMetaText:
            soundMetaClear.write(x+"\n")
        soundMetaClear.close()
    soundMeta.close()
def exitRect(color):
    exitRect = pygame.draw.rect(screen,color,[300,500,200,50])
    exitRect = pygame.draw.rect(screen,dr_red,[300,500,200,50],3)
    mainText2 = Write2(25,"Exit",dark_gray,[400,525])
    screen.blit(mainText2.writeText,mainText2.textRect)   

    pygame.display.update()

print("Looking for path...")
for x in disks:
    check = findFile(r"WakeUp.exe",r"{}:\\".format(x))
    if check != None:
        print("Path found!")
        global dirPath
        dirPath = check[:-36]
        break
print("Making enviroment...")
alarmScreen()
isSoundOn()
exitRect(lt_red)
if isSound:
    try:
        openMeta = open(r"{}WakeUp!\Data\userData\Meta\meta6p.txt".format(dirPath),"r")
        readMeta = openMeta.read()
        pygame.mixer.music.load(r"{}WakeUp!\Data\userData\wav\{}".format(dirPath,decipher(readMeta)))
        pygame.mixer.music.play(1)
        openMeta.close()
    except:
        pygame.mixer.music.load(r"{}WakeUp!\Data\userData\wav\iron_man.wav".format(dirPath))
        pygame.mixer.music.play(1)
print("Done!")
while running:
    clock.tick(60)
    mouse_pos = pygame.mouse.get_pos()
    #coords
    exitRectCord = mouse_pos[0] in list(range(300,500)) and mouse_pos[1] in list(range(500,550))
        
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEMOTION:
            if exitRectCord:
                exitRect(dr_red)
            elif not exitRectCord:
                exitRect(lt_red)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if exitRectCord and event.button == 1:
                running = False

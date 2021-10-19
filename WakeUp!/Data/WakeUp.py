from typing import ChainMap
import pygame
from pygame.locals import *
import os
import subprocess
from random import randint
from time import sleep
from datetime import datetime
pygame.init()

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path[:-4]#-16 in .exe|-4 in .py


#color tupples
green = (0,255,0)
purple = (100,15,161)
lt_blue = (150,255,255)
blue = (81,132,184)
dark_blue = (50,50,250)
red = (225,0,0)
white = (255,255,255)
black = (0,0,0)
lt_purple = (127,0,255)
gray = (169,169,169)
dark_green = (0,71,49)
orange = (255, 102, 0)
dark_gray = (43,45,47)
darker_gray=(31,31,31)
yel = (250,250,0)
bronze = (111,54,8)
pink = (230,0,126)
salmon = (250,128,114)
aqua=(127,255,212)
khaki=(161,140,117)
ecru=(245,245,220)
allColors = [green,purple,lt_blue,blue,dark_blue,red,white,black,lt_purple,gray,dark_green,orange,dark_gray,
darker_gray,yel,bronze,pink,salmon,aqua,khaki,ecru]

backgroundPict = "Bonsai.jpg"
sideBarPict = "Leaves.png"

backgrounds = ["Bonsai.jpg","City.jpg","Couple.jpg","Dog.jpg","Flower.jpg","River.jpg","Sea.jpg","Stars.jpg"]
sideBars = ["Clouds.png","Cobblestone.png","Colorfoul.png","Leaves.png","Mountain.png","Sea.png","Sky.png","Stars.png"]
sounds = ["Meltdown","Ready","Iron_Man","Pacific_Rim","Pirates","Sorry","Never","Legendary"]

def cipher(textin):
    ciphered = ""
    for char in textin:
        char = ord(char) + 1
        ciphered += chr(char)
    return ciphered 
def decipher(textin):
    deciphered = ""
    for char in textin:
        char = ord(char) - 1
        deciphered += chr(char)
    return deciphered
def getFromMeta():
    global col1,col2,col3,backgroundPict,sideBarPict
    try:
        metaFile = open(r"{}Data\userData\Meta\meta{}.txt".format(dir_path,1),"r")
        metaFileData = metaFile.read()
        metaFileData = decipher(metaFileData)[:-23]
        metaRGB = metaFileData.split("{")
        col1 = (int(metaRGB[0]),int(metaRGB[1]),int(metaRGB[2]))
        metaFile.close()
    except:
        col1 = darker_gray
    try:
        metaFile2 = open(r"{}Data\userData\Meta\meta{}.txt".format(dir_path,2),"r")
        metaFileData = metaFile2.read()
        metaFileData = decipher(metaFileData)[:-23]
        metaRGB = metaFileData.split("{")
        col2 = (int(metaRGB[0]),int(metaRGB[1]),int(metaRGB[2]))
        metaFile2.close()
    except:
        col2 = dark_green
    try:
        metaFile3 = open(r"{}Data\userData\Meta\meta{}.txt".format(dir_path,3),"r")
        metaFileData = metaFile3.read()
        metaFileData = decipher(metaFileData)[:-23]
        metaRGB = metaFileData.split("{")
        col3 = (int(metaRGB[0]),int(metaRGB[1]),int(metaRGB[2]))
        metaFile3.close()
    except:
        col3 = dark_gray
    metaFile4 = open(r"{}Data\userData\Meta\meta{}p.txt".format(dir_path,4),"r")
    metaFileData = metaFile4.read()
    if len(metaFileData) > 4:
        metaFileData = decipher(metaFileData)
        backgroundPict = metaFileData
    else:
        backgroundPict = "Bonsai.jpg"
    metaFile4.close()
    metaFile5 = open(r"{}Data\userData\Meta\meta{}p.txt".format(dir_path,5),"r")
    metaFileData = metaFile5.read()
    if len(metaFileData) > 4:
        metaFileData = decipher(metaFileData)
        sideBarPict = metaFileData
    else:
        sideBarPict = "Leaves.png"
    metaFile5.close()

getFromMeta()

#for setAlarm
hour1 = "0"
hour2 = "0"
min1 = "0"
min2 = "0"
wake_nr = randint(1,10000)
iterator_sound=1

fps=60
clock = pygame.time.Clock()


class WriteRegular(pygame.sprite.Sprite):
    def __init__(self,size,text,color,center):
        pygame.sprite.Sprite.__init__(self)
        self.textObject = pygame.font.Font(r"{}Fonts\TrajanPro\TrajanPro-Regular.ttf".format(dir_path),size)
        self.writeText = self.textObject.render(str(text),True,color)
        self.textRect = self.writeText.get_rect()
        self.textRect.center = center
class WriteBold(pygame.sprite.Sprite):
    def __init__(self,size,text,color,center):
        pygame.sprite.Sprite.__init__(self)
        self.textObject = pygame.font.Font(r"{}Fonts\arrow\Arrow.ttf".format(dir_path),size)
        self.writeText = self.textObject.render(text,True,color)
        self.textRect = self.writeText.get_rect()
        self.textRect.center = center
class CustomRect(pygame.sprite.Sprite):
    def __init__(self,image,location):
        pygame.sprite.Sprite.__init__(self)
        self.imageRect = pygame.image.load(image).convert()
        self.rect = self.imageRect.get_rect()
        self.rect.left, self.rect.top = location

def writeToMeta(number,val):
        metaFile = open(r"{}Data\userData\Meta\meta{}.txt".format(dir_path,number),"w")
        val1 = cipher(str(val[0]))
        val2 = cipher(str(val[1]))
        val3 = cipher(str(val[2]))
        standardText = cipher("ThoseAreCipheredColors") #len:22
        metaFile.write(str(val1)+"|")
        metaFile.write(str(val2)+"|")
        metaFile.write(str(val3)+"|")
        metaFile.write(standardText)
        metaFile.close()
def writeToMeta_P(number,val):
    metaFile = open(r"{}Data\userData\Meta\meta{}p.txt".format(dir_path,number),"w")
    ciphVal = cipher(val)
    metaFile.write(ciphVal)
    metaFile.close()
def clearMetaFile(endwith_string):
    metaFile = open(r"{}Data\userData\Meta\meta{}.txt".format(dir_path,endwith_string),"w")
    metaFile.close()
def resetMeta():
    clearMetaFile("1")
    clearMetaFile("2")
    clearMetaFile("3")
    clearMetaFile("4p")
    clearMetaFile("5p")

def opt1Text(borderColor,textColor):
    global sideBarOpt1
    sideBarOpt1 = pygame.draw.rect(screen,borderColor,[10,45,105,115],5)
    optText1 = WriteBold(25,"Set",textColor,[60,80])
    optText12 = WriteBold(25,"Alarm",textColor,[60,115])
    screen.blit(optText1.writeText,optText1.textRect)
    screen.blit(optText12.writeText,optText12.textRect)   
def opt2Text(borderColor,textColor):
    global sideBarOpt2
    sideBarOpt2 = pygame.draw.rect(screen,borderColor,[10,195,105,115],5)
    optText2 = WriteBold(24,"Planned",textColor,[60,230])
    optText21 = WriteBold(24,"Alarms",textColor,[60,265])
    screen.blit(optText2.writeText,optText2.textRect)
    screen.blit(optText21.writeText,optText21.textRect)
def opt3Text(borderColor,textColor):
    global sideBarOpt3
    sideBarOpt3 = pygame.draw.rect(screen,borderColor,[10,325,105,115],5)
    optText3 = WriteBold(24,"Settings",textColor,[60,380])
    screen.blit(optText3.writeText,optText3.textRect)
def opt4Text(borderColor,textColor):
    global sideBarOpt4
    sideBarOpt4 = pygame.draw.rect(screen,borderColor,[10,495,105,115],5)
    optText4 = WriteBold(30,"Quit",textColor,[60,550])
    screen.blit(optText4.writeText,optText4.textRect)
def optsMouseOverEvents():
    if sideBarOpt1.collidepoint(mouse_pos):                    
        opt1Text(col3,col2)
    elif not sideBarOpt1.collidepoint(mouse_pos):
        opt1Text(col1,col2)
    if sideBarOpt2.collidepoint(mouse_pos):
        opt2Text(col3,col2)
    elif not sideBarOpt2.collidepoint(mouse_pos):
        opt2Text(col1,col2)
    if sideBarOpt3.collidepoint(mouse_pos):
        opt3Text(col3,col2)
    elif not sideBarOpt3.collidepoint(mouse_pos):
        opt3Text(col1,col2)
    if sideBarOpt4.collidepoint(mouse_pos):
        opt4Text(col3,col2)
    elif not sideBarOpt4.collidepoint(mouse_pos):
        opt4Text(col1,col2)

def useMainScreen():
    global screenSize,name,background,screen

    screenSize = (1100,680)
    name = "WakeUp!"
    try:
        background = pygame.image.load(r"{}Picts\Background\{}".format(dir_path,backgroundPict))
    except:
        background = pygame.image.load(r"{}Picts\Background\{}".format(dir_path,"Bonsai.jpg"))   

    screen = pygame.display.set_mode(screenSize,0,32)
    
    icon = pygame.image.load(r"{}Picts\Rects\32x32Clock.png".format(dir_path))
    pygame.display.set_icon(icon)

    pygame.display.set_caption(name)
    screen.blit(background, (0,0))

    mainTitle = WriteRegular(48,"Welcome to WakeUp!",col2,[575,100])
    screen.blit(mainTitle.writeText,mainTitle.textRect)

    try:
        sideBar = CustomRect(r"{}Picts\sideBar\{}".format(dir_path,sideBarPict),[0,0])
    except:
        sideBar = CustomRect(r"{}Picts\sideBar\{}".format(dir_path,"Leaves.png"),[0,0])
    screen.blit(sideBar.imageRect,sideBar.rect)

    pygame.display.flip()
def counter(startObject,xstart,ystart,xlenght,ylenght):
    current = startObject
    pygame.draw.rect(screen,col1,[xstart,ystart,xlenght,ylenght])
    if xlenght>60:
        drawCounter = WriteRegular(14,current,col2,[(xstart+xlenght)-50,(ystart+ylenght)-15])
        screen.blit(drawCounter.writeText,drawCounter.textRect) 
    else:
        drawCounter = WriteRegular(14,current,col2,[(xstart+xlenght)-15,(ystart+ylenght)-15])
        screen.blit(drawCounter.writeText,drawCounter.textRect) 
def setFps():
    global fps
    if fps60 and event.button == 1:
        fps = 60
        resetScreen(True)
        settingsDraw(col2,col3)
        fps60Text = WriteRegular(20,"60",col2,[400,223])
        screen.blit(fps60Text.writeText,fps60Text.textRect)
    elif fps120 and event.button == 1:
        fps =120
        resetScreen(True)
        settingsDraw(col2,col3)
        fps120Text = WriteRegular(20,"120",col2,[600,223])
        screen.blit(fps120Text.writeText,fps120Text.textRect)
    elif fps200 and event.button == 1:
        fps = 200
        resetScreen(True)
        settingsDraw(col2,col3)
        fps200Text = WriteRegular(20,"200",col2,[800,223])
        screen.blit(fps200Text.writeText,fps200Text.textRect)
def useAdditionalScreen(color):
    surface = pygame.draw.rect(screen,color,[134,150,1000,530])
    exitButton = pygame.draw.rect(screen,red,[1050,151,50,50],3)
    exitButtonX = WriteBold(30,"X",red,[1075,177])
    screen.blit(exitButtonX.writeText,exitButtonX.textRect)

def setAlarmDraw(rectColor,textColor,succColor):
    global soundsButton
    mainRect = pygame.draw.rect(screen,rectColor,[450,340,250,100],5)
    pygame.draw.line(screen,rectColor,[575,340],[575,440],5)

    hourUp1 = pygame.draw.rect(screen,rectColor,[460,260,50,80],5)
    hourUp2 = pygame.draw.rect(screen,rectColor,[510,260,50,80],5)
    minuteUp1 = pygame.draw.rect(screen,rectColor,[590,260,50,80],5)
    minuteUp2 = pygame.draw.rect(screen,rectColor,[640,260,50,80],5)
    hourDown1 = pygame.draw.rect(screen,rectColor,[460,440,50,80],5)
    hourDown2 = pygame.draw.rect(screen,rectColor,[510,440,50,80],5)
    minuteDown1 = pygame.draw.rect(screen,rectColor,[590,440,50,80],5)
    minuteDown2 = pygame.draw.rect(screen,rectColor,[640,440,50,80],5)
    success = pygame.draw.rect(screen,succColor,[900,440,100,80],5)

    timeH1 = WriteBold(76,hour1,textColor,[485,400])
    screen.blit(timeH1.writeText,timeH1.textRect)
    timeH2 = WriteBold(76,hour2,textColor,[535,400])
    screen.blit(timeH2.writeText,timeH2.textRect)

    timeM1 = WriteBold(76,min1,textColor,[615,400])
    screen.blit(timeM1.writeText,timeM1.textRect)
    timeM2 = WriteBold(76,min2,textColor,[665,400])
    screen.blit(timeM2.writeText,timeM2.textRect)
    
    arrowUpH1 = WriteRegular(76,"+",textColor,[485,300])
    screen.blit(arrowUpH1.writeText,arrowUpH1.textRect)
    arrowUpH2 = WriteRegular(76,"+",textColor,[535,300])
    screen.blit(arrowUpH2.writeText,arrowUpH2.textRect)    

    arrowUpM1 = WriteRegular(76,"+",textColor,[615,300])
    screen.blit(arrowUpM1.writeText,arrowUpM1.textRect)
    arrowUpM2 = WriteRegular(76,"+",textColor,[665,300])
    screen.blit(arrowUpM2.writeText,arrowUpM2.textRect)

    arrowDownH1 = WriteRegular(76,"-",textColor,[485,480])
    screen.blit(arrowDownH1.writeText,arrowDownH1.textRect)
    arrowDownH2 = WriteRegular(76,"-",textColor,[535,480])
    screen.blit(arrowDownH2.writeText,arrowDownH2.textRect)
    
    arrowDownM1 = WriteRegular(76,"-",textColor,[615,480])
    screen.blit(arrowDownM1.writeText,arrowDownM1.textRect)
    arrowDownM2 = WriteRegular(76,"-",textColor,[665,480])
    screen.blit(arrowDownM2.writeText,arrowDownM2.textRect)

    setAlarmDateButton = pygame.draw.rect(screen,rectColor,[520,600,150,50],3)
    setAlarmDateButtonText=WriteBold(20,"+Date",rectColor,[590,627])
    screen.blit(setAlarmDateButtonText.writeText,setAlarmDateButtonText.textRect)

    addNoteButton = pygame.draw.rect(screen,col3,[160,180,100,50],3)
    addNoteText = WriteRegular(22,"+Note",col3,[205,207])
    screen.blit(addNoteText.writeText,addNoteText.textRect)

    successText = WriteBold(36,"OK",succColor,[950,480])
    screen.blit(successText.writeText,successText.textRect)

    setAlarmSoundDraw()


def setAlarmSetDateDraw(back_color):
    pygame.draw.rect(screen,col3,[230,570,800,80]) #main

    pygame.draw.rect(screen,col1,[240,575,200,70]) #left
    dText = WriteRegular(42,"D|",col2,[280,615])
    screen.blit(dText.writeText,dText.textRect)

    pygame.draw.rect(screen,col1,[450,575,200,70]) #center
    mText = WriteRegular(42,"M|",col2,[490,615])
    screen.blit(mText.writeText,mText.textRect)

    pygame.draw.rect(screen,col1,[660,575,200,70]) #right
    yText = WriteRegular(36,"Today",col2,[750,615])
    screen.blit(yText.writeText,yText.textRect)

    pygame.draw.rect(screen,back_color,[890,575,100,70],3) #back
    arrow = WriteRegular(52,"<-",col2,[940,610])
    screen.blit(arrow.writeText,arrow.textRect)
    #DATES
    currentDay = WriteRegular(45,setDateDay,col2,[360,615])
    screen.blit(currentDay.writeText,currentDay.textRect)

    currentMonth = WriteRegular(45,setDateMonth,col2,[570,615])
    screen.blit(currentMonth.writeText,currentMonth.textRect)
def setAlarmSetDateDayChoosingFunc():
    if setAlarmSetDateDayChoosing:
        pygame.draw.rect(screen,col2,[240,575,200,70],3)
    else:
        pygame.draw.rect(screen,col1,[240,575,200,70],3)
    currentDay = WriteRegular(45,setDateDay,col2,[360,615])
    screen.blit(currentDay.writeText,currentDay.textRect)
def setAlarmSetDateMonthChoosingFunc():
    if setAlarmSetDateMonthChoosing:
        pygame.draw.rect(screen,col2,[450,575,200,70],3)
    else:
        pygame.draw.rect(screen,col1,[450,575,200,70],3)
    currentMonth = WriteRegular(45,setDateMonth,col2,[570,615])
    screen.blit(currentMonth.writeText,currentMonth.textRect)
def setAlarmSetDateCurrentDate():
    global setDateDay,setDateMonth
    now = datetime.now()
    setDateDay = str(now)[8:-16]
    setDateMonth = str(now)[5:-19]

    setAlarmSetDateReset("day")
    setAlarmSetDateReset("month")

    if setAlarmSetDateToday:
        pygame.draw.rect(screen,col2,[660,575,200,70],3)
    else:
        pygame.draw.rect(screen,col1,[660,575,200,70],3)
def setAlarmSetDateReset(DayOrMonth_String):
    global setDateDay,setDateMonth
    if str(DayOrMonth_String).upper() == "DAY":
        pygame.draw.rect(screen,col1,[305,585,125,55])
        currentDay = WriteRegular(45,setDateDay,col2,[360,615])
        screen.blit(currentDay.writeText,currentDay.textRect)

    if str(DayOrMonth_String).upper() == "MONTH":
        pygame.draw.rect(screen,col1,[520,585,120,55])
        currentMonth = WriteRegular(45,setDateMonth,col2,[570,615])
        screen.blit(currentMonth.writeText,currentMonth.textRect)
    try:
        if int(setDateDay) > 31 or int(setDateDay) < 0:
            setDateDay = ""
        if int(setDateMonth) > 12 or int(setDateMonth) < 0:
            setDateMonth = ""
    except:
        try:
            check = int(setDateDay)
        except:
            setDateDay = ""
        try:
            check = int(setDateMonth)
        except:
            setDateMonth=""
def setAlarmResetScreen():
    useAdditionalScreen(col1)
    setAlarmDraw(col3,col2,col3)
    if setAlarmSetDate:
        setAlarmSetDateDraw(col1)
    if addNoteEvents:
        setAlarmAddNoteDraw()
def setAlarmMouseMotionEvents():
    if setAlarmSuccBut: #Set Alarm Success Button Change
        successText = WriteBold(36,"OK",col2,[950,480])
        screen.blit(successText.writeText,successText.textRect)
    elif not setAlarmSuccBut: #Set Alarm Success Button Change To Normal
        successText = WriteBold(36,"OK",col3,[950,480])
        screen.blit(successText.writeText,successText.textRect)
    if not setAlarmSetDate: #Set Alarm Set Date Events in Main Set Alarm
        if setAlarmDateButton: #Set Alarm Set Date Button Change
            setAlarmDateButtonText=WriteBold(20,"+Date",col2,[590,627])
            screen.blit(setAlarmDateButtonText.writeText,setAlarmDateButtonText.textRect)
        elif not setAlarmDateButton: #Set Alarm Set Date Button Change To Normal
            setAlarmDateButtonText=WriteBold(20,"+Date",col3,[590,627])
            screen.blit(setAlarmDateButtonText.writeText,setAlarmDateButtonText.textRect)
    elif setAlarmSetDate:
        if setAlarmDateButton_Back: 
            pygame.draw.rect(screen,col2,[890,575,100,70],3)
        elif not setAlarmDateButton_Back:
            pygame.draw.rect(screen,col1,[890,575,100,70],3)
    if addNotePos:
        addNoteButton = pygame.draw.rect(screen,col2,[160,180,100,50],3)
    elif not addNotePos:
        addNoteButton = pygame.draw.rect(screen,col3,[160,180,100,50],3)
def setAlarmClockClickEvents():
                global setAlarmIt,setAlarmLimit
                global setAlarmHDown1,setAlarmHDown2,setAlarmHUp1,setAlarmHUp2
                global setAlarmMDown1,setAlarmMDown2,setAlarmMUp1,setAlarmMUp2
                global hour1,hour2,min1,min2
                setAlarmLimit = False
                setAlarmResetScreen()
                #Setting Alarms by main options - START
                if setAlarmIt >= 56:
                    setAlarmLimit = True
                if setAlarmLimit:
                    setAlarmLimitText = WriteBold(25,"Limit Reached!",col3,[800,200])
                    screen.blit(setAlarmLimitText.writeText,setAlarmLimitText.textRect)
                if setAlarmHUp1 and event.button==1:
                    if int(hour1) < 2:
                        if int(hour1) != 1 or int(hour2) <= 3:
                            hour1 = int(hour1) + 1
                            hour1 = str(hour1)
                            setAlarmResetScreen()
                if setAlarmHUp2 and event.button==1:
                    if int(hour1) < 2:
                        if int(hour2) < 9:
                            hour2 = int(hour2) + 1
                            hour2 = str(hour2)
                            setAlarmResetScreen()
                    else:
                        if int(hour2) < 3:
                            hour2 = int(hour2) + 1
                            hour2 = str(hour2)
                            setAlarmResetScreen()
                if setAlarmHDown1 and event.button==1: 
                    if int(hour1) > 0:
                        hour1 = int(hour1) - 1
                        hour1 = str(hour1)
                        setAlarmResetScreen()
                if setAlarmHDown2 and event.button==1:
                    if int(hour2) > 0:
                        hour2 = int(hour2) - 1
                        hour2 = str(hour2)
                        setAlarmResetScreen()
                if setAlarmMUp1 and event.button==1:
                    if int(hour1) != 2  or int(hour2) != 4:
                        if int(min1) < 5:
                            min1 = int(min1) + 1
                            min1 = str(min1)
                            setAlarmResetScreen()
                if setAlarmMDown1 and event.button==1:
                    if int(min1) > 0:
                        min1 = int(min1) - 1
                        min1 = str(min1)
                        setAlarmResetScreen()
                if setAlarmMUp2 and event.button==1:
                    if int(hour1) != 2  or int(hour2) != 4:
                        if int(min2) < 9:
                            min2 = int(min2) + 1
                            min2 = str(min2)
                            setAlarmResetScreen()
                if setAlarmMDown2 and event.button==1:
                    if int(min2) > 0:
                        min2 = int(min2) - 1
                        min2 = str(min2)
                        setAlarmResetScreen()
def setAlarmButtonAction():
                global setAlarmSetDate, finalTime, wake_nr, setAlarmIt
                global setAlarmSetDateDayChoosing,setAlarmSetDateMonthChoosing, setAlarmSetDateToday
                global setDateDay,setDateMonth
                global addNoteEvents,noteText,noteTextList
                global iterator_sound, soundOn
                lenght = 0
                isCorrect = True
                if addNotePos and event.button == 1: #Add note
                    addNoteEvents=True
                    setAlarmAddNoteDraw()
                if setAlarmDateButton and event.button==1: #Set Alarm Setting Date
                    setAlarmSetDate = True
                    setAlarmSetDateDraw(col1)
                    setAlarmSetDateCurrentDate()
                if setAlarmSetDate:
                    if setAlarmSetDateLeft and event.button == 1:
                        setAlarmSetDateDayChoosing = True
                        setAlarmSetDateMonthChoosing = False
                        setAlarmSetDateToday = False
                        setAlarmSetDateDayChoosingFunc()
                    elif setAlarmSetDateCenter and event.button == 1:
                        setAlarmSetDateMonthChoosing = True
                        setAlarmSetDateDayChoosing = False
                        setAlarmSetDateToday = False
                        setAlarmSetDateMonthChoosingFunc()
                    else:
                        setAlarmSetDateMonthChoosing = False
                        setAlarmSetDateDayChoosing = False
                        setAlarmSetDateToday = False
                    if setAlarmSetDateRight and event.button == 1:
                        setAlarmSetDateMonthChoosing = False
                        setAlarmSetDateDayChoosing = False
                        setAlarmSetDateToday = True
                        setAlarmSetDateCurrentDate()
                    if setAlarmSetDate and setAlarmDateButton_Back and event.button == 1: #BACK
                        setAlarmSetDateMonthChoosing = False
                        setAlarmSetDateDayChoosing = False
                        setDateMonth = str(nowDay)
                        setDateDay = str(nowMonth)
                        setAlarmSetDate = False
                        setAlarmResetScreen()
                if addNoteEvents:
                    setAlarmAddNoteDraw()
                    if addNoteButtonXPos and event.button==1:
                        addNoteEvents = False
                        setAlarmResetScreen()
                        noteText = ""
                        noteTextList = []
                if soundsButton.collidepoint(mouse_pos) and event.button==1:
                    iterator_sound += 1
                    if iterator_sound % 2 == 0:
                        soundOn = False
                    else:
                        soundOn=True
                    setAlarmSoundDraw()
                if setAlarmSuccBut and event.button == 1 and not setAlarmLimit:
                    finalTime=hour1+hour2+":"+min1+min2
                    #check if date is correct
                    try:
                        if len(setDateDay) == 0 and len(setDateMonth) == 0:
                            pass
                        elif int(setDateMonth) == 2 and int(setDateDay)>28:
                            isCorrect=False 
                        elif int(setDateMonth) in list([2,4,6,9,11]) and int(setDateDay)>30:
                            isCorrect = False
                        elif int(setDateMonth) < int(nowMonth):
                            isCorrect = False
                        elif int(setDateMonth) == int(nowMonth):
                            if int(setDateDay) < int(nowDay):
                                isCorrect = False
                            elif int(setDateDay) == int(nowDay):
                                if int(finalTime[0:2]) < int(nowHour[0:2]):
                                    isCorrect = False
                                elif int(finalTime[0:2]) == int(nowHour[0:2]):
                                    if int(finalTime[3:]) <= int(nowHour[3:]):
                                        isCorrect=False
                    except:
                        isCorrect = False
                    #clear file before use 
                    setAlarmClear = open(r"{}Data\planned.txt".format(dir_path),'w')
                    setAlarmClear.close()

                    if len(setDateDay) == 1:
                        setDateDay = '0' + setDateDay
                    elif len(setDateMonth) == 1:
                        setDateMonth = '0' + setDateMonth
                    elif len(setDateDay) == 0 and len(setDateMonth) == 0:
                        setDateDay = str(datetime.now())[8:-16]
                        setDateMonth = str(datetime.now())[5:-19]
                    date = setDateDay+"/"+setDateMonth+"/"+str(datetime.now())[:-22]
                    if isCorrect:
                        noteMeta = open(r"{}Data\userData\Meta\alarmMeta.txt".format(dir_path),"a")
                        for x in noteTextList:
                            noteMeta.write(cipher(x)+"\n")
                        noteMeta.write(cipher(noteText)+"\n")
                        noteMeta.close()

                        noteMeta = open(r"{}Data\userData\Meta\alarmMeta2.txt".format(dir_path),"a")
                        if len(noteTextList)!=0: 
                            lenght += len(noteTextList)
                        if len(noteText) != 0:
                            lenght += 1
                        if lenght != 0:
                            noteMeta.write(str(lenght)+date+finalTime+"\n")
                        noteMeta.close()
                        soundMeta = open(r"{}Data\userData\wav\specmeta.txt".format(dir_path),"a")
                        soundMeta.write(str(soundOn)[0]+date+finalTime+"\n")
                        soundMeta.close()
                        
                    if len(setDateDay)==0 and len(setDateMonth)==0:
                        os.system(r"schtasks /create /tn Wake{} /tr '{}Data\dist\Alarm\Alarm.exe' /sc once /st {} /f".format(wake_nr,dir_path,finalTime))
                    else:
                        os.system(r"schtasks /create /tn Wake{} /tr '{}Data\dist\Alarm\Alarm.exe' /sc once /st {} /sd {} /f".format(wake_nr,dir_path,finalTime,date))
                    wake_nr = randint(1,10000)
                    setAlarmIt += 1
                    useAdditionalScreen(col1)
                    setAlarmDraw(col3,col2,col3)
                    if setAlarmSetDate:
                        setAlarmSetDateDraw(col1)
                    if addNoteEvents:
                        setAlarmAddNoteDraw()
                    if isCorrect:
                        if setAlarmIt%2==0:
                            setSuccess = WriteRegular(32,"Set!",col2,[950,400])
                            screen.blit(setSuccess.writeText,setSuccess.textRect)
                        else:
                            setSuccess = WriteRegular(32,"Set!",col2,[950,300])
                            screen.blit(setSuccess.writeText,setSuccess.textRect)
                    else:
                        wrongDateText = WriteRegular(30,"Incorrect Date!",col2,[900,300])
                        screen.blit(wrongDateText.writeText,wrongDateText.textRect)
def setAlarmAddNoteDraw():
    global setAlarmSetDateDayChoosing,setAlarmSetDateMonthChoosing
    pygame.draw.rect(screen,col3,[160,250,250,300])

    goBackButtonRect = pygame.draw.rect(screen,col2,[360,199,50,50],3)
    goBackButtonX = WriteRegular(30,"X",col2,[385,227])
    screen.blit(goBackButtonX.writeText,goBackButtonX.textRect)

    notex = 285
    notey = 270
    it = 20
    listIt = 0

    if len(noteTextList) == 0:
        note = WriteRegular(16,noteText,col2,[notex,notey])
        screen.blit(note.writeText,note.textRect)
    else:
        for x in noteTextList:
            earlierNote = WriteRegular(16,x,col2,[notex,notey+(it*listIt)])
            screen.blit(earlierNote.writeText,earlierNote.textRect)
            listIt += 1

        note = WriteRegular(16,noteText,col2,[notex,notey+it*len(noteTextList)])
        screen.blit(note.writeText,note.textRect)
def setAlarmSoundDraw():
    global soundOn,soundsButton
    if soundOn:
        soundsButton = pygame.draw.rect(screen,col3,[820,160,150,50])
        soundsPic = pygame.image.load(r"{}Picts\Rects\speaker.png".format(dir_path))
        screen.blit(soundsPic,(825,165))
        soundsActiveRect = pygame.draw.rect(screen,col2,[820,160,150,50],1)
        isSoundText = WriteRegular(25,"ON",col2,[910,185])
        screen.blit(isSoundText.writeText,isSoundText.textRect)
    else:
        soundsButton = pygame.draw.rect(screen,col3,[820,160,150,50])
        soundsPic = pygame.image.load(r"{}Picts\Rects\speaker.png".format(dir_path))
        screen.blit(soundsPic,(825,165))
        isSoundText = WriteRegular(25,"OFF",col2,[910,185])
        screen.blit(isSoundText.writeText,isSoundText.textRect)
        pygame.draw.line(screen,col2,[860,165],[830,205],3)

def plannedAlarmsLines(color):
    pygame.draw.line(screen,color,[300,150],[300,700],3)
    pygame.draw.line(screen,color,[900,150],[900,700],3)
def plannedAlarmsMain(color1,color2):
                    global setAlarmIt
                    plannedAlarmsDeleteButton = pygame.draw.rect(screen,color2,[920,550,150,50],3)
                    DeleteAllButton=WriteRegular(20,"DELETE ALL",color2,[995,577])
                    screen.blit(DeleteAllButton.writeText,DeleteAllButton.textRect)
                    it = 1
                    plannedList=[]
                    #clear file
                    plannedClear = open(r"{}Data\planned.txt".format(dir_path),'w')
                    plannedClear.close()
                    #perform operation with planned.txt
                    os.system(r"schtasks >> {}Data\planned.txt".format(dir_path))
                    plannedRead = open(r"{}Data\planned.txt".format(dir_path),'r')
                    plannedCheck = plannedRead.read()
                    plannedCheck = plannedCheck.splitlines()
                    global plannedExistingAlarms,plannedFinal
                    plannedExistingAlarms = []
                    plannedFinal=[]
                    for x in plannedCheck:
                        if x.startswith("Wake") and not "N/A" in x:
                            plannedExistingAlarms.append(x[41:-19])
                            plannedFinal.append(x[:-71].strip())
                    plannedRead.close()
                    plannedx=680
                    plannedy=200
                    unplannedx=500
                    i = 1
                    plannedExistingAlarms.sort()
                    plannedIt=len(plannedExistingAlarms)
                    if plannedIt < 20:
                        for x in plannedExistingAlarms:
                            plannedPreWrite = WriteBold(20,"{} .   Alarm planned for:".format(i),color1,[unplannedx,plannedy])
                            plannedWrite = WriteBold(20,x,color2,[plannedx,plannedy])
                            screen.blit(plannedWrite.writeText,plannedWrite.textRect)
                            screen.blit(plannedPreWrite.writeText,plannedPreWrite.textRect)
                            plannedy+=25
                            i+=1
                    elif plannedIt >= 20 and plannedIt <= 28:
                        for x in plannedExistingAlarms:
                            plannedPreWrite = WriteBold(15,"{} .Alarm planned for:".format(i),color1,[unplannedx,plannedy])
                            plannedWrite = WriteBold(15,x,color2,[plannedx,plannedy])
                            screen.blit(plannedWrite.writeText,plannedWrite.textRect)
                            screen.blit(plannedPreWrite.writeText,plannedPreWrite.textRect)
                            plannedy+=17
                            i+=1  
                    elif plannedIt > 28:
                        pygame.draw.line(screen,col2,[480,150],[480,700],3)
                        pygame.draw.line(screen,col2,[880,150],[880,700],3)
                        plannedAlarmsLines(col1)
                        unplannedx=220
                        plannedx=400
                        secUnplannedX = 570
                        secPlannedX = 750
                        secPlannedY = 200
                        for x in plannedExistingAlarms:
                            if i>28:
                                plannedPreWrite = WriteBold(15,"{} .Alarm planned for:".format(i),color1,[secUnplannedX,secPlannedY])
                                plannedWrite = WriteBold(15,x,color2,[secPlannedX,secPlannedY])
                                screen.blit(plannedWrite.writeText,plannedWrite.textRect)
                                screen.blit(plannedPreWrite.writeText,plannedPreWrite.textRect)
                                secPlannedY+=17
                                i+=1                                 
                            else:
                                plannedPreWrite = WriteBold(15,"{} .Alarm planned for:".format(i),color1,[unplannedx,plannedy])
                                plannedWrite = WriteBold(15,x,color2,[plannedx,plannedy])
                                screen.blit(plannedWrite.writeText,plannedWrite.textRect)
                                screen.blit(plannedPreWrite.writeText,plannedPreWrite.textRect)
                                plannedy+=17
                                i+=1                                                        
                    if plannedy==200:
                        setAlarmIt = 0
                        nonePlannedWrite = WriteBold(35,"No alarms have been set",color2,[600,300])
                        screen.blit(nonePlannedWrite.writeText,nonePlannedWrite.textRect)
                    setAlarmIt = i
def plannedAlarmsMouseOverEvents():
    if DeleteAllButton:
        plannedAlarmsDeleteButton = pygame.draw.rect(screen,col2,[920,550,150,50],3)
    else:
        plannedAlarmsDeleteButton = pygame.draw.rect(screen,col3,[920,550,150,50],3)  
def plannedAlarmsScreen():
    useAdditionalScreen(col1)
    plannedAlarmsLines(col2)
    plannedAlarmsMain(col2,col3)
def plannedAlarmsClear():
    global setAlarmLimit,setAlarmIt,plannedFinal,plannedExistingAlarms
    metaClear = open(r"{}Data\userData\Meta\alarmMeta.txt".format(dir_path),"w")
    metaClear.close()
    metaClear = open(r"{}Data\userData\Meta\alarmMeta2.txt".format(dir_path),"w")
    metaClear.close()
    metaClear = open(r"{}Data\userData\wav\specmeta.txt".format(dir_path),"w")
    metaClear.close()
    setAlarmLimit = False 
    setAlarmIt = 0
    for x in plannedFinal:
        os.system(r"schtasks /delete /tn {} /f".format(x))
    plannedFinal.clear()
    plannedExistingAlarms.clear()
    resetScreen(False)
    plannedAlarmsScreen()

def settingsColorPalette(color,color2):
    pygame.draw.rect(screen,color,[190,100,800,400])
    pygame.draw.rect(screen,color2,[190,100,800,400],2)
    paletteText = WriteBold(13,"Esc to exit",color2,[950,490])
    screen.blit(paletteText.writeText,paletteText.textRect)

    global colPalCords
    colPalCords = []
    width = 90
    height = 90
    colIt = 0
    x = 220
    y = 120
    for it in range(3):
        for it2 in range(7):
            pygame.draw.rect(screen,allColors[colIt],[x,y,width,height])
            pygame.draw.rect(screen,red,[x,y,width,height],1)
            colPalCords.append(x)
            colPalCords.append(width+x)
            colPalCords.append(y)
            colPalCords.append(height+y)
            x += 110
            colIt+=1
        y += 130
        x=220
def itemsChoosingScreen(size,items_list,addCustom=True):
    pygame.draw.rect(screen,col1,[210,250,770,300])
    pygame.draw.rect(screen,col3,[210,250,770,300],3)
    x = 220
    y = 270
    for a in range(2):
        for b in range(4):
            pygame.draw.rect(screen,col2,[x,y,180,80],2)
            x+=190
        x=220
        y+=100
    names = items_list
    x=310
    y=310
    namesIt = 0
    for a in range(2):
        for b in range(4):
            picture = WriteRegular(size,names[namesIt],col2,[x,y])
            screen.blit(picture.writeText,picture.textRect)
            x+= 190
            namesIt += 1
        x=310
        y+= 100
    if addCustom:
        pygame.draw.rect(screen,col2,[545,470,100,60],2)
        custPict = WriteRegular(40,"+",col2,[595,500])
        screen.blit(custPict.writeText,custPict.textRect)
def settingsDraw(color,textColor):
    #FPS section
    pygame.draw.rect(screen,color,[200,200,700,40],3)
    pygame.draw.line(screen,color,[300,200],[300,240],3)
    pygame.draw.line(screen,color,[500,200],[500,240],3)
    pygame.draw.line(screen,color,[700,200],[700,240],3)
    
    fpsText = WriteBold(20,"FPS",textColor,[250,223])
    screen.blit(fpsText.writeText,fpsText.textRect)

    fps60 = WriteRegular(20,"60",textColor,[400,223])
    screen.blit(fps60.writeText,fps60.textRect)

    fps120 = WriteRegular(20,"120",textColor,[600,223])
    screen.blit(fps120.writeText,fps120.textRect)

    fps200 = WriteRegular(20,"200",textColor,[800,223])
    screen.blit(fps200.writeText,fps200.textRect)
    #color section
    pygame.draw.rect(screen,color,[220,270,200,50],3)
    color1Text = WriteRegular(24,"Color 1.",textColor,[320,297])
    screen.blit(color1Text.writeText,color1Text.textRect)
    
    pygame.draw.rect(screen,color,[440,270,200,50],3)
    color2Text = WriteRegular(24,"Color 2.",textColor,[540,297])
    screen.blit(color2Text.writeText,color2Text.textRect)

    pygame.draw.rect(screen,color,[660,270,200,50],3)
    color3Text = WriteRegular(24,"Color 3.",textColor,[760,297])
    screen.blit(color3Text.writeText,color3Text.textRect)
    #reset button
    if col1 != red:
        pygame.draw.rect(screen,red,[910,600,150,50],3)
        resetText = WriteRegular(16,"Reset",red,[980,625])
        screen.blit(resetText.writeText,resetText.textRect)
    else:
        pygame.draw.rect(screen,ecru,[910,600,150,50],3)
        resetText = WriteRegular(16,"Reset",ecru,[980,625])
        screen.blit(resetText.writeText,resetText.textRect)    
    #pictures section
    pygame.draw.rect(screen,color,[240,360,260,70],3)  
    bckgrText = WriteRegular(24,"Background",textColor,[370,395])
    screen.blit(bckgrText.writeText,bckgrText.textRect)

    pygame.draw.rect(screen,color,[560,360,260,70],3)   
    sdbarText = WriteRegular(24,"Side Bar",textColor,[690,395])
    screen.blit(sdbarText.writeText,sdbarText.textRect)

    pygame.draw.rect(screen,col2,[360,480,320,80],3)
    alarmSoundsText = WriteRegular(24,"Alarm sounds",textColor,[520,520])
    screen.blit(alarmSoundsText.writeText,alarmSoundsText.textRect)

def colorChanging(opt):
                        colRectList = [colRect1,colRect2,colRect3,colRect4,colRect5,colRect6,colRect7,
                        colRect8,colRect9,colRect10,colRect11,colRect12,colRect13,colRect14,colRect15,
                        colRect16,colRect17,colRect18,colRect19,colRect20,colRect21
                        ]
                                                #GLOBAL COLOR ITEMS
                        global col1,col2,col3
                        cols=[col1,col2,col3]

                        for x in colRectList:
                            if event.button == 1 and x:
                                cols[opt-1] = allColors[colRectList.index(x)]
                                writeToMeta(opt,allColors[colRectList.index(x)])
                        getFromMeta()
def pictureChanging(opt): #changing events
    global backgroundPict,sideBarPict,customPictChoose
    if opt == 4:
        for x in pos:
            if event.button == 1 and x:
                refreshPict(opt,backgrounds[pos.index(x)])
    if opt == 5:
        for x in pos:
            if event.button == 1 and x:
                refreshPict(opt,sideBars[pos.index(x)])
    if event.button == 1 and custom:
            customPictChanging(col1,col2,col3,opt)
            customPictChoose = True
    if customPictChoose:
        pass
    else:
        resetScreen(False)
def customPictChanging(col1,col2,col3,opt):
    pygame.draw.rect(screen,col1,[190,200,770,350])
    pygame.draw.rect(screen,col3,[190,200,770,350],3)
    pygame.draw.rect(screen,col3,[230,300,700,200])

    noteTitle = WriteBold(24,"Note:",col2,[230,230])
    screen.blit(noteTitle.writeText,noteTitle.textRect)
    if opt == 4:
        noteText = WriteRegular(16,r"""Make sure picture you want to set is in WakeUp!\Picts\Background""",col3,[580,230])
    elif opt == 5:
        noteText = WriteRegular(16,r"""Make sure picture you want to set is in WakeUp!\Picts\sideBar""",col3,[580,230])
    screen.blit(noteText.writeText,noteText.textRect)
    
    infoText = WriteBold(24,"Enter filename with its extension eg. picture1.jpg",col2,[520,280])
    screen.blit(infoText.writeText,infoText.textRect)

    customWriteText = WriteRegular(16,customPictText,col2,[585,320])
    screen.blit(customWriteText.writeText,customWriteText.textRect)

def soundChanging():
    global changingSound,afterReset
    for x in pos:
        if event.button == 1 and x:
            openMeta = open(r"{}Data\userData\Meta\meta{}p.txt".format(dir_path,6),"w")
            openMeta.write(cipher("{}.wav".format(sounds[pos.index(x)])))
            openMeta.close()
            changingSound = False
            afterReset = True
            resetScreen(True)
            settingsDraw(col2,col3)

def customPictChooseEscape():
    global customPictChoose,sideBarChoose,backgroundChoose,customPictText,settings
    customPictChoose = False
    sideBarChoose = False
    backgroundChoose = False
    resetScreen(True)
    settingsDraw(col2,col3)
    customPictText = ""
    settings = True
def customPictChooseAddChar():
    global customPictText,pictureChangingOpt,col1,col2,col3
    if len(customPictText) > 40:
        pass
    else:
        try:
            customPictText += event.unicode
            customPictChanging(col1,col2,col3,pictureChangingOpt)
        except:
            pass
def customPictChooseEnter():
    global pictureChangingOpt,customPictText,customPictChoose,sideBarChoose,backgroundChoose,customPictText
    writeToMeta_P(pictureChangingOpt,customPictText)
    getFromMeta()
    resetScreen(False)
    customPictChoose = False
    sideBarChoose = False
    backgroundChoose = False
    resetScreen(False)
    customPictText = ""
def customPictChooseBackspace():
    global customPictText,pictureChangingOpt
    customPictText = str(customPictText)[:-1]
    customPictChanging(col1,col2,col3,pictureChangingOpt)

def setDateAddChar():
    global setAlarmSetDateDayChoosing,setAlarmSetDateMonthChoosing
    global setDateMonth,setDateDay, addNoteEvents
    if setAlarmSetDateDayChoosing:
        if len(setDateDay) >= 2:
            setDateDay = ""
        setDateDay += event.unicode
        setAlarmSetDateReset("day")
    elif  setAlarmSetDateMonthChoosing:
        if len(setDateMonth) >= 2:
            setDateMonth = ""
        setDateMonth += event.unicode
        setAlarmSetDateReset("month")
def setDateBackspace():
    global setAlarmSetDateDayChoosing,setAlarmSetDateMonthChoosing
    global setDateDay,setDateMonth,addNoteEvents

    if setAlarmSetDateDayChoosing and not addNoteEvents:
        setDateDay = str(setDateDay)[:-1]
        setAlarmSetDateReset("day")
    elif setAlarmSetDateMonthChoosing and not addNoteEvents:
        setDateMonth = str(setDateMonth)[:-1]
        setAlarmSetDateReset("month")

def addNoteAddChar():
    global noteText,noteTextList
    if len(noteTextList) < 14:
        if len(noteText) < 16:
            noteText += event.unicode
            setAlarmAddNoteDraw()
        else:
            noteText += event.unicode
            setAlarmAddNoteDraw()
            noteTextList.append(noteText)
            noteText = ""
def addNoteBackspace():
    global noteText,noteTextList
    if len(noteText) > 0:
        noteText = noteText[:-1]
        setAlarmAddNoteDraw()
    else:
        try:
            noteTextList.pop(len(noteTextList)-1)
            setAlarmAddNoteDraw()
        except:
            pass


def resetScreen(truetoDrawAddictScreen):
        useMainScreen()
        opt1Text(col1,col2)
        opt2Text(col1,col2)
        opt3Text(col1,col2)
        opt4Text(col1,col2)
        if truetoDrawAddictScreen:
                useAdditionalScreen(col1)
def checkScreen(color1,color2,color3):
    pygame.draw.rect(screen,color1,[250,300,600,300])
    pygame.draw.rect(screen,color3,[250,300,600,300],3)

    firstText = WriteRegular(24,"Are you sure?",color2,[550,350])
    screen.blit(firstText.writeText,firstText.textRect)

    if col1==col2==col3:
        for x in allColors:
            if x != col1:
                color = x
                break
        sucButt = pygame.draw.rect(screen,color,[350,425,170,100],2)
        sucButtText = WriteBold(36,"Yes",color,[435,475])
        screen.blit(sucButtText.writeText,sucButtText.textRect)
        falsButt = pygame.draw.rect(screen,color,[570,425,170,100],2)
        falsButtText = WriteBold(36,"No",color,[655,475])
        screen.blit(falsButtText.writeText,falsButtText.textRect)        
    else:
        sucButt = pygame.draw.rect(screen,color2,[350,425,170,100],2)
        sucButtText = WriteBold(36,"Yes",color2,[435,475])
        screen.blit(sucButtText.writeText,sucButtText.textRect)
        falsButt = pygame.draw.rect(screen,color2,[570,425,170,100],2)
        falsButtText = WriteBold(36,"No",color2,[655,475])
        screen.blit(falsButtText.writeText,falsButtText.textRect)
def refreshPict(opt,val):
    writeToMeta_P(opt,val)
    getFromMeta()
    resetScreen(False)


#Setting needed values
now = str(datetime.now())
nowDay = now[8:-16]
nowMonth = now[5:-19]
nowHour = now[11:-10]

resetScreen(False)

running = True
sideBarEvents = True

setAlarm = False
setAlarmIt = 0
setAlarmSetDate = False
setAlarmSetDateDayChoosing = False
setAlarmSetDateMonthChoosing = False
setAlarmSetDateToday = False
setDateDay = str(nowDay)
setDateMonth = str(nowMonth)
noteText=""
noteTextList =[]
addNoteEvents = False
soundOn = True

plannedAlarms = False

settings = False

colorPalette = False
col1Palette = False
col2Palette = False
col3Palette = False

isCheckScreen = False
afterReset = False

backgroundChoose = False
sideBarChoose = False
customPictChoose = False
changingSound = False
pictureChangingOpt = 0
customPictText = ""


while running:

    counter(str(int(clock.get_fps())),1070,0,30,30)

    mouse_pos = pygame.mouse.get_pos() 
    clock.tick(fps)
    #pos
    #SIDE BAR
    addictExitButton = mouse_pos[0] in list(range(1050,1100)) and mouse_pos[1] in list(range(151,201))
    setAlarmSuccBut = mouse_pos[0] in list(range(900,1000)) and mouse_pos[1] in list(range(440,520))
    #SET ALARM
    #clock
    setAlarmHUp1 = mouse_pos[0] in list(range(460,510)) and mouse_pos[1] in list(range(260,340))
    setAlarmHUp2 = mouse_pos[0] in list(range(510,560)) and mouse_pos[1] in list(range(260,340))
    setAlarmMUp1 = mouse_pos[0] in list(range(590,640)) and mouse_pos[1] in list(range(260,340))
    setAlarmMUp2 = mouse_pos[0] in list(range(640,690)) and mouse_pos[1] in list(range(260,340))
    setAlarmHDown1 = mouse_pos[0] in list(range(460,510)) and mouse_pos[1] in list(range(440,520))
    setAlarmHDown2 = mouse_pos[0] in list(range(510,560)) and mouse_pos[1] in list(range(440,520))
    setAlarmMDown1 = mouse_pos[0] in list(range(590,640)) and mouse_pos[1] in list(range(440,520))
    setAlarmMDown2 = mouse_pos[0] in list(range(640,690)) and mouse_pos[1] in list(range(440,520))
    #date
    setAlarmDateButton = mouse_pos[0] in list(range(520,670)) and mouse_pos[1] in list(range(600,650)) 
    setAlarmDateButton_Back = mouse_pos[0] in list(range(890,990)) and mouse_pos[1] in list(range(575,645))
    setAlarmSetDateLeft = mouse_pos[0] in list(range(240,440)) and mouse_pos[1] in list(range(575,645)) 
    setAlarmSetDateCenter = mouse_pos[0] in list(range(450,650)) and mouse_pos[1] in list(range(575,645))
    setAlarmSetDateRight = mouse_pos[0] in list(range(660,860)) and mouse_pos[1] in list(range(575,645))
    #Add note
    addNotePos = mouse_pos[0] in list(range(160,260)) and mouse_pos[1] in list(range(180,230))
    addNoteButtonXPos = mouse_pos[0] in list(range(360,410)) and mouse_pos[1] in list(range(199,249))
    #PLANNED ALARMS
    DeleteAllButton = mouse_pos[0] in list(range(920,1070)) and mouse_pos[1] in list(range(550,600))
    settingsColor1 = mouse_pos[0] in list(range(220,420)) and mouse_pos[1] in list(range(270,320))
    settingsColor2 = mouse_pos[0] in list(range(440,640)) and mouse_pos[1] in list(range(270,320))
    settingsColor3 = mouse_pos[0] in list(range(660,860)) and mouse_pos[1] in list(range(270,320))
    #SETTINGS
    #fps
    fps60 = mouse_pos[0] in list(range(300,500)) and mouse_pos[1] in list(range(200,240))
    fps120 = mouse_pos[0] in list(range(500,700)) and mouse_pos[1] in list(range(200,240))
    fps200 = mouse_pos[0] in list(range(700,900)) and mouse_pos[1] in list(range(200,240))
    #colors
    colRect1 = mouse_pos[0] in list(range(220,310)) and mouse_pos[1] in list(range(120,210))
    colRect2 = mouse_pos[0] in list(range(330,420)) and mouse_pos[1] in list(range(120,210))
    colRect3 = mouse_pos[0] in list(range(440,530)) and mouse_pos[1] in list(range(120,210))
    colRect4 = mouse_pos[0] in list(range(550,640)) and mouse_pos[1] in list(range(120,210))
    colRect5 = mouse_pos[0] in list(range(660,750)) and mouse_pos[1] in list(range(120,210))
    colRect6 = mouse_pos[0] in list(range(770,860)) and mouse_pos[1] in list(range(120,210))
    colRect7 = mouse_pos[0] in list(range(880,970)) and mouse_pos[1] in list(range(120,210))
    colRect8 = mouse_pos[0] in list(range(220,310)) and mouse_pos[1] in list(range(250,340))
    colRect9 = mouse_pos[0] in list(range(330,420)) and mouse_pos[1] in list(range(250,340))
    colRect10 = mouse_pos[0] in list(range(440,530)) and mouse_pos[1] in list(range(250,340))
    colRect11 = mouse_pos[0] in list(range(550,640)) and mouse_pos[1] in list(range(250,340))
    colRect12 = mouse_pos[0] in list(range(660,750)) and mouse_pos[1] in list(range(250,340))
    colRect13 = mouse_pos[0] in list(range(770,860)) and mouse_pos[1] in list(range(250,340))
    colRect14 = mouse_pos[0] in list(range(880,970)) and mouse_pos[1] in list(range(250,340))
    colRect15 = mouse_pos[0] in list(range(220,310)) and mouse_pos[1] in list(range(380,470))
    colRect16 = mouse_pos[0] in list(range(330,420)) and mouse_pos[1] in list(range(380,470))
    colRect17 = mouse_pos[0] in list(range(440,530)) and mouse_pos[1] in list(range(380,470))
    colRect18 = mouse_pos[0] in list(range(550,640)) and mouse_pos[1] in list(range(380,470))
    colRect19 = mouse_pos[0] in list(range(660,750)) and mouse_pos[1] in list(range(380,470))
    colRect20 = mouse_pos[0] in list(range(770,860)) and mouse_pos[1] in list(range(380,470))
    colRect21 = mouse_pos[0] in list(range(880,970)) and mouse_pos[1] in list(range(380,470))
    #Alarm sounds
    changeAlarmSoundPos = mouse_pos[0] in list(range(360,680)) and mouse_pos[1] in list(range(480,560))
    #reset
    resetButton = mouse_pos[0] in list(range(905,1060)) and mouse_pos[1] in list(range(600,650))
    #checkScreen
    succCheckPos = mouse_pos[0] in list(range(350,520)) and mouse_pos[1] in list(range(425,525))
    falsCheckPos = mouse_pos[0] in list(range(570,740)) and mouse_pos[1] in list(range(425,525))
    #pictures
    backgroundPos = mouse_pos[0] in list(range(240,500)) and mouse_pos[1] in list(range(360,430))
    sideBarPos = mouse_pos[0] in list(range(560,820)) and mouse_pos[1] in list(range(360,430))
    #Items Choosing Screen
    item1 = mouse_pos[0] in list(range(220,400)) and mouse_pos[1] in list(range(270,350))
    item2 = mouse_pos[0] in list(range(410,590)) and mouse_pos[1] in list(range(270,350))
    item3 = mouse_pos[0] in list(range(600,780)) and mouse_pos[1] in list(range(270,350))
    item4 = mouse_pos[0] in list(range(790,970)) and mouse_pos[1] in list(range(270,350))
    item5 = mouse_pos[0] in list(range(220,400)) and mouse_pos[1] in list(range(370,450))
    item6 = mouse_pos[0] in list(range(410,590)) and mouse_pos[1] in list(range(370,450))
    item7 = mouse_pos[0] in list(range(600,780)) and mouse_pos[1] in list(range(370,450))
    item8 = mouse_pos[0] in list(range(790,970)) and mouse_pos[1] in list(range(370,450))
    pos = [item1,item2,item3,item4,item5,item6,item7,item8]
    custom = mouse_pos[0] in list(range(545,645)) and mouse_pos[1] in list(range(470,530))  


    for event in pygame.event.get():

        counter(mouse_pos,940,0,100,30)
        
        if event.type == MOUSEMOTION:
            #SIDE BAR COLOR CHANGE ON MOUSEMOTION
            optsMouseOverEvents()
            #SET ALARM MOUSEMOTION EVENTS
            if setAlarm:
                setAlarmMouseMotionEvents()
            if plannedAlarms:
                plannedAlarmsMouseOverEvents()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if setAlarm or plannedAlarms or settings or backgroundChoose or sideBarChoose or changingSound or afterReset:
                if addictExitButton and event.button == 1: #Closing Addictional Screen by X
                    setAlarm = False
                    setAlarmSetDate = False
                    setAlarmSetDateDayChoosing = False
                    setAlarmSetDateMonthChoosing = False
                    addNoteEvents = False
                    plannedAlarms = False
                    settings = False
                    changingSound = False
                    afterReset = False
                    resetScreen(False)
                    #zeroing setAlarm values
                    hour1 = "0"
                    hour2 = "0"
                    min1 = "0"
                    min2 = "0"
                    setDateDay = ""
                    setDateMonth = ""
                    noteText = ""
                    noteTextList = []
            if sideBarOpt1.collidepoint(mouse_pos) and sideBarEvents and event.button == 1: #Set Alarm
                colorPalette = False
                changingSound = False
                setAlarm = True
                plannedAlarms = False
                settings = False
                afterReset = False
                backgroundChoose = False
                sideBarChoose = False
                resetScreen(False)
            if setAlarm: 
                setAlarmClockClickEvents()
                setAlarmButtonAction()
            if sideBarOpt2.collidepoint(mouse_pos) and sideBarEvents and event.button == 1:
                if colorPalette:
                    resetScreen(False)
                colorPalette = False
                backgroundChoose = False
                sideBarChoose = False
                plannedAlarms = True
                setAlarm = False
                settings = False
                sideBarEvents = False
                afterReset = False
                changingSound = False
                if plannedAlarms:
                    plannedAlarmsScreen() 
                sideBarEvents = True
            if plannedAlarms and DeleteAllButton and event.button == 1: #plannedAlarms Delete All
                plannedAlarmsClear()
            if sideBarOpt3.collidepoint(mouse_pos) and sideBarEvents and event.button == 1:
                settings = True
                setAlarm = False
                plannedAlarms = False
                colorPalette = False
                afterReset = False
                resetScreen(False)
            if afterReset:
                settings = True
                afterReset = False
            if colorPalette:
                if col1Palette:
                    colorChanging(1)
                    resetScreen(False)
                    colorPalette = False  
                    col1Palette = False
                if col2Palette: 
                    colorChanging(2)
                    resetScreen(False)
                    colorPalette = False  
                    col2Palette = False
                if col3Palette: 
                    colorChanging(3)
                    resetScreen(False)
                    colorPalette = False  
                    col3Palette = False
            if isCheckScreen:
                if event.button ==1 and succCheckPos:
                    fps = 60
                    resetMeta()
                    getFromMeta()
                    resetScreen(True)
                    settingsDraw(col2,col3)  
                    isCheckScreen = False
                    afterReset = True
                if event.button == 1 and falsCheckPos:
                    resetScreen(True)
                    settingsDraw(col2,col3)
                    isCheckScreen=False
                    afterReset = True
            if backgroundChoose and not settings:
                pictureChanging(4)
                pictureChangingOpt = 4
                backgroundChoose = False
            if sideBarChoose and not settings:
                pictureChanging(5)    
                pictureChangingOpt = 5
                sideBarChoose = False
            if changingSound and not settings:
                soundChanging()
                #HERE SOUND SETTINGS
            if settings and not colorPalette: #here settings
                useAdditionalScreen(col1)
                settingsDraw(col2,col3)
                #pictures
                if changeAlarmSoundPos and event.button == 1:
                    changingSound = True
                    settings = False
                    itemsChoosingScreen(24,sounds,False)
                if backgroundPos and event.button ==1:
                    backgroundChoose = True
                    settings = False
                    itemsChoosingScreen(24,backgrounds)
                if sideBarPos and event.button == 1:
                    sideBarChoose = True
                    settings = False
                    itemsChoosingScreen(18,sideBars)
                #reset
                if resetButton and event.button == 1:
                    isCheckScreen = True
                    settings = False
                    checkScreen(col1,col2,col3)
                #fps
                setFps()
                #col
                if settings and settingsColor1 and event.button == 1: 
                    settingsColorPalette(col1,col3)
                    colorPalette = True
                    col1Palette = True   
                    settings = False              
                if settings and settingsColor2 and event.button == 1:
                    settingsColorPalette(col1,col3)
                    colorPalette = True
                    col2Palette = True
                    settings = False
                if settings and settingsColor3 and event.button == 1:
                    settingsColorPalette(col1,col3)
                    colorPalette = True
                    col3Palette = True
                    settings = False
            #QUIT
            if sideBarOpt4.collidepoint(mouse_pos) and event.button == 1:
                running = False
        elif event.type == pygame.KEYDOWN:
            if colorPalette and event.key==pygame.K_ESCAPE:
                settings = True
                colorPalette = False
                resetScreen(True)
                col1Palette = False
                col2Palette = False
                col3Palette = False
                settingsDraw(col2,col3)
            elif backgroundChoose or sideBarChoose and event.key == K_ESCAPE:
                backgroundChoose = False
                sideBarChoose = False
                customPictChoose = False
                resetScreen(True)
                settingsDraw(col2,col3)
                pictureChangingOpt = 0
                settings = True
            elif changingSound and event.key == K_ESCAPE:
                changingSound = False
                resetScreen(True)
                settingsDraw(col2,col3)
                settings = True
            elif customPictChoose:
                if event.key == K_ESCAPE: 
                    customPictChooseEscape()
                elif event.key == K_BACKSPACE:
                    customPictChooseBackspace()
                elif event.key == K_RETURN:
                    customPictChooseEnter()
                else:
                    customPictChooseAddChar()
            elif setAlarmSetDate:
                if event.key == K_BACKSPACE:
                    setDateBackspace()
                else:
                    setDateAddChar()
            if addNoteEvents and not setAlarmSetDateDayChoosing and not setAlarmSetDateMonthChoosing and setAlarm:
                if event.key == K_BACKSPACE:
                    addNoteBackspace()
                else:
                    addNoteAddChar()
        elif event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
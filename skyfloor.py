import signal
import os
from os import system,name
import time
import random
import math
from colorama import Fore, Back, Style
'''from colorama import init, Fore
init()
'''
from obstacles import obstacles,obstacle1,obstacle2,obstacle3,coins,magnet,speedbooster
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from board import board
from mario import player
from scenery import skyfloor
from dragon import dragon
'''from enemy import Enemy, BossEnemy
from config import Config'''
rr=50
cc=102

tt=0
#os.system('clear')
board_obj=board(rr,2002)
board_obj.createboard()
board_obj.createobs()
screen=board_obj.get_screen()
obs1=board_obj.get_obs1()

obs2=board_obj.get_obs2()
#board_obj.update(0)
skyfloor_obj=skyfloor(screen)
skyfloor_obj.createsky(screen)
skyfloor_obj.createfloor(screen)
drobj=dragon(6,940,screen)
i=0

while i<650:
    i=i+random.randint(70,100)
    j=i+random.randint(15,25)
    k=i+random.randint(30,60)
    x1=random.randint(15,20)
    x2=random.randint(26,44)
    x3=random.randint(4,20)
    x4=random.randint(30,40)
    r1=random.randint(1,3)
    r2=random.randint(1,3)
    r3=random.randint(1,4)
    rr=random.randint(1,2)
    if rr==1:
        x1=random.randint(15,20)
    else:
        x1=random.randint(4,20)
    if(r1==1):
        obstacles_obj=obstacle1(x1,i,screen,obs1,obs2)
        obstacles_obj.createobstacle(screen,obs1,obs2)
    if(r1==2):
        obstacles_obj=obstacle2(x1,i,screen,obs1,obs2)
        obstacles_obj.createobstacle(screen,obs1,obs2)
    if(r1==3):
        obstacles_obj=obstacle3(x1,i,screen,obs1,obs2)
        obstacles_obj.createobstacle(screen,obs1,obs2)
    
    #obstacles_obj1=obstacles(x2,i)
    if(r2==1):
        obstacles_obj1=obstacle1(x2,i,screen,obs1,obs2)
        obstacles_obj1.createobstacle(screen,obs1,obs2)
    if(r2==2):
        obstacles_obj1=obstacle2(x2,i,screen,obs1,obs2)
        obstacles_obj1.createobstacle(screen,obs1,obs2)
    if(r2==3):
        obstacles_obj1=obstacle3(x2,i,screen,obs1,obs2)
        obstacles_obj1.createobstacle(screen,obs1,obs2)
    
    
    #obstacles_obj2=obstacles(x1,j)
    
    if(r3==1):
            obstacles_obj2=coins(x3,j,screen,obs1,obs2)
            obstacles_obj2.createcoins1(screen,obs1,obs2)
    if(r3==2):
            obstacles_obj2=coins(x3,j,screen,obs1,obs2)
            obstacles_obj2.createcoins2(screen,obs1,obs2)
    if(r3==3):
            obstacles_obj2=coins(x3,j,screen,obs1,obs2)
            obstacles_obj2.createcoins3(screen,obs1,obs2)
    if(r3==4):
            obstacles_obj2=coins(x3,j,screen,obs1,obs2)
            obstacles_obj2.createcoins4(screen,obs1,obs2)
    if(r3==1):
            obstacles_obj2=coins(x4,j,screen,obs1,obs2)
            obstacles_obj2.createcoins1(screen,obs1,obs2)
    if(r3==2):
            obstacles_obj2=coins(x4,j,screen,obs1,obs2)
            obstacles_obj2.createcoins2(screen,obs1,obs2)
    if(r3==3):
            obstacles_obj2=coins(x4,j,screen,obs1,obs2)
            obstacles_obj2.createcoins3(screen,obs1,obs2)
    if(r3==4):
            obstacles_obj2=coins(x4,j,screen,obs1,obs2)
            obstacles_obj2.createcoins4(screen,obs1,obs2)
    if rr==1:
        #print(x1,j)
        obstacles_obj2=magnet(x1,k,screen,obs1,obs2)
        obstacles_obj2.createobstacle(screen,board_obj.sc1,obs1,obs2)
    if rr==2:
        obstacles_obj2=speedbooster(x1,k,screen,obs1,obs2)
        obstacles_obj2.createobstacle(screen,obs1,obs2)

#print('\033[0;0H')

player_obj=player(27,0,screen)
player_obj.updatescreen(screen)
#board_obj.printscreen(0)
#os.system('clear')
#tt=1
#def get_tt():
#    return tt
#def set_tt(v):

#tt=v
def moveplayer(v,t):
        def alarmhandler(signum, frame):
                raise AlarmException

        def user_input(timeout=0.1):
                ''' input method '''
                signal.signal(signal.SIGALRM, alarmhandler)
                signal.setitimer(signal.ITIMER_REAL, timeout)

                try:
                        text = getChar()()
                        signal.alarm(0)
                        return text
                except AlarmException:
                        pass
                signal.signal(signal.SIGALRM, signal.SIG_IGN)
                return ''

        ch = user_input()
        #ch='d'
        f=t
        if ch=='a':
            valid=1
           # f=-1
            if valid==1:
                obstacles_obj=obstacles(0,0,screen,obs1,obs2)
                player_obj.changepos(1,screen,v,board_obj.sc1,obstacles_obj,obs1,obs2)
                player_obj.changepos(1,screen,v,board_obj.sc1,obstacles_obj,obs1,obs2)
         # time.sleep(0.01)
        if ch=='d':
            valid=1
            #tt=0
          #  f=-1
            if valid==1:
                obstacles_obj=obstacles(0,0,screen,obs1,obs2)
                player_obj.changepos(2,screen,v,board_obj.sc1,obstacles_obj,obs1,obs2)
            #time.sleep(0.01)
        if ch=='w':
            valid=1
            global tt
            tt=0
            f=-1
            if valid==1:
                obstacles_obj=obstacles(0,0,screen,obs1,obs2)
                player_obj.changepos(3,screen,v,board_obj.sc1,obstacles_obj,obs1,obs2)
           # time.sleep(0.01)
        if ch=='b':
            valid=1
           # f=-1
            if valid==1:
                player_obj.createbullet()


        if ch==' ':
            valid=1
           # f=-1;
            if valid==1:
                #print(player_obj.cansh())
                player_obj.shield(1)
        if f==0:
            valid=1
            #time.sleep(0.01)
            obstacles_obj=obstacles(0,0,screen,obs1,obs2)
            if valid==1 and tt>0 :
                pp=tt
                dd=(pp*pp)-((pp-1)*(pp-1))
                dd=math.floor(dd)

                for i in range(dd):
                    player_obj.changepos(4,screen,v,board_obj.sc1,obstacles_obj,obs1,obs2)
        
        if ch=='q':
            quit()

t=0
v=0
x=round(time.time())
st=0
co=0
k=1
en=0
ff=0
prr=0
speedst=-1
speedend=0
os.system('clear')
py=0
while True:
    #print('\033[0;0H')
    #if v<798:
    #os.system('clear')
    obstacles_obj=obstacles(0,0,screen,obs1,obs2)

    y=round(time.time())-x
    if y-py>=1:
        tt=tt+1
    #    set_tt(pp+1)
    #    print('hello') 
    sc1=board_obj.sc1
    xx=player_obj.get_xpos()
    yy=player_obj.get_ypos()
    #if sc1[xx][yy]=='L':
    #    tt=0
    #if sc1[xx][yy]=='R':
    
    #tt=0
    #if sc1[xx][yy]=='U':
    #    tt=0
    #if sc1[xx][yy]=='D':
    #    tt=0
    if sc1[xx][yy]=='P':
        tt=0
    if sc1[xx][yy]=='K':
        tt=0 
    player_obj.changepos(0,screen,v,board_obj.sc1,obstacles_obj,obs1,obs2)
    #player_obj.changepos(0,screen,v,board_obj.sc1,obstacles_obj,obs1,obs2)
    #player_obj.changepos(0,screen,v,board_obj.sc1)
    #player_obj.changepos(0,screen,v,board_obj.sc1)
    moveplayer(v,t%2)
    py=y
    #timeout=0.2
    #signal.setitimer(signal.ITIMER_REAL, timeout)

    obstacles_obj=obstacles(0,0,screen,obs1,obs2)
    player_obj.movebullets(screen,v,obstacles_obj,obs1,obs2,drobj)
    player_obj.movebullets(screen,v,obstacles_obj,obs1,obs2,drobj)    
    player_obj.movebullets(screen,v,obstacles_obj,obs1,obs2,drobj)
   # y=round(time.time())-x

    if(y-prr>=2and player_obj.get_ypos() > 800):
        drobj.createbullet(player_obj)
        prr=y
    if v>798 or player_obj.get_ypos()>860:
        drobj.movedragon(player_obj.get_xpos(),screen)
        drobj.printdragon(screen)
        drobj.movebullets(screen,player_obj)
        drobj.movebullets(screen,player_obj)
        drobj.movebullets(screen,player_obj)
    print('\033[0;0H')
    board_obj.printscreen(v)
    
    #y=round(time.time())-x

    if y-speedst>=5 and player_obj.get_sb()==1 and speedst!=-1:
        player_obj.set_sb()
        speedst=-1

    #print('\033[0;0H')
    print(' TIME REMAINING: ',200-y,end='\t \t')
    
    
    print("COINS:",player_obj.get_coins(), end = '\t \t')
    print("LIVES:",player_obj.get_lives(),end='\t \t')
    if(player_obj.get_shield()==1):
        if co==0:
            st=y
            co=1
            
        ff=1     
        print("SHIELD ACTIVATED  ",end='\t \t')
        print("                  " ,end='\t \t')
    else:
        
        print("SHIELD DEACTIVATED",end='\t \t')
        p=30-(y-en)
        if p>0 and ff!=0:
            print("SHIELD REFILL IN ",p,end='\t \t')
        else:
            print("SHIELD REFILLED   " ,end='\t \t')
    if v>798:
        print("DRAGON LIVES: ",drobj.get_lives(),end='\t \t')
    if v<798:
        if(player_obj.get_sb()==1):
            if speedst==-1:
                speedst=y
            print("SPEED BOOSTER ACTIVATED  ",end='\t \t')
        else:
            print("SPEED BOOSTER DEACTIVATED",end='\t \t')
        

    print()
    
    #board_obj.printscreen(v)
    if y-st >=10 and player_obj.get_shield()==1:
        player_obj.shield(0)
        co=0
        en=y
        player_obj.set_canuseshield(0)
        #print("hello")


    if player_obj.get_canuseshield()==0 and y-en >= 30 and player_obj.get_shield()==0:
        #print("hello")
        player_obj.set_canuseshield(1)
        co=0
    
    t=t+1 
   # print('\033[0;0H')

    if(t%2==0):
        if player_obj.get_sb()==1:
            dd=5
        else:
            dd=2
        if v<800:
            v=v+dd
        player_obj.checkleft(v,screen)
        if v<798:
            for i in range(dd):
                obstacles_obj=obstacles(0,0,screen,obs1,obs2)

                player_obj.changepos(2,screen,v,board_obj.sc1,obstacles_obj,obs1,obs2)
            #player_obj.changepos(2,screen,v,board_obj.sc1)
            # player_obj.changepos(2,screen,v,board_obj.sc1)


import random
import os
from os import system,name
import time
rr=50
class player:

    def __init__(self,x,y,screen):
        self.__xpos=x
        self.__ypos=y
        self.__coins=0
        self.__shape=[[' ','#',' '],[' ','#',' '],['#',' ','#']]
        self.__shield=0
        self.__canuseshield=1
        self.__lives=5
        self.__lst1=[]
        self.__lst2=[]
        self.__sb=0
        self.__screen=screen

    def collision(self,ch):
        if(ch=='_' or ch=='|' or ch=='/'):
            return 1
        else:
         return 0
    def set_sb(self):
        self.__sb=0
    def get_lives(self):
        return self.__lives
    def coins(self,ch):
        if(ch=='*'):
            return 1
        else:
            return 0
    def sb(self,ch):
        if(ch=='%'):
            return 1
        else:
            return 0
    def get_sb(self):
        return self.__sb

    def kill(self):
        self.__lives=self.__lives-1
        if(self.__lives==0):
            os.system('clear')
            print('YOU LOSE:',end='\t \t')
            print('SCORE:',self.__coins)
            quit()
    def get_xpos(self):
        return self.__xpos
    def get_ypos(self):
        return self.__ypos
    def shield(self,h):
        if h==1 and self.__canuseshield==1:
            self.__shield=1
            #print("hello")
        else:
            self.__shield=0
    def set_canuseshield(self,k):
        if k==1:
            self.__canuseshield=1
        else: 
            self.__canuseshield=0
    
    def get_canuseshield(self):
        return self.__canuseshield


    def get_shield(self):
        return self.__shield
    def get_coins(self):
        return self.__coins
    
    def changepos(self,t,screen1,v,sc1,obj,obs1,obs2):
        xx=self.__xpos
        yy=self.__ypos
        kk=0 
        if t==0:
            if sc1[xx][yy]=='L':
                t=1
            if sc1[xx][yy]=='R':
                t=2

            if sc1[xx][yy]=='U':
                t=3
            if sc1[xx][yy]=='D':
                t=4
            if sc1[xx][yy]=='P':
                t=2
                kk=-1
            if sc1[xx][yy]=='K':
                t=1
                kk=-1


        if t==1 and yy>v:
            xx=self.__xpos
            yy=self.__ypos
            self.__xpos=xx
            self.__ypos=yy-1
            if(self.__shield ==0):

                if (self.collision(self.__screen[xx][yy-1])==1 or self.collision(self.__screen[xx+1][yy-1])==1 or self.collision(self.__screen[xx+2][yy-1])==1 ):
                #print(self.__coins)
                    self.__lives=self.__lives-1
                    obj.destroyobstacle(self.__screen,obs1[xx][yy-1],obs2[xx][yy-1])
                    obj.destroyobstacle(self.__screen,obs1[xx+1][yy-1],obs2[xx+1][yy-1])
                    obj.destroyobstacle(self.__screen,obs1[xx+2][yy-1],obs2[xx+2][yy-1])
                    time.sleep(1)
                    os.system('clear')
                    #sleep(2)
                    #v=0
                    if(self.__lives==0):
                        os.system('clear')
                        print('YOU LOSE:',end='\t \t')
                        print('SCORE:',self.__coins)
                        quit() 
            if self.coins(self.__screen[xx][yy-1])==1:
                self.__coins=self.__coins+1
            if self.coins(self.__screen[xx+1][yy-1])==1 :
                self.__coins=self.__coins+1
            if self.coins(self.__screen[xx+2][yy-1])==1 :

                self.__coins=self.__coins+1
            
            if (self.sb(self.__screen[xx][yy-1])==1 or self.sb(self.__screen[xx+1][yy-1])==1 or self.sb(self.__screen[xx+2][yy-1])==1 ):
                self.__sb=1
                obj.destroyobstacle(self.__screen,obs1[xx][yy-1],obs2[xx][yy-1])
                obj.destroyobstacle(self.__screen,obs1[xx+1][yy-1],obs2[xx+1][yy-1])
                obj.destroyobstacle(self.__screen,obs1[xx+2][yy-1],obs2[xx+2][yy-1])
            
            ch='#'
            if self.__shield ==1:
                ch='@'

            
            if self.__screen[xx][yy-1]!='M' and self.__screen[xx+1][yy-1]!='M' and self.__screen[xx+2][yy-1]!='M':            
                self.__screen[xx][yy-1]=ch
                self.__screen[xx+1][yy-1]=ch
                self.__screen[xx+2][yy-1]=ch
                self.__screen[xx][yy+2]=' '
                self.__screen[xx+1][yy+2]=' '
                self.__screen[xx+2][yy+2]=' '
            
            else:
                self.__xpos=xx
                self.__ypos=yy



        if t==2 and yy+2<v+198 and yy<930:
            xx=self.__xpos
            yy=self.__ypos
            self.__xpos=xx
            self.__ypos=yy+1
            if(self.__shield ==0):

                if (self.collision(self.__screen[xx][yy+3])==1 or self.collision(self.__screen[xx+1][yy+3])==1 or self.collision(self.__screen[xx+2][yy+3])==1 ):
                    self.__lives=self.__lives-1
                    #v=0
                    obj.destroyobstacle(self.__screen,obs1[xx][yy+3],obs2[xx][yy+3])
                    obj.destroyobstacle(self.__screen,obs1[xx+1][yy+3],obs2[xx+1][yy+3])
                    obj.destroyobstacle(self.__screen,obs1[xx+2][yy+3],obs2[xx+2][yy+3])
                    time.sleep(1)
                    os.system('clear')
                    if(self.__lives==0):
                        os.system('clear')
                        print('YOU LOSE:',end='\t \t')
                        print('SCORE:',self.__coins)
                        quit()
            if self.coins(self.__screen[xx][yy+3])==1:
                self.__coins=self.__coins+1
            if self.coins(self.__screen[xx+1][yy+3])==1 :
                self.__coins=self.__coins+1
            if self.coins(self.__screen[xx+2][yy+3])==1 :

                self.__coins=self.__coins+1
            if (self.sb(self.__screen[xx][yy+3])==1 or self.sb(self.__screen[xx+1][yy+3])==1 or self.sb(self.__screen[xx+2][yy+3])==1 ):
                self.__sb=1
                obj.destroyobstacle(self.__screen,obs1[xx][yy+3],obs2[xx][yy+3])
                obj.destroyobstacle(self.__screen,obs1[xx+1][yy+3],obs2[xx+1][yy+3])
                obj.destroyobstacle(self.__screen,obs1[xx+2][yy+3],obs2[xx+2][yy+3])
            ch='#'
            if self.__shield ==1:
                ch='@'
            
            if self.__screen[xx][yy+3]!='M' and self.__screen[xx+1][yy+3]!='M' and self.__screen[xx+2][yy+3]!='M':
                self.__screen[xx][yy]=' '
                self.__screen[xx+1][yy]=' '
                self.__screen[xx+2][yy]=' '
                self.__screen[xx][yy+3]=ch
                self.__screen[xx+1][yy+3]=ch
                self.__screen[xx+2][yy+3]=ch
            else:
                self.__xpos=xx
                self.__ypos=yy
        
        
            #if kk==-1 and t==2:
        
        if t==2 or t==1:
            if kk==-1:
                t=3
         
        if t==3 and xx >3:
            xx=self.__xpos
            yy=self.__ypos     
            self.__xpos=xx-1
            self.__ypos=yy
            
            if(self.__shield ==0):

                if (self.collision(self.__screen[xx-1][yy])==1 or self.collision(self.__screen[xx-1][yy+1])==1 or self.collision(self.__screen[xx-1][yy+2])==1 ):
                #print(self.__coins)
                    obj.destroyobstacle(self.__screen,obs1[xx-1][yy],obs2[xx-1][yy])
                    obj.destroyobstacle(self.__screen,obs1[xx-1][yy+1],obs2[xx-1][yy+1])
                    obj.destroyobstacle(self.__screen,obs1[xx-1][yy+2],obs2[xx-1][yy+2])
                    time.sleep(1)
                    os.system('clear')
                    self.__lives=self.__lives-1
                    #os.system('clear')
                    #sleep(2)
                    #v=0
                    if(self.__lives==0):
                        os.system('clear')
                        print('YOU LOSE:',end='\t \t')
                        print('SCORE:',self.__coins)
                        quit() 
            
            if self.coins(self.__screen[xx-1][yy])==1:
                self.__coins=self.__coins+1
            if self.coins(self.__screen[xx-1][yy+1])==1 :
                self.__coins=self.__coins+1
            if self.coins(self.__screen[xx-1][yy+2])==1 :

                self.__coins=self.__coins+1
            if (self.sb(self.__screen[xx-1][yy])==1 or self.sb(self.__screen[xx-1][yy+1])==1 or self.sb(self.__screen[xx-1][yy+2])==1 ):
                self.__sb=1
                obj.destroyobstacle(self.__screen,obs1[xx-1][yy],obs2[xx-1][yy])
                obj.destroyobstacle(self.__screen,obs1[xx-1][yy+1],obs2[xx-1][yy+1])
                obj.destroyobstacle(self.__screen,obs1[xx-1][yy+2],obs2[xx-1][yy+2])
            ch='#'
            if self.__shield ==1:
                ch='@'
            if self.__screen[xx-1][yy]!='M' and self.__screen[xx-1][yy+1]!='M' and self.__screen[xx-1][yy+2]!='M':

                self.__screen[xx-1][yy]=ch
                self.__screen[xx-1][yy+1]=ch
                self.__screen[xx-1][yy+2]=ch
                self.__screen[xx+2][yy]=' '
                self.__screen[xx+2][yy+1]=' '
                self.__screen[xx+2][yy+2]=' '
            else:
                self.__xpos=xx
                self.__ypos=yy
        
        
        
        
        
        
        
        if t==4 and xx+2 <rr-3: 
            xx=self.__xpos
            yy=self.__ypos

            self.__xpos=xx+1
            self.__ypos=yy
            if(self.__shield ==0):

                if (self.collision(self.__screen[xx+3][yy])==1 or self.collision(self.__screen[xx+3][yy+1])==1 or self.collision(self.__screen[xx+3][yy+2])==1 ):
                #print(self.__coins)
                    obj.destroyobstacle(self.__screen,obs1[xx+3][yy],obs2[xx+3][yy])
                    obj.destroyobstacle(self.__screen,obs1[xx+3][yy+1],obs2[xx+3][yy+1])
                    obj.destroyobstacle(self.__screen,obs1[xx+3][yy+2],obs2[xx+3][yy+2])
                    self.__lives=self.__lives-1
                    os.system('clear')
                    #sleep(2)
                   # v=0
                    time.sleep(1)
                    if(self.__lives==0):
                        os.system('clear')
                        print('YOU LOSE:',end='\t \t')
                        print('SCORE:',self.__coins)
                        quit()
            if self.coins(self.__screen[xx+3][yy])==1:
                self.__coins=self.__coins+1
            if self.coins(self.__screen[xx+3][yy+1])==1 :
                self.__coins=self.__coins+1
            if self.coins(self.__screen[xx+3][yy+2])==1 :

                self.__coins=self.__coins+1            

            if (self.sb(self.__screen[xx+3][yy])==1 or self.sb(self.__screen[xx+3][yy+1])==1 or self.sb(self.__screen[xx+3][yy+2])==1 ):
                self.__sb=1 
                obj.destroyobstacle(self.__screen,obs1[xx+3][yy],obs2[xx+3][yy])
                obj.destroyobstacle(self.__screen,obs1[xx+3][yy+1],obs2[xx+3][yy+1])
                obj.destroyobstacle(self.__screen,obs1[xx+3][yy+2],obs2[xx+3][yy+2])
            ch='#'
            if self.__shield ==1:
                ch='@'
            if self.__screen[xx+3][yy]!='M' and self.__screen[xx+3][yy+1]!='M' and self.__screen[xx+3][yy+2]!='M':
                self.__screen[xx][yy]=' '
                self.__screen[xx][yy+1]=' '
                self.__screen[xx][yy+2]=' '
                self.__screen[xx+3][yy]=ch
                self.__screen[xx+3][yy+1]=ch
                self.__screen[xx+3][yy+2]=ch
            else:
                self.__xpos=xx
                self.__ypos=yy


    def checkleft(self,v,screen1):
        xx=self.__xpos
        yy=self.__ypos
        if yy<=v+1:
            self.__ypos=self.__ypos+1
            ch='#'
            if self.__shield ==1:
                ch='@'
            self.__screen[xx][yy]=' '
            self.__screen[xx+1][yy]=' '
            self.__screen[xx+2][yy]=' '
            self.__screen[xx][yy+3]=ch
            self.__screen[xx+1][yy+3]=ch
            self.__screen[xx+2][yy+3]=ch

    def updatescreen(self,screen1):
        xx=self.__xpos
        yy=self.__ypos
        self.__screen[xx][yy]='#'
        self.__screen[xx][yy+1]='#'
        self.__screen[xx][yy+2]='#'
        self.__screen[xx+1][yy]='#'
        self.__screen[xx+1][yy+1]='#'
        self.__screen[xx+1][yy+2]='#'
        self.__screen[xx+2][yy]='#'
        self.__screen[xx+2][yy+1]='#'
        self.__screen[xx+2][yy+2]='#'

    def createbullet(self):
        xx=self.__xpos
        yy=self.__ypos
        self.__lst1.append(xx)
        self.__lst2.append(yy+2)

    def movebullets(self,screen1,v,obj,obs1,obs2,drobj):
        n=len(self.__lst2)
        for i in range(n):
            self.__lst2[i]=self.__lst2[i]+2
            y=self.__lst2[i]
            if y<= v+200:
                xc=self.__lst1[i]
                if ( self.__screen[self.__lst1[i]][y-2]=='+'):
                    self.__screen[self.__lst1[i]][y-2]=' '
                
                xx1=' '
                xx2=' '
                xx3=' '
                xx4=' '
                xx5=' '
                xx6=' '
                if v<798:
                    if(self.__screen[self.__lst1[i]][y]=='*'):
                        xx1='*'
                    if(self.__screen[self.__lst1[i]][y-1]=='*'):
                        xx2='*'

                    if(self.__screen[self.__lst1[i]][y]=='M'):
                        xx3='M'
                    if(self.__screen[self.__lst1[i]][y-1]=='M'):
                        xx4='M'

                    if(self.__screen[self.__lst1[i]][y]=='%'):
                        xx5='%'
                    if(self.__screen[self.__lst1[i]][y-1]=='%'):
                        xx6='%'

                if(v>798):
                    

                    if(self.__screen[self.__lst1[i]][y]!=' ' and self.__screen[self.__lst1[i]][y]!=':'):
                        drobj.kill()
                        self.__lst2[i]=1500
                        
                    elif(self.__screen[self.__lst1[i]][y-1]!=' ' and  self.__screen[self.__lst1[i]][y-1]!=':'):
                        drobj.kill()
                        self.__lst2[i]=1500

                if v<798:
                    if(self.__screen[self.__lst1[i]][y]=='|' or self.__screen[self.__lst1[i]][y]=='_' or self.__screen[self.__lst1[i]][y]=='/'):
                        obj.destroyobstacle(self.__screen,obs1[xc][y],obs2[xc][y])
                        y=1500
                        self.__lst2[i]=1500
                
                    if(self.__screen[self.__lst1[i]][y-1]=='|' or self.__screen[self.__lst1[i]][y-1]=='_' or self.__screen[self.__lst1[i]][y-1]=='/'):
                        obj.destroyobstacle(self.__screen,obs1[xc][y-1],obs2[xc][y-1])
                        y=1500
                        self.__lst2[i]=1500
                        

                self.__screen[self.__lst1[i]][y]='+'
                if v<798:
                    if xx1=='*':
                        self.__screen[self.__lst1[i]][y]='*'
                    if xx2=='*':
                        self.__screen[self.__lst1[i]][y-1]='*'
                    if xx3=='M':
                        self.__screen[self.__lst1[i]][y]='M'
                    if xx4=='M':
                        self.__screen[self.__lst1[i]][y-1]='M'
                    if xx5=='%':
                        self.__screen[self.__lst1[i]][y]='%'
                    if xx6=='%':
                        self.__screen[self.__lst1[i]][y-1]='%'
            else:
                
                
                if y<1000:
                    self.__screen[self.__lst1[i]][y]=' '
                    self.__screen[self.__lst1[i]][y-2]=' '
                self.__lst2[i]=1500

            
        

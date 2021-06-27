import os
from os import system,name
class dragon:

    def __init__(self,x,y,screen):
        self.__x=x
        self.__y=y
        self.__lives=5
        self.__lst1=[]
        self.__lst2=[]
        self.__screen=screen
    def printdragon(self,screen):
        fd=open('dragon.txt')
        xx=self.__x
        yy=self.__y
        for i in fd:
            #print(i)
            i=i.rstrip()
            for ch in i:
                self.__screen[xx][yy]=ch
                #print(xx,yy)
                yy=yy+1
            yy=self.__y
            #print()
            xx=xx+1
                

    def movedragon(self,x,screen):
        xx=self.__x
        yy=self.__y
        fd=open('dragon.txt')
        for i in fd:
            #print(i)
            i=i.rstrip()
            for ch in i:
                self.__screen[xx][yy]=' '
                #print(xx,yy)
                yy=yy+1
            yy=self.__y
            #print()
            xx=xx+1
        xx=self.__x
        yy=self.__y
        if self.__x > x and self.__x >3 :
            self.__x=self.__x-2
            for j in range(40):
                self.__screen[xx+12][yy+j]=' '
            for j in range(40):
                self.__screen[xx+13][yy+j]=' '

        if self.__x < x and self.__x <33:
            self.__x=self.__x+2
            for j in range(40):
                self.__screen[xx][yy+j]=' '
            for j in range(40):
                self.__screen[xx+1][yy+j]=' '

    def get_lives(self):
        return self.__lives
    def createbullet(self,player_obj):
        xx=self.__x
        yy=self.__y
        self.__lst1.append(player_obj.get_xpos())
        self.__lst2.append(yy-2)
        self.__lst1.append(xx+10)
        
        self.__lst2.append(yy-2)
        
    def movebullets(self,screen,player_obj):
        n=len(self.__lst2)
        for i in range(n):
            self.__lst2[i]=self.__lst2[i]-2
            y=self.__lst2[i]
            if y>794 and y<1000:
                if ( self.__screen[self.__lst1[i]][y+2]==':'):
                    self.__screen[self.__lst1[i]][y+2]=' '
                if(self.__screen[self.__lst1[i]][y]=='#'):
                    player_obj.kill()
                    self.__lst2[i]=0
                elif(self.__screen[self.__lst1[i]][y-1]=='#'):
                    player_obj.kill()
                    self.__lst2[i]=0
                self.__screen[self.__lst1[i]][self.__lst2[i]]=':'    
    def kill(self):
        self.__lives=self.__lives-1
        if self.__lives==0:
            os.system('clear')
            print('YOU WIN')
            quit()


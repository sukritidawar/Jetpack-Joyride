from random import randint
from board import board



class obstacles:
    def __init__(self,x,y,screen1,obs1,obs2):
        self._xx=x
        self._yy=y
        self._screen=screen1
        self._obs1=obs1
        self._obs2=obs2
    def createobstacle(self,screen1,obs11,obs22):
        xc=self._xx
        yc=self._yy
        self._screen[xc][yc]='|'
        self._screen[xc+1][yc]='|'
        self._screen[xc+2][yc]='|'
        self._screen[xc+3][yc]='|'

        self._obs1[xc][yc]=xc
        self._obs1[xc+1][yc]=xc
        self._obs1[xc+2][yc]=xc
        self._obs1[xc+3][yc]=xc

        self._obs2[xc][yc]=yc
        self._obs2[xc+1][yc]=yc
        self._obs2[xc+2][yc]=yc
        self._obs2[xc+3][yc]=yc

    def destroyobstacle(self,screen1,xc,yc):

        if self._screen[xc][yc]=='|':
            self._screen[xc][yc]=' '
            self._screen[xc+1][yc]=' '
            self._screen[xc+2][yc]=' '
            self._screen[xc+3][yc]=' '

        if self._screen[xc][yc]=='/':

            self._screen[xc][yc]=' '
            self._screen[xc+1][yc-1]=' '
            self._screen[xc+2][yc-2]=' '
            self._screen[xc+3][yc-3]=' '

        if self._screen[xc][yc]=='_':
            self._screen[xc][yc]=' '
            self._screen[xc][yc+1]=' '
            self._screen[xc][yc+2]=' '
            self._screen[xc][yc+3]=' '
        if self._screen[xc][yc]=='%':
            self._screen[xc][yc]=' '
            self._screen[xc+1][yc+1]=' '
            self._screen[xc][yc+1]=' '
            self._screen[xc+1][yc]=' '


class obstacle1(obstacles):
    def createobstacle(self,screen1,obs11,obs22):
        xc=self._xx
        yc=self._yy
        self._screen[xc][yc]='|'
        self._screen[xc+1][yc]='|'
        self._screen[xc+2][yc]='|'
        self._screen[xc+3][yc]='|'
        
        self._obs1[xc][yc]=xc
        self._obs1[xc+1][yc]=xc
        self._obs1[xc+2][yc]=xc
        self._obs1[xc+3][yc]=xc

        self._obs2[xc][yc]=yc
        self._obs2[xc+1][yc]=yc
        self._obs2[xc+2][yc]=yc
        self._obs2[xc+3][yc]=yc

    def destroyobstacle(self,screen1,xc,yc):

        if self._screen[xc][yc]=='|':
            self._screen[xc][yc]=' '
            self._screen[xc+1][yc]=' '
            self._screen[xc+2][yc]=' '
            self._screen[xc+3][yc]=' '

class obstacle2(obstacles):

    def createobstacle(self,screen1,obs11,obs22):
        xc=self._xx
        yc=self._yy

        self._screen[xc][yc]='_'
        self._screen[xc][yc+1]='_'
        self._screen[xc][yc+2]='_'
        self._screen[xc][yc+3]='_'

        self._obs1[xc][yc]=xc
        self._obs1[xc][yc+1]=xc
        self._obs1[xc][yc+2]=xc
        self._obs1[xc][yc+3]=xc

        self._obs2[xc][yc]=yc
        self._obs2[xc][yc+1]=yc
        self._obs2[xc][yc+2]=yc
        self._obs2[xc][yc+3]=yc
    
    def destroyobstacle(self,screen1,xc,yc):
    
        if self._screen[xc][yc]=='_':
            self._screen[xc][yc]=' '
            self._screen[xc][yc+1]=' '
            self._screen[xc][yc+2]=' '
            self._screen[xc][yc+3]=' '
class obstacle3(obstacles):

    def createobstacle(self,screen1,obs11,obs22):
        xc=self._xx
        yc=self._yy

        self._screen[xc][yc]='/'
        self._screen[xc+1][yc-1]='/'
        self._screen[xc+2][yc-2]='/'
        self._screen[xc+3][yc-3]='/'

        self._obs1[xc][yc]=xc
        self._obs1[xc+1][yc-1]=xc
        self._obs1[xc+2][yc-2]=xc
        self._obs1[xc+3][yc-3]=xc

        self._obs2[xc][yc]=yc
        self._obs2[xc+1][yc-1]=yc
        self._obs2[xc+2][yc-2]=yc
        self._obs2[xc+3][yc-3]=yc

    def destroyobstacle(self,screen1,xc,yc):
         if self._screen[xc][yc]=='/':

            self._screen[xc][yc]=' '
            self._screen[xc+1][yc-1]=' '
            self._screen[xc+2][yc-2]=' '
            self._screen[xc+3][yc-3]=' '

    '''
    def destroyobstacle(self,screen1,xc,yc):

        if screen1[xc][yc]=='|':
            screen[xc][yc]=' '
            screen[xc+1][yc]=' '
            screen[xc+2][yc]=' '
            screen[xc+3][yc]=' '

        if screen[xc][yc]=='/':

            screen[xc][yc]=' '
            screen[xc+1][yc-1]=' '
            screen[xc+2][yc-2]=' '
            screen[xc+3][yc-3]=' '

        if screen[xc][yc]=='_':
            screen[xc][yc]=' '
            screen[xc][yc+1]=' '
            screen[xc][yc+2]=' '
            screen[xc][yc+3]=' '
        if screen[xc][yc]=='%':
            screen[xc][yc]=' '
            screen[xc+1][`yc+1]=' '
            screen[xc][yc+1]=' '
            screen[xc+1][yc]=' '
    '''
class magnet(obstacles):
    def createobstacle(self,screen1,sc1,obs11,obs22):
        xc=self._xx
        yc=self._yy
        self._screen[xc][yc]='M'
        self._screen[xc+1][yc+1]='M'
        self._screen[xc][yc+1]='M'
        self._screen[xc+1][yc]='M' 
        sc1[xc][yc]='M'
        sc1[xc+1][yc]='M'
        sc1[xc][yc+1]='M'
        sc1[xc+1][yc+1]='M'
        k=0
        for i in range(xc-9,xc):
            for j in range(yc-9+k,yc+1+10-k):
                sc1[i][j]='D'
            k=k+1
        k=0
        i=xc+7
        while i>xc+1:

            for j in range(yc-9+k,yc+1+10-k):
                sc1[i][j]='U'
            k=k+1
            i=i-1

        k=0
        for i in range(yc-36,yc):
            for j in range(xc-10,xc+1+10):
                sc1[j][i]='R'
            k=k+1
        k=0
        i=yc+33
        while  i>yc+1:

            for j in range(xc-10,xc+1+10):
                sc1[j][i]='L'
            k=k+1
            i=i-1
        for i in range(yc-36,yc):
            for j in range(xc-1,xc+3):
                sc1[j][i]='P'
            k=k+1
        for i in range(yc+1,yc+36):
            
            for j in range(xc-1,xc+3):
                sc1[j][i]='K'
            k=k+1
class coins(obstacles):
    def createcoins1(self,screen1,obs11,obs22):
        xc=self._xx
        yc=self._yy

        self._screen[xc][yc]='*'
        self._screen[xc+1][yc]='*'
        self._screen[xc][yc+1]='*'
        self._screen[xc+1][yc+1]='*'
    def createcoins2(self,screen1,obs11,obs22):
        xc=self._xx
        yc=self._yy

        self._screen[xc][yc]='*'
        self._screen[xc+1][yc-1]='*'
        self._screen[xc][yc+1]='*'
        self._screen[xc+1][yc+1]='*'


    def createcoins3(self,screen1,obs11,obs22):
        xc=self._xx
        yc=self._yy

        self._screen[xc][yc]='*'
        self._screen[xc][yc+1]='*'
        self._screen[xc][yc+2]='*'
        self._screen[xc+1][yc]='*'
        self._screen[xc+1][yc+1]='*'
        self._screen[xc+1][yc+2]='*'


    def createcoins4(self,screen1,obs11,obs22):
        xc=self._xx
        yc=self._yy

        self._screen[xc][yc]='*'
        self._screen[xc+1][yc]='*'
class speedbooster(obstacles):
    def createobstacle(self,screen1,obs11,obs22):
        xc=self._xx
        yc=self._yy

        self._screen[xc][yc]='%'
        self._screen[xc+1][yc]='%'
        self._screen[xc][yc+1]='%'
        self._screen[xc+1][yc+1]='%'

        self._obs1[xc][yc]=xc
        self._obs1[xc+1][yc]=xc
        self._obs1[xc][yc+1]=xc
        self._obs1[xc+1][yc+1]=xc

        self._obs2[xc][yc]=yc
        self._obs2[xc+1][yc]=yc
        self._obs2[xc][yc+1]=yc
        self._obs2[xc+1][yc+1]=yc 


    def destroyobstacle(self,screen1,xc,yc):
        if self._screen[xc][yc]=='%':
            self._screen[xc][yc]=' '
            self._screen[xc+1][yc+1]=' '
            self._screen[xc][yc+1]=' '
            self._screen[xc+1][yc]=' '        

import os
from colorama import Fore, Back, Style
class board:
    def __init__(self,r,c):
        self.__rows=r
        self.__col=c
        self.__screen=[]
        self.__obs1=[]
        self.__obs2=[]
        self.sc1=[]
    

    def createboard(self):
        self.__screen=[[' ' for x in range(self.__col)] for y in range(self.__rows)]
    
    def createobs(self):
        self.__obs1=[[0 for x in range(self.__col)] for y in range(self.__rows)]
        self.__obs2=[[0 for x in range(self.__col)] for y in range(self.__rows)]
        self.sc1=[[' ' for x in range(self.__col)] for y in range(self.__rows)]

    def get_screen(self):
        return self.__screen
    def get_obs1(self):
        return self.__obs1
    def get_obs2(self):
        return self.__obs2
    def printscreen(self,v):
        
        '''self.screen[0][v+1]='S'
        self.screen[0][v+2]='C'
        self.screen[0][v+3]='O'
        self.screen[0][v+4]='R'
        self.screen[0][v+5]='E'
        '''
        
        #print('\033[0;0H')
        
        if(v<=798):
            for i in range(self.__rows):
                for j in range(v,v+201):
                    print(Back.BLACK,end='')
                    print(Style.BRIGHT,end='')
                    ch=self.__screen[i][j]
                    if ch=='#' or ch=='+':
                        print(Fore.RED,end='')
                        print(Style.BRIGHT,end='')
                        print(self.__screen[i][j],end='')
                    elif ch=='|' or ch=='/' or ch=='_':
                        print(Fore.YELLOW,end='')
                        print(Style.BRIGHT,end='')
                        print(self.__screen[i][j],end='')
                    elif ch=='M':
                        print(Fore.GREEN,end='')
                        print(Style.BRIGHT,end='')
                        print(self.__screen[i][j],end='')
                    elif ch=='%':
                        print(Fore.BLUE,end='')
                        print(Style.BRIGHT,end='')
                        print(self.__screen[i][j],end='')
                    elif ch=='S' or ch=='F':
                        print(Fore.BLUE,end='')
                        print(Style.BRIGHT,end='')
                        print(self.__screen[i][j],end='')

                    else:
                        print(Fore.WHITE,end='')
                        print(Style.BRIGHT,end='')
                        print(self.__screen[i][j],end='')
                print()
        elif(v>798):
            for i in range(self.__rows):
                for j in range(798,998):
                    print(Back.BLACK,end='')
                    print(Style.BRIGHT,end='')
                    ch=self.__screen[i][j]
                    if ch=='#' or ch=='+':
                        print(Fore.RED,end='')
                        print(Style.BRIGHT,end='')
                        print(self.__screen[i][j],end='')
                    elif ch=='|' or ch=='/' or ch=='_':
                        print(Fore.YELLOW,end='')
                        print(Style.BRIGHT,end='')
                        print(self.__screen[i][j],end='')
                    elif ch=='M':
                        print(Fore.GREEN,end='')
                        print(Style.BRIGHT,end='')
                        print(self.__screen[i][j],end='')
                    elif ch=='%':
                        print(Fore.BLUE,end='')
                        print(Style.BRIGHT,end='')
                        print(self.__screen[i][j],end='')
                    elif ch=='S' or ch=='F':
                        print(Fore.BLUE,end='')
                        print(Style.BRIGHT,end='')
                        print(self.__screen[i][j],end='')
                    else:
                        print(Fore.WHITE,end='')
                        print(Style.BRIGHT,end='')
                        print(self.__screen[i][j],end='')

                print()
        

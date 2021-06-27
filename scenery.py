import random
import os

rr=50
class skyfloor:
    def __init__(self,screen):
        self.__sky='S'
        self.__floor='F'
        self.__screen=screen
    def createsky(self,screen1):
        for i in range(1000):
            self.__screen[1][i]=self.__sky
        #for i in range(1,52):
        #    screen[i][798]='E'
    def createfloor(self,screen1):
        for i in range(1000):
            self.__screen[rr-1][i]=self.__floor


#make a stop watch using pygame
import pygame as pg
import time
import sys

#initialize pygame

pg.init()

pg.display.set_caption("Stop Watch")
size=(500,500)
screen=pg.display.set_mode(size)
clock=pg.time.Clock()
color=(0,255,0)

count=0.0
while True:
    clock.tick(30)
    screen.fill(color)
    pg.display.update()
    if count>1000:
        
        break
    
pg.quit()




    
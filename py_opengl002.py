import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def draw():
    glColor3f(0, 0, 1)  # Set color to white
    glBegin(GL_POLYGON)
    glVertex2f(-3,2 ) 
    glVertex2f(-1,4 ) 
    glVertex2f(0,2 ) 
    glVertex2f(-2,0 ) 
    glColor3f(1, 0, 1)
    glVertex2f(-1,0 ) 
    glVertex2f(1,2 ) 
    glVertex2f(2,1 ) 
    glVertex2f(0,-2 )
    glColor3f(0,.91, 0.21)
    glVertex2f(1,-2 )
    glVertex2f(3,0 ) 
    glVertex2f(4,-2)
    glVertex2f(2,-4 )
    glEnd()
    

def main():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL|RESIZABLE)
    
    gluPerspective(80, (display[0] / display[1]), 1, 50)
    glTranslatef(0.0, 0.0, -5)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw()
        pygame.display.flip()
        
main()
         
                
    
            
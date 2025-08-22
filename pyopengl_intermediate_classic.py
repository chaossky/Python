from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    # 배경색 (검정)
    glClearColor(0.0, 0.0, 0.0, 1.0)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # 삼각형 그리기
    glBegin(GL_TRIANGLES)

    glColor3f(1.0, 0.0, 0.0)   # 빨강
    glVertex3f(-0.5, -0.5, 0.0)

    glColor3f(0.0, 1.0, 0.0)   # 초록
    glVertex3f(0.5, -0.5, 0.0)

    glColor3f(0.0, 0.0, 1.0)   # 파랑
    glVertex3f(0.0, 0.5, 0.0)

    glEnd()

    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"PyOpenGL Immediate Mode Triangle")

    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()

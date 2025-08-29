try:
    from OpenGL.GLUT import *
    from OpenGL.GLU import *
    from OpenGL.GL import *
except Exception as msg:
    print("PyOpenGL이 올바르게 설치되지 않았습니다. 오류코드：", msg)
    
WIDTH = 400
HEIGHT = 200
STATE = 1

def drawColorCube():
    glBegin(GL_QUADS)  
    glColor3f(1.0, 0.0, 0.0) 
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)

    glColor3ub(255, 150, 0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)

    glColor3f(0.0, 0.0, 1.0)  
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    glColor3f(0.0, 1.0, 0.0)  
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)

    glColor3f(1.0, 1.0, 0.0) 
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)

    glColor3f(1.0, 1.0, 1.0)  
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glEnd()


def mouseclick(button, state, x, y):
    global STATE
    if state == 0 and button == 0:
        if STATE < 8:
            STATE += 1
        else:
            STATE = 1


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0) 
    # glShadeModel(GL_FLAT)  
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)  
    glLoadIdentity()  
    glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)
    glMatrixMode(GL_MODELVIEW)


def update():
    global STATE
    # print("update", STATE)
    if STATE == 1:  
        glLoadIdentity()  
        gluLookAt(3.0, 3.0, 3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)  # 设置视点与视角
    elif STATE == 2:
        glLoadIdentity()
        gluLookAt(3.0, 3.0, -3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    elif STATE == 3:
        glLoadIdentity()
        gluLookAt(-3.0, 3.0, -3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    elif STATE == 4:
        glLoadIdentity()
        gluLookAt(-3.0, 3.0, 3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    elif STATE == 5:
        glLoadIdentity()
        gluLookAt(3.0, -3.0, 3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    elif STATE == 6:
        glLoadIdentity()
        gluLookAt(3.0, -3.0, -3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    elif STATE == 7:
        glLoadIdentity()
        gluLookAt(-3.0, -3.0, -3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    elif STATE == 8:
        glLoadIdentity()
        gluLookAt(-3.0, -3.0, 3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  
    drawColorCube()
    glutSwapBuffers()  

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(WIDTH, HEIGHT)
glutCreateWindow(b'cube')
init()
glutDisplayFunc(update)
glutMouseFunc(mouseclick)  #
glutMainLoop()
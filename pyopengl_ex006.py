from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

# 회전 각도
angle_x = 0
angle_y = 0

# 마우스 상태
mouse_down = False
mouse_x = 0
mouse_y = 0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    # 조명 설정
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [1.0, 0.5,0,5, 0.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.4, 0.6, 1.0, 1.0])

    # 재질 설정
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [0.8, 0.5, 0.6, 1.0])
    glShadeModel(GL_SMOOTH)

def draw_sphere(radius, slices, stacks):
    for i in range(stacks):
        lat0 = math.pi * (-0.5 + float(i) / stacks)
        z0 = radius * math.sin(lat0)
        zr0 = radius * math.cos(lat0)

        lat1 = math.pi * (-0.5 + float(i + 1) / stacks)
        z1 = radius * math.sin(lat1)
        zr1 = radius * math.cos(lat1)

        glBegin(GL_QUAD_STRIP)
        for j in range(slices + 1):
            lng = 2 * math.pi * float(j) / slices
            x = math.cos(lng)
            y = math.sin(lng)

            glNormal3f(x, y, z0 / radius)  # 법선 벡터 설정 (조명 계산에 필요)
            glVertex3f(x * zr0, y * zr0, z0)
            glNormal3f(x, y, z1 / radius)
            glVertex3f(x * zr1, y * zr1, z1)
        glEnd()

def display():
    global angle_x, angle_y
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)

    glRotatef(angle_x, 1.0, 0.0, 0.0)
    glRotatef(angle_y, 0.0, 1.0, 0.0)

    draw_sphere(1.0, 50, 50)

    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, width / float(height), 1, 100)
    glMatrixMode(GL_MODELVIEW)

# 마우스 클릭 이벤트
def mouse(button, state, x, y):
    global mouse_down, mouse_x, mouse_y
    if button == GLUT_LEFT_BUTTON:
        mouse_down = (state == GLUT_DOWN)
        mouse_x = x
        mouse_y = y

# 마우스 드래그 이벤트
def motion(x, y):
    global angle_x, angle_y, mouse_x, mouse_y
    if mouse_down:
        dx = x - mouse_x
        dy = y - mouse_y
        angle_x += dy * 0.5
        angle_y += dx * 0.5
        mouse_x = x
        mouse_y = y
        glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Interactive Lit Sphere")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    glutMainLoop()

if __name__ == "__main__":
    main()

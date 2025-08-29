#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

try:
    from OpenGL.GLUT import *
    from OpenGL.GLU import *
    from OpenGL.GL import *
except Exception as msg:
    print("PyOpenGL이 올바르게 설치되지 않았습니다. 오류코드：", msg)

WIDTH = 400
HEIGHT = 200


def init():
    """초기화"""
    glClearColor(0.0, 0.0, 0.0, 0.0)  # "색상 지우기" 를 검은색으로 설정합니다

    glLoadIdentity()  # 관찰 행렬 초기화
    # 시점 설정
    gluLookAt(0.0, 0.0, 7.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    # 투영 모드로 설정
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # 관찰 행렬 초기화
    
    # OPENGL에서 원근 투영을 설정하는 함수
    # 3D 공간을 카메라 시점에서 바라보는 시야의 범위를 정의
    # glFrustum(left, right, bottom, top, near, far)
    # 
    # left	가까운 평면의 왼쪽 경계	-1.0	카메라에서 보이는 왼쪽 끝
    # right	가까운 평면의 오른쪽 경계	1.0	카메라에서 보이는 오른쪽 끝
    # bottom	가까운 평면의 아래쪽 경계	-1.0	화면 아래쪽
    # top	가까운 평면의 위쪽 경계	1.0	화면 위쪽
    # near	가까운 평면까지의 거리	1.5	카메라에서 1.5 단위 거리부터 보임
    # far	먼 평면까지의 거리	20.0	20 단위 거리까지 보임
    # glFrustum()은 카메라 시야를 절두체(Frustum) 형태로 정의합니다. 절두체는 앞이 좁고 뒤가 넓은 잘린 피라미드 모양으로, 원근감을 표현하는 데 사용돼요.
    # 가까운 물체는 크게 보이고
    # 멀리 있는 물체는 작게 보이는
    # 현실적인 원근 효과를 만들어줍니다
    
    glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)  #
    glMatrixMode(GL_MODELVIEW)


def update():
    glClear(GL_COLOR_BUFFER_BIT)  # 화면을 지정된 색-검정으로 초기화
    glutWireCube(3.0)  # 큐브의 경계선을 그립니다.
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(WIDTH, HEIGHT)
glutCreateWindow(b'cube')
init()
glutDisplayFunc(update)
glutMainLoop()
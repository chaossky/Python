#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from __future__ import division # 정확한 나눗셈
try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
except Exception as msg:
    print("PyOpenGL이 올바르게 설치되지 않았습니다. 오류 코드:", msg)

PX = PY = 100
WIDTH = 400
HEIGHT = 200

def drawpoint():
    """점 그리기, PX, PY 위치에 어떻게 그릴 것인가? 2s, 2i, 2d 모두 정상적이지 않음"""
    print("drawpoint")
    glColor3ub(255, 0, 0)
    glPointSize(25)
    glEnable(GL_POINT_SMOOTH)
    glBegin(GL_POINTS)
    glVertex2f(PX / WIDTH, PY / HEIGHT) # 점의 좌표
    glEnd()

def update():
    print("update")
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    drawpoint()
    glFlush()
    print("update down")

def reshape(width, height):
    """윈도우 크기가 변경될 때 콜백
    매개변수:
    width: 크기 변경 후 윈도우 너비
    height: 크기 변경 후 윈도우 높이
    """
    print("reshape", width, height)

def mouseclick(button, state, x, y):
    """마우스 클릭 시 콜백 발생
    매개변수:
    button: 0~2, 왼쪽, 중간, 오른쪽 버튼
    state: 0 누름, 1 놓음
    x, y: 윈도우 내에서 마우스의 위치 좌표
    """
    print("mouseclick", button, state, x, y)
    global PX, PY
    PX = x
    PY = y

def mousemotion(x, y):
    """마우스를 누르고 드래그할 때 콜백
    매개변수:
    x, y: 윈도우 내에서 마우스의 위치 좌표
    """
    print("mousemotion", x, y)

def keydown(key, x, y):
    """윈도우가 활성화되었을 때의 키보드 응답 이벤트
    매개변수:
    key: 키보드 해당 키
    x, y: 윈도우 내에서 마우스의 위치 좌표
    """
    print("keydown", key, x, y)

def mouseenter(enter):
    """마우스가 윈도우에 진입하거나 떠날 때 콜백
    매개변수:
    enter: 0 윈도우 떠남, 1 윈도우 진입
    """
    print("mouseenter", enter)

def mousemove(x, y):
    """마우스 이동 응답 이벤트
    매개변수:
    x, y: 윈도우 내에서 마우스의 위치 좌표
    """
    print("mousemove", x, y)

glutInit()
glutInitDisplayMode(GLUT_RGB)
glutInitWindowSize(WIDTH, HEIGHT) # 윈도우 크기 설정
window = glutCreateWindow(b'PyOpenGL Event')
glutDisplayFunc(update) # 콜백 함수 등록
glutReshapeFunc(reshape) # 윈도우 변경에 응답하는 함수 reshape() 등록
glutMouseFunc(mouseclick) # 마우스 클릭에 응답하는 함수 mouseclick() 등록
glutMotionFunc(mousemotion) # 마우스 드래그에 응답하는 함수 mousemotion() 등록
glutKeyboardFunc(keydown) # 키보드 입력 함수 keydown() 등록
glutEntryFunc(mouseenter) # 등록
glutPassiveMotionFunc(mousemove) # 등록
glutMainLoop()
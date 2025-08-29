#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
except Exception as msg:
    print("PyOpenGL이 올바르게 설치되지 않았습니다. 오류 코드:", msg)

STATE = 0

def mouseclick(button, state, x, y):
    """마우스 클릭 시 콜백 발생: 마우스 왼쪽 버튼 클릭 시 STATE가 1~3 사이에서 순환
    매개변수:
    button: 0~2, 왼쪽, 중간, 오른쪽 버튼
    state: 0 누름, 1 놓음
    x, y: 윈도우 내에서 마우스의 위치 좌표
    """
    global STATE
    if state == 0 and button == 0:
        if STATE < 3:
            STATE += 1
        else:
            STATE = 1

def drawpoint():
    """점 그리기"""
    glColor3ub(255, 0, 0) # 브러시 색상을 빨간색으로 설정
    glPointSize(25) # 기본 픽셀 점의 크기 설정
    glEnable(GL_POINT_SMOOTH) # 점 부드럽게 하기 활성화
    glBegin(GL_POINTS) # 스케치 점 그리기 모드 시작
    glVertex2f(0.0, 0.0) # 점의 좌표
    glEnd()

def drawline():
    """선분 그리기"""
    glColor4f(0.0, 1.0, 0.0, 1.0) # 브러시 색상을 녹색으로, 불투명도를 1로 설정
    glLineWidth(5) # 선의 너비 설정
    glBegin(GL_LINES) # 스케치 선 그리기 모드 활성화
    glVertex2f(-1.0, -1.0) # 시작점 좌표
    glVertex2f(0.5, 0.5) # 끝점 좌표
    glVertex2f(-1.0, -1.0) # 시작점 좌표
    glVertex2f(1.0, -1.0) # 끝점 좌표
    glEnd() # 선 그리기 모드 닫기

def drawtriangle():
    """삼각형 그리기"""
    glBegin(GL_TRIANGLES)
    glColor3f(0, 0, 1) # 브러시 색상을 파란색으로 설정
    glVertex2f(-1.0, 0.0)
    glVertex2f(-0.5, 0.0)
    glVertex2f(1.0, 1.0)
    glEnd()

def drawquad():
    """사각형 그리기"""
    # 채워진 직사각형 그리기
    glBegin(GL_QUADS) # 기본값은 채우기 모드
    glColor3f(0, 1, 1) # 브러시 색상을 청록색으로 설정
    glVertex2f(0.5, 0.0)
    glVertex2f(0.5, -0.8)
    glVertex2f(1.0, -0.8)
    glVertex2f(1.0, 0.0)
    glEnd()

def update():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    global STATE
    print(STATE)
    """STATE 값에 따라 다른 뷰 볼륨 설정, STATE 기본값은 0"""
    if STATE == 1: # 아래 두 줄의 주석을 해제하면 무엇을 발견하나요???
        glLoadIdentity() # 관찰 행렬 재설정
        glOrtho(0.0, 1.0, -1.0, 0.0, -1.0, 1.0)
    elif STATE == 2:
        glLoadIdentity() # 관찰 행렬 재설정
        glOrtho(0.0, 0.6, -0.6, 0.0, -1.0, 1.0)
    elif STATE == 3:
        glLoadIdentity() # 관찰 행렬 재설정
    
    drawpoint()
    drawline()
    drawtriangle()
    drawquad()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutCreateWindow(b'PyOpenGL glOrtho')
glutMouseFunc(mouseclick) # 마우스 클릭에 응답하는 함수 mouseclick() 등록
glutDisplayFunc(update) # 콜백 함수 등록
glutMainLoop()
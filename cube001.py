# 이 부분은 OpenGL의 세 가지 주요 모듈을 임포트합니다:
# OpenGL.GLUT: 윈도우 생성, 이벤트 처리, 키보드/마우스 입력 등을 담당하는 유틸리티 툴킷
# OpenGL.GLU: 고급 유틸리티 함수 (예: 카메라 시점 설정 등)
# OpenGL.GL: 기본적인 OpenGL 함수들 (예: 도형 그리기, 색상 설정 등)
# *를 사용해서 해당 모듈의 모든 함수와 상수를 불러옵니다.
try:
    from OpenGL.GLUT import *
    from OpenGL.GLU import *
    from OpenGL.GL import *
except Exception as msg:
    print("PyOpenGL이 올바르게 설치되지 않았습니다. 오류코드：", msg)
# 만약 위의 import 중 하나라도 실패하면, Exception을 잡아서 오류 메시지를 출력합니다.

WIDTH = 840
HEIGHT = 640

def drawColorCube():
    """육색 정육면체 그리기
    
        윗면	빨간색 (glColor3f(1.0, 0.0, 0.0))	y = +1 평면
        아랫면	주황색 (glColor3ub(255, 150, 0))	y = -1 평면
        앞면	파란색 (glColor3f(0.0, 0.0, 1.0))	z = +1 평면
        뒷면	녹색 (glColor3f(0.0, 1.0, 0.0))	    z = -1 평면
        왼쪽면	노란색 (glColor3f(1.0, 1.0, 0.0))	x = -1 평면
        오른쪽면	흰색 (glColor3f(1.0, 1.0, 1.0))	x = +1 평면
    
    glVertex3f로 꼭짓점을 4개 정의
    glVertex3f(x, y, z)는 3D 공간상의 꼭짓점을 지정합니다.
        
    """
    glBegin(GL_QUADS)  # 여러 사각형 그리
    glColor3f(1.0, 0.0, 0.0)  # 빨간색
    # glColor3f(r, g, b) — 부동소수점 방식
    # 각 색상값은 0.0~1.0 사이의 실수값으로 표현
    # 색상강도를 정규화된 값으로 표현
    # 부드러운 색상 조절이 가능
    # 그래픽 프로그램에서 조명, 혼합등을 다룰때 자주 사용
        
    # 입체적인 육면 그리기
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)

    glColor3ub(255, 150, 0) #주황색
    # glColor3ub(r, g, b) — 정수 방식
    # 각 색상값은 0~255 사이의 정수값으로 표현
    # 우리가 보는 RGB 색상값과 동일한 방식
    # 이미지 처리나 픽셀기반 색상 지정에 직관적
    # 색상 테이블이나 외부이지지 데이타를 사용할 때 유용
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)

    glColor3f(0.0, 0.0, 1.0)  # 파란색
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    glColor3f(0.0, 1.0, 0.0)  # 녹색
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)

    glColor3f(1.0, 1.0, 0.0)  # 노란색
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)

    glColor3f(1.0, 1.0, 1.0)  # 흰색
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glEnd()

def init():
    global WIDTH, HEIGHT
    # OpenGL에서 깊이 버퍼(Depth Buffer)를 설정
    # 물체의 앞 뒤 관계를 판단하는데 핵심적인 역할을 담장
   # 깊이 캐시 설정
   # 이 함수는 glClear(GL_DEPTH_BUFFER_BIT) 호출 시, 깊이 버퍼를 어떤 값으로 초기화할지를 지정합니다.
   # 기본적으로 1.0은 최대 깊이값을 의미하며, 일반적으로 가장 먼 거리를 나타냅니다.
    # 즉, 화면을 새로 그릴 때 모든 픽셀의 깊이 값을 최대로 설정해서, 이후 그려지는 물체들이 이 값을 기준으로 비교될 수 있도록 합니다.
    # glClearDepth(1.0)
    # 깊이 테스트 종류 설정
    # glDepthFunc(GL_LESS)
    # 이 함수는 OpenGL이 새로 그릴 픽셀의 깊이값과 현재 깊이 버퍼에 저장된 값을 비교할 때 사용하는 기준을 설정합니다.
    # GL_LESS는 "새 픽셀이 더 가까울 경우에만 그려라"는 의미입니다.
    # 즉, 카메라에 더 가까운 물체만 화면에 표시되도록 하여, 뒤에 있는 물체는 가려지게 됩니다.
        
    # 깊이 테스트 허용하기
    glEnable(GL_DEPTH_TEST)

    # 카메라 시점과 모델 위치를 설정하는 핵심 부분
    
    # OpenGL에게 투영 행렬(Projection Matrix)을 설정하겠다고 알려주는 명령
    # 영 행렬은 카메라의 시야각, 화면 비율, 원근감 등을 결정
    glMatrixMode(GL_PROJECTION) 
    
    # 현재 선택된 행렬(여기선 투영 행렬)을 초기화합니다.
    #즉, 이전에 설정된 카메라 정보나 변환을 모두 지우고 기본 상태로 되돌립니다.
    glLoadIdentity()
    
    # 원근 투영(Perspective Projection)을 설정합니다.
    # 인자 설명:
    # 45.0: 시야각(FOV, Field of View) — 카메라가 보는 각도 (좁으면 줌인, 넓으면 줌아웃)
    # WIDTH / HEIGHT: 화면의 종횡비 (aspect ratio) — 왜곡 방지
    # 1: 가까운 클리핑 거리 (near plane) — 카메라에서 1단위 거리보다 가까운 건 안 보임
    # 10: 먼 클리핑 거리 (far plane) — 10단위 거리보다 먼 건 안 보임
    #이 설정은 마치 카메라 렌즈를 조절하는 것과 같아요.
    gluPerspective(45.0, float(WIDTH) / float(HEIGHT), 1, 10)  #
    
    
    # 이제부터는 모델뷰 행렬(ModelView Matrix)을 설정하겠다는 뜻입니다.
    # 모델뷰 행렬은 객체의 위치, 회전, 크기 등을 조절
    glMatrixMode(GL_MODELVIEW)
    
    # 현재 모델을 x축으로 1.5만큼 오른쪽, z축으로 -7만큼 뒤로 이동시킵니다.
    # 즉, 카메라에서 멀리 떨어진 위치에 큐브를 배치
    glTranslatef(1.5, 0.0, -7.0)

def update(): # OpenGL에서 화면을 갱신하고 큐브를 회전시키는 핵심 루틴
    # 화면을 새로 그리기 전에 컬러 버퍼와 깊이 버퍼를 초기화합니다.
    # 이전 프레임의 잔상이 남지 않도록 지워주는 역할이에요.
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # x, y축 둘레 0.005도 회전
    # 현재 모델뷰 행렬에 회전 변환을 추가합니다.
    # glRotate(angle, x, y, z)는 지정된 축(x, y, z)을 기준으로 angle만큼 회전시킵니다.
    # 여기서는 x축과 y축 방향으로 동시에 0.005도씩 회전 → 대각선 방향 회전처럼 보입니다.
    # 참고: glRotate()는 누적 방식이기 때문에, update()가 반복 호출되면 큐브가 계속 회전합니다.
    glRotate(0.005, 1.0, 1.0, 0.0)

    # 사용자가 정의한 함수로 색상이 입혀진 정육면체를 화면에 그림.
    drawColorCube()
    
    # 더블 버퍼링을 사용하여 화면 깜빡임 없이 부드럽게 렌더링합니다.
    # 백 버퍼에서 그린 내용을 프론트 버퍼로 전환하여 사용자에게 보여줍니다.
    glutSwapBuffers()  # 스왑 캐시


# GLUT 라이브러리를 초기화합니다.
# 내부적으로 명령줄 인자를 처리하고, 윈도우 시스템과 연결을 설정해요.
glutInit()

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB) #디스플레이 모드를 설정
# GLUT_DOUBLE: 더블 버퍼링 사용 → 깜빡임 없이 부드러운 렌더링
# GLUT_RGB: RGB 색상 모드 사용

glutInitWindowSize(WIDTH, HEIGHT) # 생성할 윈도우의 크기를 지정
glutCreateWindow(b'PyOpenGL cube') # 실제 윈도우를 생성하고, 제목을 설정
init()  # 사용자 정의 초기화 함수 호출
#여기서 배경색 설정, 조명, 뷰포트, 투영 설정 등을 할 수 있어요
glutDisplayFunc(update) # 화면을 다시 그릴 때 호출되는 콜백 함수 등록  update() 함수가 큐브를 그리고 회전시키는 역할을 합니다
glutIdleFunc(update) # 프로그램이 유휴 상태일 때 계속 update()를 호출 결과적으로 큐브가 계속 회전하며 애니메이션처럼 보입니다
glutMainLoop() # 이벤트 루프 시작 키보드, 마우스, 윈도우 이벤트를 처리하며 프로그램이 종료될 때까지 계속 실행됩니다
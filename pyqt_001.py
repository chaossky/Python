# 필요한 모듈을 불러온다.
# 기본적인 UI 구성 요소를 제공하는 위젯 (클래스)는 
# PyQT5.QtWidgets 모듈에 포함
import sys
# sys 모듈은 파이썬의 시스템 관련 기능을 다룰 수 있게 해주는 표준 라이브러리 중 하나
# 이 모듈을 사용하면 파이썬 인터프리터와 관련된 다양한 정보를 얻거나 제어
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication

# QApplication:
# PyQt 애플리케이션의 기본 환경을 설정하는 클래스
# 이벤트 루프를 관리하고, 전체 GUI 프로그램의 실행을 담당.

# QWidget:
# 기본 윈도우 창을 나타내는 클래스
# 버튼, 텍스트박스 등 다양한 위젯을 담을 수 있는 컨테이너 역할.

# QPushButton:
# 클릭 가능한 버튼을 생성하는 클래스.
# 사용자 인터랙션을 처리.

class MyApp(QWidget):

  def __init__(self):
      super().__init__()
      self.initUI()
      # MyApp 클래스는 QWidget을 상속받고 있습니다. 
      # super()는 부모 클래스인 QWidget을 참조하는 함수입니다.
      # super().__init__()는 QWidget의 생성자를 호출하여 윈도우 창을 초기화합니다.
      # self는 MyApp 객체를 말한다.
      # super는 부모클래스인 QWidget을 가리킨다. 
      # __init__()의 핵심 개념
      # 객체가 생성될 때 실행되는 초기 설정 함수
      # 클래스 내부에 정의된 변수나 상태를 초기화하는 데 사용
      # self는 생성된 객체 자신을 참조하는 키워드
        
  def initUI(self):
      btn = QPushButton('Quit', self)
      btn.move(50, 50) #위젯을 스크린의 x=300px,y=300px 위치로 이동
      btn.resize(btn.sizeHint()) # PyQt에서 버튼의 크기를 자동으로 설정하는 코드
      btn.clicked.connect(QCoreApplication.instance().quit)

      self.setWindowTitle('Quit Button') #타이틀바에 나타나는 창의 제목 설정
      self.setGeometry(300, 300, 300, 200)
      self.show() #위젯을 스크린에 보여준다.
    # 
    #     PyQt에서 윈도우 창의 위치와 크기를 설정하는 코드입니다.
    #     이 메서드는 총 4개의 인자를 받는데, 각각의 의미는 다음과 같아요:
    #     📐 setGeometry(x, y, width, height)의 의미
    #     x	: 화면의 왼쪽에서부터 창의 시작 위치 (300px)
    #     y	: 화면의 위쪽에서부터 창의 시작 위치 (300px)
    #     width : 창의 너비 (300px)
    #     height :	창의 높이 (200px)
    # 
      

if __name__ == '__main__': #'__name__'은 현재 모듈의 이름이 저장되는 내장변수
    app = QApplication(sys.argv) #PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 합니다.
    ex = MyApp()
    sys.exit(app.exec_())
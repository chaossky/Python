import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
current_path=os.getcwd()# 현재 작업할 디렉토리

filename="test002.ui" # 작업할 파일명을 여기에 적어 넣는다.

#현재 작업 디렉토리 + 프로젝트 디렉토리 + 파일명을 합쳐서 파일이 있는 경로 생성
get_file_location=current_path+"\\PYQT\\"+filename 

# 폼 클래스가 있는 곳을 알려주고 그 파일을 로드한다.
form_class = uic.loadUiType(get_file_location)[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        """
        ---------------------------------------------
        이 부분에 시그널을 입력해야 합니다.
        시그널이 작동할 때 실행될 기능은 보통 이 클래스의 멤버함수로 작성합니다.
        ---------------------------------------------

        
        """
        # 메뉴에 만들어 놓은 각각의 메뉴에 액션이 QT 디자이너를 통해 만들어졌거나, 
        # 개발자가 구성을 해놓은(입력해 놓았다.) 그것을 함수와 연결.
        self.file_new.triggered.connect(self.newFunc)
        self.file_new_window.triggered.connect(self.newwindowFunc)
        self.file_open.triggered.connect(self.openFunc)
        self.file_save.triggered.connect(self.saveFunc)
        self.file_saveas.triggered.connect(self.saveasFunc)
        self.file_page.triggered.connect(self.pageFunc)
        self.file_print.triggered.connect(self.printFunc)
        self.file_exit.triggered.connect(self.exitFunc)


    #함수를 만들어 준다. 위에서 시그널 받은 것을 함수에 연결
    # 함수에서는 그 것에 맞는 것을 구현하면 된다.
    def newFunc(self):
        print("new")

    def newwindowFunc(self):
        print("new window")

    def openFunc(self):
        # 열기(open)을 메뉴에서 선택하면 탐색기가 실행되면서 폴더와 파일을 선택할수 있게 된다.)
        # 어떤 한 파일을 선택하면 그 파일 이름을 가지고 온다.
        #[0]이라는 인덱스는 여러개를 선택 했을 경우 제일 처음의 파일 만 가지고 오도록한다.
        fname=QFileDialog.getOpenFileName(self)
        # open할 파일 이름이 정해졌다면......
        if fname[0]:
            # 그 파일을 UTF8 형식으로 인코딩하여 f라는 변수로 가지고 온다.
            with open(fname[0],encoding='UTF8') as f:
                # 파일을 읽기 메소드로 읽은후 그 내용을 data라는 변수에 저장한다.
                data=f.read()
            # data변수에 저장된 값을 QT Designer로 만든 GUI 창의 plainText 창에 세팅한다.
            self.plainTextEdit.setPlainText(data)
            # print(fname[0])
            # plainTextEdit
            print("{} open!!".format(fname[0]))
    
    def saveFunc(self):
        # 저장(save)을 메뉴에서 선택하면 탐색기가 실행되면서 
        # 저장할 폴더와 파일 이름을 넣을 수 있게 된다.)
        fname=QFileDialog.getSaveFileName(self)
    # 저장할 파일 이름을 지정하였다면...... 
        if fname[0]:
             # data라는 변수에 plainTextEdit에 입력된 내용을 일반 텍스트 형식으로 
             # 가져온다.
            data=self.plainTextEdit.toPlainText()
            # 입력된 파일이름을 가지고 data 내용을 UTF8 형식으로 인코딩하여 
            # f라는 변수로 가지고 온다.
            with open(fname[0],'w',encoding='UTF8') as f:
                # 파일을 쓰기 메소드로 data라는 변수에 저장된 내용을 쓴다.
                f.write(data)
            print("{} saved!!".format(fname[0]))

    def saveasFunc(self,file_name):#파일명을 한번 정해보았다.
        print("file saved as~~~!!",file_name)
    
    def pageFunc(self):
        print("show page")

    def printFunc(self):
        print("print!!!!")

    def exitFunc(self):
        print("Exit !!! Good Bye")
        #창을 닫는 코드를 넣어보아라!

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
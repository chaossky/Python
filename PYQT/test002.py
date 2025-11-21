import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic

# UI 파일을 로드할 경로를 구성합니다.
# 현재 작업 디렉토리를 기준으로 하며, 
# 실제 배포나 이식성 측면에서는 os.path.join 사용을 권장합니다.
current_path = os.getcwd()  # 현재 작업 디렉토리 절대 경로

filename = "test002.ui"  # 사용할 Qt Designer UI 파일명

# 현재 작업 디렉토리 하위의 PYQT 폴더에 있는 UI 파일을 직접 문자열 결합으로 지정합니다.
# 윈도우 전용 경로 구성이므로 다른 OS에서는 동작이 달라질 수 있습니다.
get_file_location = current_path + "\\PYQT\\" + filename

# uic.loadUiType은 .ui 파일로부터 (폼 클래스, 베이스 클래스) 튜플을 생성합니다.
# [0]을 사용해 폼 클래스만 가져옵니다.
form_class = uic.loadUiType(get_file_location)[0]

# QMainWindow와 UI 폼 클래스를 다중 상속하여, setupUi로 위젯들을 초기화합니다.
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        # UI 파일에 정의된 위젯/액션을 현재 인스턴스(self)에 바인딩합니다.
        self.setupUi(self)

        """
        ---------------------------------------------
        시그널/슬롯 연결 구간입니다.
        Qt Designer에서 정의된 QAction들을 Python 메서드에 연결합니다.
        ---------------------------------------------
        """
        # QAction의 triggered 시그널은 기본적으로 bool 인자를 전달할 수 있습니다
        # (체크 가능한 액션일 경우).
        # 연결된 메서드 시그니처가 이를 수용하는지 확인하는 것이 안전합니다.
        self.file_new.triggered.connect(self.newFunc)
        self.file_new_window.triggered.connect(self.newwindowFunc)
        self.file_open.triggered.connect(self.openFunc)
        self.file_save.triggered.connect(self.saveFunc)
        self.file_saveas.triggered.connect(self.saveasFunc)  # triggered(bool)과 연결됨
        self.file_page.triggered.connect(self.pageFunc)
        self.file_print.triggered.connect(self.printFunc)
        self.file_exit.triggered.connect(self.exitFunc)

    # 새 문서 생성 등의 동작을 수행할 수 있는 슬롯입니다.
    def newFunc(self):
        print("new")

    # 새 창 열기 등의 동작을 수행할 수 있는 슬롯입니다.
    def newwindowFunc(self):
        print("new window")

    def openFunc(self):
        # 파일 열기 대화상자를 띄워 사용자가 선택한 파일 경로를 가져옵니다.
        # 반환값은 (선택된 파일 경로 문자열, 선택된 필터 문자열)의 튜플입니다.
        fname = QFileDialog.getOpenFileName(self)
        # 파일 경로가 비어 있지 않을 때만 파일을 엽니다.
        if fname[0]:
            # UTF-8 인코딩으로 텍스트 파일을 읽어들입니다.
            with open(fname[0], encoding='UTF8') as f:
                data = f.read()
            # 읽은 내용을 plainTextEdit 위젯에 설정합니다.
            self.plainTextEdit.setPlainText(data)
            # 파일이 열렸을때 확인을 위한 코드 - 주석처리
            # print("{} open!!".format(fname[0]))

    def saveFunc(self):
        # 파일 저장 대화상자를 띄워 저장할 경로를 선택받습니다.
        # 반환값은 (저장할 파일 경로 문자열, 선택된 필터 문자열)의 튜플입니다.
        fname = QFileDialog.getSaveFileName(self)
        # 사용자가 경로를 지정했을 때만 저장을 수행합니다.
        if fname[0]:
            # plainTextEdit의 내용을 일반 텍스트로 추출합니다.
            data = self.plainTextEdit.toPlainText()
            # UTF-8 인코딩으로 파일을 생성/덮어쓰기 합니다.
            with open(fname[0], 'w', encoding='UTF8') as f:
                f.write(data)
            # 파일이 저장된 것을 확인하기 위한 코드- 주석처리
            # print("{} saved!!".format(fname[0]))

    def saveasFunc(self, file_name):
        # QAction.triggered는 일반적으로 bool(체크 상태)을 전달합니다.
        # 여기서는 그 값을 file_name 인자로 받아 출력만 합니다.
        # 실사용에서는 파일명 문자열을 받지 않으므로, Save As 동작을 구현하려면
        # 별도의 QFileDialog.getSaveFileName 호출이 필요합니다.
        print("file saved as~~~!!", file_name)

    def pageFunc(self):
        # 페이지 설정 또는 관련 동작을 수행할 자리입니다.
        print("show page")

    def printFunc(self):
        # 인쇄 동작을 수행할 자리입니다. QPrinter/QPrintDialog 활용을 고려할 수 있습니다.
        print("print!!!!")

    def exitFunc(self):
        # 종료 동작을 수행합니다. 현재는 콘솔 메시지 출력만 하고 있습니다.
        # 실제로 창을 닫으려면 self.close() 호출을 추가하세요.
        print("Exit !!! Good Bye")
        self.close()

if __name__ == "__main__":
    # QApplication은 Qt 애플리케이션의 진입점으로, 이벤트 루프를 관리합니다.
    app = QApplication(sys.argv)

    # 메인 윈도우 인스턴스를 생성합니다.
    myWindow = WindowClass()

    # 메인 윈도우를 화면에 표시합니다.
    myWindow.show()

    # 이벤트 루프에 진입하여 사용자 입력/시스템 이벤트를 처리합니다.
    # 일반적으로 sys.exit(app.exec_()) 형태로 반환 코드를 OS에 전달하는 것이 관례입니다.
    app.exec_()

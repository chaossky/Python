from pynput import mouse
import time
import threading
import signal
import sys

# 전역 종료 플래그
running = True

def signal_handler(sig, frame):
    """Ctrl+C 시그널 처리"""
    global running
    print("\n프로그램을 종료합니다...")
    running = False
    sys.exit(0)

def on_click(x, y, button, pressed):
    """마우스 클릭 이벤트 처리"""
    global running
    if not running:
        return False  # 리스너 종료
        
    if pressed:
        if button == mouse.Button.left:
            print(f"왼쪽 버튼 클릭 - 위치: ({x}, {y})")
        elif button == mouse.Button.right:
            print(f"오른쪽 버튼 클릭 - 위치: ({x}, {y})")
        elif button == mouse.Button.middle:
            print(f"중간 버튼 클릭 - 위치: ({x}, {y})")

def on_move(x, y):
    """마우스 이동 이벤트 처리 (선택사항)"""
    global running
    if not running:
        return False  # 리스너 종료
    # 마우스 이동이 너무 많이 출력되므로 주석 처리
    # print(f"마우스 이동 - 위치: ({x}, {y})")
    pass

def position_thread():
    """현재 마우스 위치를 주기적으로 출력하는 쓰레드"""
    global running
    while running:
        try:
            # 현재 마우스 위치 가져오기
            import tkinter as tk
            root = tk.Tk()
            root.withdraw()  # 윈도우 숨기기
            x = root.winfo_pointerx()
            y = root.winfo_pointery()
            root.destroy()
            
            if running:  # 종료되지 않았을 때만 출력
                print(f"현재 마우스 위치: ({x}, {y})")
            
            # 0.5초씩 나누어 체크하여 빠른 종료 가능
            for _ in range(10):  # 총 5초 대기
                if not running:
                    break
                time.sleep(0.5)
                
        except Exception as e:
            if running:
                time.sleep(1)
            break

if __name__ == "__main__":
    # Ctrl+C 시그널 핸들러 등록
    signal.signal(signal.SIGINT, signal_handler)
    
    print("마우스 입력 감지를 시작합니다...")
    print("프로그램을 종료하려면 Ctrl+C를 누르세요.")
    
    # 현재 위치 출력 쓰레드 시작
    position_thread_obj = threading.Thread(target=position_thread, daemon=True)
    position_thread_obj.start()
    
    # 마우스 리스너 설정
    try:
        with mouse.Listener(
            on_click=on_click,
            on_move=on_move
        ) as listener:
            while running:
                time.sleep(0.1)  # 짧은 간격으로 체크
    except KeyboardInterrupt:
        pass
    finally:
        running = False
        print("\n프로그램이 종료되었습니다.")
        listener.stop()  # 리스너 종료
        
        
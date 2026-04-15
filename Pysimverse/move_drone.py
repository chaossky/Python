from pysimverse import Drone
import threading
import time
import keyboard

step_size = 10
drone = Drone()
running_actions = {}  # 현재 실행 중인 키별 쓰레드 관리

def ready():
    drone.connect()
    drone.take_off(takeoff_height=140,takeoff_speed=400)
    drone.set_speed(400)

def continuous_action(key, func):
    while running_actions.get(key, False):
        func(step_size)
        time.sleep(0.1)  # 너무 빠르게 호출되지 않도록 딜레이

def start_action(key, func, continuous=True):
    if continuous:
        # 키가 눌리면 쓰레드 시작
        if not running_actions.get(key, False):
            running_actions[key] = True
            threading.Thread(target=continuous_action, args=(key, func), daemon=True).start()
    else:
        # 한 번만 실행되는 함수
        func()

def stop_action(key):
    # 키가 떼어지면 해당 쓰레드 종료
    running_actions[key] = False

# 키 매핑
key_actions = {
    'up':    {'func': drone.move_forward, 'arg': step_size, 'continuous': True},
    'down':  {'func': drone.move_backward, 'arg': step_size, 'continuous': True},
    'left':  {'func': drone.move_left, 'arg': step_size, 'continuous': True},
    'right': {'func': drone.move_right, 'arg': step_size, 'continuous': True},
    'z':     {'func': drone.rotate, 'arg': -1*step_size, 'continuous': True},  # 반시계 방향
    'x':     {'func': drone.rotate, 'arg': step_size, 'continuous': True},   # 시계 방향
    'l':     {'func': drone.land, 'arg': None, 'continuous': False},   # 착륙은 한 번만 실행
}

def main():
    ready()

    # 키 눌림 이벤트
    def on_press(event):
        if event.name == 'q':
            exit()
        action = key_actions.get(event.name)
        if action:
            start_action(event.name, action['func'], action['continuous'])

    # 키 뗌 이벤트
    def on_release(event):
        if event.name in key_actions and key_actions[event.name]['continuous']:
            stop_action(event.name)

    keyboard.on_press(on_press)
    keyboard.on_release(on_release)

    keyboard.wait('q')  # 'q' 누르면 종료

if __name__ == "__main__":
    main()

from pysimverse import Drone
import time
import keyboard

step_size = 10
drone = Drone()

def ready():
    drone.connect()
    drone.take_off(takeoff_height=140,takeoff_speed=400)
    drone.set_speed(300)

def main():
    key_actions = {
        'z': lambda: drone.move_up(step_size),
        'c': lambda: drone.move_down(step_size),
        'w': lambda: drone.move_forward(step_size),
        's': lambda: drone.move_backward(step_size),
        'a': lambda: drone.move_left(step_size),
        'd': lambda: drone.move_right(step_size),
        'q': lambda: drone.rotate(-step_size),
        'e': lambda: drone.rotate(step_size),
        'l': lambda: drone.land(),
    }
    ready()
    
    while True:

        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'esc':
                break
            action = key_actions.get(event.name)
            if action:
                action()


if __name__ == "__main__":
    main()

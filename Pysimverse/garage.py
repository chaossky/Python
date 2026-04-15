from pysimverse import Drone
import time
import keyboard

step_size=10
drone=Drone()

def ready():
    drone.connect()
    drone.take_off()

def main():
    key_actions = {
        'up':    lambda: drone.move_up(step_size),
        'down':  lambda: drone.move_down(step_size),
        'left':  lambda: drone.move_left(step_size),
        'right': lambda: drone.move_right(step_size),
        'w': lambda:drone.move_forward(step_size),
        's': lambda:drone.move_backward(step_size),
        'a': lambda:drone.move_left(10),
        'd': lambda:drone.move_right(10),
        'r': lambda:drone.rotate(step_size),
        'l': lambda:drone.land(),
        
    }
    ready()
    while True:
        event=keyboard.read_event()
        if event.event_type==keyboard.KEY_DOWN:
            if event.name=='q':
                break
            action=key_actions.get(event.name)
            if action:
                action()
                
if __name__ == "__main__":
    main()


 
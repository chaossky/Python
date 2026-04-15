from pysimverse import Drone
import time

drone=Drone()
drone.connect()
drone.take_off()

drone.move_down(20)
time.sleep(2)
drone.move_up(30)
time.sleep(2)
drone.move_right(30)
time.sleep(2)
drone.move_left(20)
time.sleep(2)
drone.move_forward(70)
time.sleep(2)
drone.move_backward(50)
time.sleep(2)

left_right=0
forward_backward=50
up_down=0
yaw=0

while True:
    drone.send_rc_control(left_right,forward_backward,up_down,yaw)

drone.land()
time.sleep(1)

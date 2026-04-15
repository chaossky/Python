from pysimverse import Drone
import time
import cv2

drone=Drone()
drone.connect()
time.sleep(2)
drone.streamon()
drone.take_off()

while True:
    frame, is_success = drone.get_frame()
    if is_success and frame is not None and frame.size > 0:
        cv2.imshow("Drone Feed", frame)
    else:
        print("Frame not available")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

drone.land()
time.sleep(1)
cv2.destroyAllWindows()

import pybullet as p
import pybullet_data
import time

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.loadURDF("plane.urdf")
ball=p.loadURDF("sphere2.urdf",[0,0,2])
p.setGravity(0,0,-9.8)
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/240)
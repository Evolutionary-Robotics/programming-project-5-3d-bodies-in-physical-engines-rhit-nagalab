import pybullet as p
import pybullet_data
import pyrosim.pyrosim as ps
import numpy as np
import time 
import matplotlib.pyplot as plt

physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
#p.loadSDF("box.sdf")
robotId = p.loadURDF("body.urdf")


duration = 100000

ps.Prepare_To_Simulate(robotId)

x = np.linspace(0,10*np.pi, duration)
y = np.sin(x)*np.pi/2
negY = np.negative(y)

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("Sin plot vs time")
plt.xlabel("Time")
plt.ylabel("Y-value")

plt.subplot(1, 2, 2)
plt.plot(x,negY)
plt.title("Negative sin plot vs time")
plt.xlabel("Time")
plt.ylabel("Y-value")

plt.show()




for i in range(duration):
    ps.Set_Motor_For_Joint(bodyIndex = robotId, 
                           jointName = b'Foot_Torso1',
                           controlMode = p.POSITION_CONTROL,
                           targetPosition = y[i],
                           maxForce = 500)
    ps.Set_Motor_For_Joint(bodyIndex = robotId, 
                           jointName = b'Foot_Torso2',
                           controlMode = p.POSITION_CONTROL,
                           targetPosition = -y[i],
                           maxForce = 1500)
    p.stepSimulation()
    time.sleep(1/500)

p.disconnect()
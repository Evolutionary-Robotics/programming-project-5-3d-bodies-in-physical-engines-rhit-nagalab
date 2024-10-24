import pyrosim.pyrosim as ps

# Global parameters
l = 2.5 # length
w = 1 # width 
h = 1 # height 

x = 0
y = 0
z = 0.5

def Create_World():
    ps.Start_SDF("box.sdf")
    for i in range(10):
        ps.Send_Cube(name="Box",pos=[x,y,z],size=[l,w,h])
        z += h
        l = 0.9 * l
        w = 0.9 * w
        h = 0.9 * h
    ps.End()

def Create_Robot():
    ps.Start_URDF("body.urdf")
    
    ps.Send_Cube(name="Foot1",pos=[x,y,z],size=[l,w,h]) # Parent
    ps.Send_Joint(name="Foot_Torso1", parent="Foot1", child="Torso", type="revolute", position = [0.5,0,1.0])
    ps.Send_Cube(name="Torso",pos=[0.5,0.0,0.5],size=[l,w,h]) # Child
    ps.Send_Cube(name= "Foot2",pos=[x,y,-z],size=[l,w,h])
    ps.Send_Joint(name="Foot_Torso2", parent="Torso", child="Foot2", type="revolute", position = [0.5,0,0])
    

    '''
    ps.Send_Cube(name="Body",pos=[0,0,0],size=[2,2,2])
    ps.Send_Joint(name="BodyJoint1", parent="Body", child="Body1", type="revolute", position = [1.5,0,0])
    ps.Send_Cube(name = "Body1", pos = [1.5,0,0],size=[1.5,1.5,1.5])
    '''
    ps.End()

Create_Robot()

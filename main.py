import time
GRAVITY = 6.67430 * 10 ** -11
EARTH_MASS = 5.97219 * 10 ** 24
EARTH_RADIUS = 6.371 * 10 ** 6
earthPos = (0,0)
class Spacecraft:
    def __init__(self, mass, position, velocity):
        self.mass = mass #in Kg
        self.position = position #a coordinate
        self.velocity = velocity #a vector
    def updatePosAndVel(self, force, time_step):
        acceleration = (force[0] / self.mass, force[1] / self.mass)
        self.velocity = (self.velocity[0] + acceleration[0] * time_step, 
                                self.velocity[1] + acceleration[1] * time_step)
        self.position = (self.position[0] + self.velocity[0] * time_step,
                         self.position[1] + self.velocity[1] * time_step)
    def getPos(self):
        return (self.position[0], self.position[1] - EARTH_RADIUS)
    
def simulate(Spacecraft, duration):
    for _ in range(duration):
        Fth = thrustForce(10)
        Fg = gravForce(Spacecraft, earthPos)
        Fn = normForce(Spacecraft)
        force = (Fth[0] + Fg[0] + Fn[0], Fth[1] + Fg[1] + Fn[1])
        print("Thrust", Fth)
        print("Gravity", Fg)
        print("Normal", Fn)
        Spacecraft.updatePosAndVel(force, 1)
        print("Velocity", Spacecraft.velocity)
        print("Position", Spacecraft.getPos())
        time.sleep(1)        
        
def gravForce(Spacecraft, earthPos):
    distanceX = Spacecraft.position[0] - earthPos[0]
    distanceY = Spacecraft.position[1] - earthPos[1]
    distance = (distanceX ** 2 + distanceY ** 2) ** .5
    gravForce = (GRAVITY * EARTH_MASS * Spacecraft.mass) / (distance ** 2)
    gravForceX = gravForce * distanceX / distance
    gravForceY = gravForce * distanceY / distance
    return (-gravForceX, -gravForceY)

def thrustForce(numberOfThrusters):
    return (0, numberOfThrusters * 1000)

def normForce(Spacecraft):
    Fg = gravForce(Spacecraft, earthPos)
    if Spacecraft.position[1] <= EARTH_RADIUS:
        return (-Fg[0], -Fg[1])
    return (0,0)
    
    
mass = 1000
position = (0,EARTH_RADIUS)
velocity = (0, 0)

firstSpaceCraft = Spacecraft(mass, position, velocity)

simulate(firstSpaceCraft, 5)


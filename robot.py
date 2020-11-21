from controller import Robot, DistanceSensor, Motor, LED, Speaker
import time

# time in [ms] of a simulation step
TIME_STEP = 64

MAX_SPEED = 6.28

# create the Robot instance.
robot = Robot()
#instanciamos cada led, cuando la función sea llamada recibirá también el argumento 'ledx'
led1 = LED('led1')
led2 = LED('led2')
led3 = LED('led3')
led4 = LED('led4')
led5 = LED('led5')
led6 = LED('led6')
#instanciamos el speaker
speaker = Speaker('speaker')
# initialize devices
ps = []
psNames = [
    'ps0', 'ps1', 'ps2', 'ps3',
    'ps4', 'ps5', 'ps6', 'ps7'
]

for i in range(8):
    ps.append(robot.getDistanceSensor(psNames[i]))
    ps[i].enable(TIME_STEP)

leftMotor = robot.getMotor('left wheel motor')
rightMotor = robot.getMotor('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)

def actionRectangle():
    reset()
    led1.set(1)
    led2.set(1)
    led3.set(1)

def actionTriangle():
    reset()
    led4.set(1)
    led5.set(1)
    led6.set(1)
def actionCircle():
    reset()
    speaker.setLanguage('es-ES')
    speaker.speak('Circulo',1)
def actionStar():
    reset()
    speaker.playSound(speaker,speaker,'marcianito.mp3', 1, 1, 1, False)
 # playSound(left, right, sound, volume, pitch, balance, loop):
 # https://www.cyberbotics.com/doc/reference/speaker?tab-language=python  
    leftMotor.setVelocity( 0.5 * MAX_SPEED)
    rightMotor.setVelocity( 0)
    time.sleep(5)
    leftMotor.setVelocity(0)
    rightMotor.setVelocity( 0.5 * MAX_SPEED)
    

def reset():
    led1.set(0)
    led2.set(0)
    led3.set(0)
    led4.set(0)
    led5.set(0)
    led6.set(0)
    time.sleep(0.5)



# feedback loop: step simulation until receiving an exit event
while robot.step(TIME_STEP) != -1:
    actionStar()
    

## Code for robomaster course

import time
from robomaster import robot, led, blaster

funcRobot = robot.Robot()
funcRobot.initialize(conn_type="sta")

chassis = funcRobot.chassis
gimbal = funcRobot.gimbal
ledCtrl = funcRobot.led
blasterCtrl = funcRobot.blaster
vision = funcRobot.vision

# Utility functions
def resetPoint():
    print("Resetting position...")
    time.sleep(5)


def handlePost(marker):
    if marker == "F":
        print("Engaging target...")
        blasterCtrl.fire()
    elif marker == "D":
        print(" Skipping post...")
    elif marker == "P":
        print("Returning to A and back...")
        returnToStart()
        goToPost()
    else:
        print("Unknown marker")

def fMarker(marker):
    if marker == "1":
        print("Doing Chassis and Gimbal actions.")
        chassis.move(x=0.2, y=0, z=90, xy_speed=0.5).waitForComplete()
        gimbal.moveto(pitch=20, yaw=0).waitForComplete()
    elif marker == "2":
        print("Flashing LEDs.")
        ledCtrl.setLED.comp = led.ALL, r=255, g=0, b=0, effect=led.EFFECT_BREATH
    elif marker == "3":
        print("Doing both Gimbal and LED actions.")
        fMarker("1")
        fMarker("2")

def returnToStart():
    chassis.move(x=-2, y=0, z=0, xy_speed=0.5).waitForComplete()

def goToPost():
    chassis.move(x=2, y=0, z=0, xy_speed=0.5).waitForComplete()

# Starting course
print("Starting at A")
resetPoint()

print("Navigating to B")
# Simulated line following
chassis.move(x=1.5, y=0, z=0, xy_speed=0.3).waitForComplete()
resetPoint()

# Post C
print("At Post C")
marker = ()
handlePost(marker)
resetPoint()

# Post E
print("At Post E")
marker = ()
handlePost(marker)
resetPoint()

# Skip D
print("D (Reset Point)")
resetPoint()

# Post G
print("At Post G")
marker = ()
handlePost(marker)
resetPoint()

# F Marker Interaction
print("At F Marker")
marker = ()
fMarker(marker)
resetPoint()

# H Turnaround
print("Reached H Turnaround point")
resetPoint()

# Return path
print("Returning D Interaction")

# Do something new here 
ledCtrl.setLED.comp = led.ALL, r=0, g=255, b=0, effect=led.FLASH
resetPoint()

print("End of course")
chassis.move(x=-2, y=0, z=0, xy_speed=0.5).waitForComplete()

funcRobot.close()

import XboxController
import RPi.GPIO as GPIO
import time

global l, r, f, b, s, fr, fl, br, bl, lx, ly, motion
global flf, flb, frf, frb, blf, blb, brf, brb

frf = 17
frb = 27
flf = 10
flb = 9
blf = 23
blb = 24
brf = 14
brb = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(flf, GPIO.OUT)
GPIO.setup(flb, GPIO.OUT)
GPIO.setup(frf, GPIO.OUT)
GPIO.setup(frb, GPIO.OUT)
GPIO.setup(blf, GPIO.OUT)  # Corrected indentation
GPIO.setup(blb, GPIO.OUT)
GPIO.setup(brf, GPIO.OUT)
GPIO.setup(brb, GPIO.OUT)

def run():
    if motion == "Forward":
        GPIO.output(flf, GPIO.HIGH)
        GPIO.output(frf, GPIO.HIGH)
        GPIO.output(blf, GPIO.HIGH)
        GPIO.output(brf, GPIO.HIGH)
        GPIO.output(flb, GPIO.LOW)
        GPIO.output(frb, GPIO.LOW)
        GPIO.output(blb, GPIO.LOW)
        GPIO.output(brb, GPIO.LOW)
    elif motion == "Backward":
        GPIO.output(flf, GPIO.LOW)
        GPIO.output(frf, GPIO.LOW)
        GPIO.output(blf, GPIO.LOW)
        GPIO.output(brf, GPIO.LOW)
        GPIO.output(flb, GPIO.HIGH)
        GPIO.output(frb, GPIO.HIGH)
        GPIO.output(blb, GPIO.HIGH)
        GPIO.output(brb, GPIO.HIGH)
    elif motion == "Front Left":
        GPIO.output(flf, GPIO.LOW)
        GPIO.output(frf, GPIO.HIGH)
        GPIO.output(blf, GPIO.LOW)
        GPIO.output(brf, GPIO.HIGH)
        GPIO.output(flb, GPIO.LOW)
        GPIO.output(frb, GPIO.LOW)
        GPIO.output(blb, GPIO.LOW)
        GPIO.output(brb, GPIO.LOW)
    elif motion == "Front Right":
        GPIO.output(flf, GPIO.HIGH)
        GPIO.output(frf, GPIO.LOW)
        GPIO.output(blf, GPIO.HIGH)
        GPIO.output(brf, GPIO.LOW)
        GPIO.output(flb, GPIO.LOW)
        GPIO.output(frb, GPIO.LOW)
        GPIO.output(blb, GPIO.LOW)
        GPIO.output(brb, GPIO.LOW)
    elif motion == "Back Left":
        GPIO.output(flf, GPIO.LOW)
        GPIO.output(frf, GPIO.LOW)
        GPIO.output(blf, GPIO.LOW)
        GPIO.output(brf, GPIO.LOW)
        GPIO.output(flb, GPIO.LOW)
        GPIO.output(frb, GPIO.HIGH)
        GPIO.output(blb, GPIO.LOW)
        GPIO.output(brb, GPIO.HIGH)
    elif motion == "Back Right":
        GPIO.output(flf, GPIO.LOW)
        GPIO.output(frf, GPIO.LOW)
        GPIO.output(blf, GPIO.LOW)
        GPIO.output(brf, GPIO.LOW)
        GPIO.output(flb, GPIO.HIGH)
        GPIO.output(frb, GPIO.LOW)
        GPIO.output(blb, GPIO.HIGH)
        GPIO.output(brb, GPIO.LOW)
    elif motion == "Left":
        GPIO.output(flf, GPIO.LOW)
        GPIO.output(frf, GPIO.HIGH)
        GPIO.output(blf, GPIO.LOW)
        GPIO.output(brf, GPIO.HIGH)
        GPIO.output(flb, GPIO.HIGH)
        GPIO.output(frb, GPIO.LOW)
        GPIO.output(blb, GPIO.HIGH)
        GPIO.output(brb, GPIO.LOW)
    elif motion == "Right":
        GPIO.output(flf, GPIO.HIGH)
        GPIO.output(frf, GPIO.LOW)
        GPIO.output(blf, GPIO.HIGH)
        GPIO.output(brf, GPIO.LOW)
        GPIO.output(flb, GPIO.LOW)
        GPIO.output(frb, GPIO.HIGH)
        GPIO.output(blb, GPIO.LOW)
        GPIO.output(brb, GPIO.HIGH)
    elif motion == "Stop":
        GPIO.output(flf, GPIO.LOW)
        GPIO.output(frf, GPIO.LOW)
        GPIO.output(blf, GPIO.LOW)
        GPIO.output(brf, GPIO.LOW)
        GPIO.output(flb, GPIO.LOW)
        GPIO.output(frb, GPIO.LOW)
        GPIO.output(blb, GPIO.LOW)
        GPIO.output(brb, GPIO.LOW)

xboxCont = XboxController.XboxController(
    controllerCallBack=None,
    joystickNo=0,
    deadzone=0.1,
    scale=1,
    invertYAxis=False
)

xboxCont.start()
print("xbox controller running")

while True:
    lx = xboxCont.LTHUMBX
    ly = xboxCont.LTHUMBY

    # BACKWARD
    if ly > 0.5 and -0.5 < lx < 0.5:
        motion = "Backward"
    # FORWARD
    elif ly < -0.5 and -0.5 < lx < 0.5:
        motion = "Forward"
    # FRONT RIGHT
    elif ly < -0.5 and lx > 0.5:
        motion = "Front Right"
    # FRONT LEFT
    elif ly < -0.5 and lx < -0.5:
        motion = "Front Left"
    # BACK RIGHT
    elif ly > 0.5 and lx > 0.5:
        motion = "Back Right"
    # BACK LEFT
    elif ly > 0.5 and lx < -0.5:
        motion = "Back Left"
    # RIGHT
    elif -0.5 < ly < 0.5 and lx > 0.5:
        motion = "Right"
    # LEFT
    elif -0.5 < ly < 0.5 and lx < -0.5:
        motion = "Left"
    # STOP
    else:
        motion = "Stop"

    run()
    print(motion)

xboxCont.stop()

import RPi.GPIO as GPIO
import time
from gpiozero import MotionSensor
from subprocess import call
import datetime as dt

# GPIO setup
channel1 = 21
pir = MotionSensor(4)
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel1, GPIO.OUT)

# motor on/off functions
def turn_on(pin):
    GPIO.output(pin, GPIO.LOW)

def turn_off(pin):
    GPIO.output(pin, GPIO.HIGH)

# MAIN
if __name__ == '__main__':
    # initially run for two minutes
    turn_on(channel1)
    time.sleep(120)
    turn_off(channel1)

    # set up variables
    activated_count = 0
    activated_time = int(dt.datetime.now().timestamp())

    # actual program
    while True:
        pir.wait_for_motion()
        print("motion")
        if (activated_count > 13):
            time.sleep(180)
            activated_count = 0
        else:
            if (int(dt.datetime.now().timestamp()) - activated_time < 25): # if activating within rapid time of each other, increase count
                activated_count += 1
            if (int(dt.datetime.now().timestamp()) - activated_time > 90): # if more than 90 seconds since last activation, reset counter
                activated_count = 0
            activated_time = int(dt.datetime.now().timestamp())
            call(["fswebcam", "-r", "1280x720", "/home/aaggarwal/"+dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+".jpg"])
            turn_on(channel1)
            time.sleep(15)
            turn_off(channel1)
            time.sleep(1)

    GPIO.cleanup()
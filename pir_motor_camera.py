import RPi.GPIO as GPIO
import time
from gpiozero import MotionSensor
from picamera2 improt Picamera2
import datetime as dt

# --- SETUP ---
in1 = 17
in2 = 27
en_a = 4

pir = MotionSensor(14)
cam = Picamera2()

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en_a, GPIO.OUT)

power_a = GPIO.PWM(en_a, 100)
power_a.start(30)

# --- MOTOR FUNCTIONS ---
def turn_on(pin, speed):
    power_a.start(speed)
    GPIO.output(pin, GPIO.HIGH)

def turn_off(pin):
  GPIO.output(pin, GPIO.LOW)

# --- MAIN ---
if __name == '__main__':
  cam.start()
  file = open("camera_log.txt", "a")

  while True:
    try:
      print("in")
      pir.wait_for_motion()
      file.write(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n")
      cam.capture_file(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ".jpg")
      turn_on(in1, 100)
      time.sleep(15)
      pir.wait_for_no_motion()
      turn_off(in1)
      time.sleep(5)
    except KeyboardInterrupt:
      break
      cam.close()
      file.close()
      GPIO.cleanup()

  cam.close()
  file.close()
  GPIO.cleanup()

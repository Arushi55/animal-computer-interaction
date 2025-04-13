import RPi.GPIO as GPIO
import time
from gpiozero import MotionSensor

inl = 17
in2 = 27
en_a = 4

pir = MotionSensor (14)

# GPIO setup
GPIO. setmode (GPIO. BCM)
﻿﻿﻿GPIO. setup(in1, GPIO.OUT)
﻿﻿﻿GP1O.setup(in2, GPIO.OUT)
GPIO. Setup(en_a, GPIO.OUT)

power_a = GPIO. PWM(en_a, 100)
power_a.start(30)

def turn_on(pin, speed): 
  print ("on!")
  power_a.start(speed)
  GPIO.output(pin, GPIO.HIGH)

def turn_off(pin):
  print("off!")
  GPIO.output(pin, GPIO.LOW)

if name _ == '_main__':
  for i in range(6): 
    try:
      print("in")
      pir.wait_for_motion()
      print("movement!")
      turn_on(in1, 100-i*10)
      time.sleep(5)
      turn_off(in1)
      time.sleep(5)
    except KeyboardInterrupt:
      GPIO.cleanup()

  GPIO.cleanup()

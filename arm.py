from __future__ import division
import time
import RPi.GPIO as GPIO
import sys
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

#IF THE SERVO HAS TO MOVE A FAR DISTANCE IT CRASHES PYTHON
#pwm.set_all_pwm(0,400)
#like these starts better
HAND_POS = 470
SHOULDER_POS = 330
WRIST_POS = 330
ELBOW_POS = 520
CAMERA_POS = 460
max_delta = 10

def hand(delta=max_delta):#range 300 - 465 inc (465 means hand is closed)
	global HAND_POS
	delta = max(-1*max_delta,min(max_delta, delta))
	new = min(470,max(300, HAND_POS+delta))
	pwm.set_pwm(15, 0, new)
	HAND_POS = new

def wrist(delta=max_delta):#range 100 - 500 inc
	global WRIST_POS
	#delta = max(-1*max_delta,min(max_delta, delta))
	new = min(560,max(110, WRIST_POS+delta))
	pwm.set_pwm(14, 0, new)
	WRIST_POS = new

def elbow(delta=max_delta): # 140 - 550 inc
	global ELBOW_POS
	delta = max(-1*max_delta,min(max_delta, delta))
	new = min(550,max(100, ELBOW_POS+delta))
	pwm.set_pwm(13, 0, new)
	ELBOW_POS = new

def shoulder(delta=max_delta): # 180 - 430 inc
	global SHOULDER_POS
	delta = max(-1*max_delta,min(max_delta, delta))
	new = min(540,max(180, SHOULDER_POS+delta))
	pwm.set_pwm(12, 0, new)
	SHOULDER_POS = new

def camera(delta=max_delta):
	global CAMERA_POS
	#delta = max(-1*max_delta,min(max_delta, delta))
	new = min(500,max(210, CAMERA_POS+delta))
	pwm.set_pwm(11, 0, new)
	CAMERA_POS = new

def set_start():
	pwm.set_pwm(15, 0, HAND_POS)
	pwm.set_pwm(14, 0, WRIST_POS)
	pwm.set_pwm(13, 0, ELBOW_POS)
	pwm.set_pwm(12, 0, SHOULDER_POS)
	pwm.set_pwm(11, 0, CAMERA_POS)
#set_start()
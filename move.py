import time
import math
import RPi.GPIO as GPIO

Motor_A_EN    = 4
Motor_B_EN    = 17

Motor_A_Pin1  = 14
Motor_A_Pin2  = 15
Motor_B_Pin1  = 27
Motor_B_Pin2  = 18

pwn_A = 0
pwm_B = 0

def motorStop():#Motor stops
	GPIO.output(Motor_A_Pin1, GPIO.LOW)
	GPIO.output(Motor_A_Pin2, GPIO.LOW)
	GPIO.output(Motor_B_Pin1, GPIO.LOW)
	GPIO.output(Motor_B_Pin2, GPIO.LOW)
	GPIO.output(Motor_A_EN, GPIO.LOW)
	GPIO.output(Motor_B_EN, GPIO.LOW)


def setup():#Motor initialization
	global pwm_A, pwm_B
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(Motor_A_EN, GPIO.OUT)
	GPIO.setup(Motor_B_EN, GPIO.OUT)
	GPIO.setup(Motor_A_Pin1, GPIO.OUT)
	GPIO.setup(Motor_A_Pin2, GPIO.OUT)
	GPIO.setup(Motor_B_Pin1, GPIO.OUT)
	GPIO.setup(Motor_B_Pin2, GPIO.OUT)

	motorStop()
	try:
		pwm_A = GPIO.PWM(Motor_A_EN, 1000)
		pwm_B = GPIO.PWM(Motor_B_EN, 1000)
	except:
		pass


def moveRight(percentSpeed):#Motor 2 positive and negative rotation
	if percentSpeed == 0: # stop
		GPIO.output(Motor_B_Pin1, GPIO.LOW)
		GPIO.output(Motor_B_Pin2, GPIO.LOW)
		GPIO.output(Motor_B_EN, GPIO.LOW)
	else:
		if percentSpeed < 0:
			GPIO.output(Motor_B_Pin1, GPIO.HIGH)
			GPIO.output(Motor_B_Pin2, GPIO.LOW)
			pwm_B.start(100)
			pwm_B.ChangeDutyCycle(abs(percentSpeed))
		elif percentSpeed > 0:
			GPIO.output(Motor_B_Pin1, GPIO.LOW)
			GPIO.output(Motor_B_Pin2, GPIO.HIGH)
			pwm_B.start(0)
			pwm_B.ChangeDutyCycle(abs(percentSpeed))


def moveLeft(percentSpeed):#Motor 1 positive and negative rotation
	if percentSpeed == 0: # stop
		GPIO.output(Motor_A_Pin1, GPIO.LOW)
		GPIO.output(Motor_A_Pin2, GPIO.LOW)
		GPIO.output(Motor_A_EN, GPIO.LOW)
	else:
		if percentSpeed < 0:
			GPIO.output(Motor_A_Pin1, GPIO.HIGH)
			GPIO.output(Motor_A_Pin2, GPIO.LOW)
			pwm_A.start(100)
			pwm_A.ChangeDutyCycle(abs(percentSpeed))
		elif percentSpeed > 0:
			GPIO.output(Motor_A_Pin1, GPIO.LOW)
			GPIO.output(Motor_A_Pin2, GPIO.HIGH)
			pwm_A.start(0)
			pwm_A.ChangeDutyCycle(abs(percentSpeed))


def moveTank(rightSpeed, leftSpeed):
	moveRight(rightSpeed)
	moveLeft(leftSpeed)

def moveArcade(throttle, turnSpeed):
	throttle *= -1
	turnSpeed *= -1
	leftPower = turnSpeed - throttle
	rightPower = turnSpeed + throttle
	moveTank(leftPower, rightPower)

def destroy():
	motorStop()
	GPIO.cleanup()             # Release resource

#simple functions to move in all 4 directions
def forwards(val=50):
	val = max(30,min(100, val))
	moveArcade(-1*val,0)
def backwards(val=50):
	val = max(30,min(100, val))
	moveArcade(val,0)
def turn_left(val=50):
	val = min(50, val)
	moveArcade(-1*val,-1*val)
def turn_right(val=50):
	val = min(50, val)
	moveArcade(-1*val,val)
def stop():
	moveArcade(0,0)

try:
	setup()
except KeyboardInterrupt:
	destroy()

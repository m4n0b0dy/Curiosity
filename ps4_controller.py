from pyPS4Controller.controller import Controller
import move
import arm
import LED
from time import sleep
import os

arm_sleep = .2

class MyController(Controller):

	def __init__(self, **kwargs):
		Controller.__init__(self, **kwargs)
		self.led = LED.LED()

	def on_up_down_arrow_release(self):
		move.stop()

	def on_left_right_arrow_release(self):
		move.stop()

	def on_up_arrow_press(self):
		move.forwards()

	def on_down_arrow_press(self):
		move.backwards()

	def on_right_arrow_press(self):
		move.turn_right()

	def on_left_arrow_press(self):
		move.turn_left()

	def on_L3_at_rest(self):
		move.stop()

	def on_L3_press(self):
		move.stop()

	def on_L3_release(self):
		move.stop()

	#camera movement
	
	#arm movement
	def on_x_press(self):
		arm.shoulder(-10)
		sleep(arm_sleep)

	def on_square_press(self):
		arm.shoulder(10)
		sleep(arm_sleep)

	def on_triangle_press(self):
		arm.elbow(-10)
		sleep(arm_sleep)
		
	def on_circle_press(self):
		arm.elbow(10)
		sleep(arm_sleep)

	def on_R2_press(self, val):
		mx = 32800
		val = int(30*(val+mx)/(2*mx))
		arm.wrist(val)

	def on_L2_press(self, val):
		mx = 32800
		val = int(30*(val+mx)/(2*mx))
		arm.wrist(-1*val)
	
	def on_R3_up(self, val):
		arm.hand(10)
		sleep(.01)

	def on_R3_right(self, val):
		arm.hand(10)
		sleep(.01)

	def on_R3_left(self, val):
		arm.hand(-10)
		sleep(.01)

	def on_R3_down(self, val):
		arm.hand(-10)
		sleep(.01)

	#camera
	def on_L3_right(self, val):
		arm.camera(10)
		sleep(.01)

	def on_L3_up(self, val):
		arm.camera(10)
		sleep(.01)

	def on_L3_left(self, val):
		arm.camera(-10)
		sleep(.01)

	def on_L3_down(self, val):
		arm.camera(-10)
		sleep(.01)
	
	def on_R1_press(self):
		self.led.change_color_routine()

	def on_L1_press(self):
		self.led.change_color()

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=True)
controller.listen(timeout=60)

import pyfirmata
import time

class board():
	def __init__(self,motor_pins,input_pins,usb_str):
		'''
		input_pins: tuple with pins corresponding to 3 motors
		usb_str: usb address (e.g.'/dev/tty.usbmodem411')
		'''
		self.board = pyfirmata.Arduino(usb_str)
		self.it = pyfirmata.util.Iterator(self.board)
		self.it.start()

		### Setup Pins for as many motors as defined ###:
		for m, pins in enumerate(motor_pins): 
			self.board.digital[pins[0]].mode = pyfirmata.PWM
			self.board.digital[pins[1]].mode = pyfirmata.PWM
		
		for a, pin in enumerate(input_pins):
			self.board.analog[pin].enable_reporting()

		self.n_motors = m+1
		self.motor_pins = motor_pins
		self.input_pins = input_pins


	#Drive straight
	def drive_straight(self):
		'''
		function to drive straight with motors 1, 2
		forward and backward depending on potentiometer 1 
		'''
		if self.input_speed > 0:
			self.board.digital[self.motor_pins[0][0]].write(self.input_speed)
			self.board.digital[self.motor_pins[1][1]].write(self.input_speed)

		else: 
			self.board.digital[self.motor_pins[0][1]].write(abs(self.input_speed))
			self.board.digital[self.motor_pins[1][0]].write(abs(self.input_speed))

	def read_speed(self):
		norm_spd = self.board.analog[self.input_pins[0]].read()
		print norm_spd
		if type(norm_spd)==float:
			self.input_speed = 2*(norm_spd - 0.5)
		else:
			self.input_speed = 0

	def spin(self):

		if self.input_speed > 0:
			self.board.digital[self.motor_pins[0][0]].write(self.input_speed)
			self.board.digital[self.motor_pins[1][0]].write(self.input_speed)
			self.board.digital[self.motor_pins[2][0]].write(self.input_speed)

		else: 
			self.board.digital[self.motor_pins[0][1]].write(abs(self.input_speed))
			self.board.digital[self.motor_pins[1][1]].write(abs(self.input_speed))
			self.board.digital[self.motor_pins[2][1]].write(abs(self.input_speed))

def run_motor():
	motor_pins = [[5,6],[9,10],[3,11]]
	input_pins = [0]
	usb_str = '/dev/tty.usbmodem411'
	b = board(motor_pins,input_pins,usb_str)
	while True:
		b.read_speed()
		#b.spin()
		b.drive_straight()
		time.sleep(0.1)




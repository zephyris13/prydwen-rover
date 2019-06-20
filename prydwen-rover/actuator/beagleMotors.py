import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM


__version__ = "0.1"


H_BRIDGE_MOTOR_FORWARD 	= 0
H_BRIDGE_MOTOR_REVERSE 	= 1

class hBridgeMotor:
	"""Class that two digital signals and a pwm signal to control an h-bridge"""

	def __init__(self, pwmChannel, fwdChannel, revChannel):
		# note the channels
		self.pwmChannel 	= pwmChannel
		self.fwdChannel		= fwdChannel
		self.revChannel 	= revChannel

		# setup the limitations
		self.minDuty 		= 85
		self.maxDuty		= 100

	def setupMinDuty(self, duty):
		"""Set the minimum allowed duty cycle for pwm"""
		self.minDuty 		= duty

	def setupMaxDuty(self, duty):
		"""Set the maximum allowed duty cycle for pwm"""
		self.maxDuty 		= duty

	def reset(self):
		"""Set the PWM to 0%, disable both h-bridge controls"""
		ret 	=  self.pwmDriver.setDutyCycle(0)
		ret 	|= self.fwdDriver.turnOff()
		ret 	|= self.revDriver.turnOff()

		return ret

	def spin(self, direction, duty):
		"""Set the PWM to the specified duty, and in the specified direction"""
		ret 	= 0

		# 0 - forward, 1 - reverse
		if (direction == H_BRIDGE_MOTOR_FORWARD):
			self.revDriver.turnOff()
			self.fwdDriver.turnOn()
		elif (direction == H_BRIDGE_MOTOR_REVERSE):
			self.fwdDriver.turnOff()
			self.revDriver.turnOn()
		else:
			ret 	= -1

		if (ret == 0):
			# check against the minimum and maximium pwm
			if duty < self.minDuty:
				duty 	= self.minDuty
			elif duty > self.maxDuty:
				duty 	= self.maxDuty

			# program the duty cycle
			ret 	= self.pwmDriver.setDutyCycle(duty)
		return ret

	def spinForward(self, duty):
		ret 	= self.spin(H_BRIDGE_MOTOR_FORWARD, duty)
		return ret

	def spinReverse(self, duty):
		ret 	= self.spin(H_BRIDGE_MOTOR_REVERSE, duty)
		return ret

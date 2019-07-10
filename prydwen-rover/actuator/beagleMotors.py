import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM


__version__ = "0.1"


H_BRIDGE_MOTOR_FORWARD 	= 0
H_BRIDGE_MOTOR_REVERSE 	= 1

class hBridgeMotor:
	"""Class that two digital signals and a pwm signal to control an h-bridge"""

	def __init__(self, fwdChannel, rwdChannel, pwmChannel):
		# note the channels
		self.fwdChannel		= fwdChannel
		self.rwdChannel 	= rwdChannel
    self.pwmChannel 	= pwmChannel

		# setup the limitations
		self.minDuty 		= 0
		self.maxDuty		= 100

    GPIO.setup(self.fwdChannel, GPIO.OUT)
    GPIO.setup(self.revChannel, GPIO.OUT)

    PWM.start(pwmChannel, 0)
    GPIO.output(self.fwdChannel, GPIO.LOW)
    GPIO.output(self.rwdChannel, GPIO.LOW)

	def setupMinDuty(self, duty):
		"""Set the minimum allowed duty cycle for pwm"""
		self.minDuty 		= duty

	def setupMaxDuty(self, duty):
		"""Set the maximum allowed duty cycle for pwm"""
		self.maxDuty 		= duty

	def reset(self):
		"""Set the PWM to 0%, disable both h-bridge controls"""
    
    PWM.set_duty_cycle(self.pwmChannel, 0)
    GPIO.output(self.fwdChannel, GPIO.LOW)
    GPIO.output(self.rwdChannel, GPIO.LOW)

		return 0

	def spin(self, direction, duty):
		"""Set the PWM to the specified duty, and in the specified direction"""

		# 0 - forward, 1 - reverse
		# if (direction == H_BRIDGE_MOTOR_FORWARD):
		# 	self.revDriver.turnOff()
		# 	self.fwdDriver.turnOn()
		# elif (direction == H_BRIDGE_MOTOR_REVERSE):
		# 	self.fwdDriver.turnOff()
		# 	self.revDriver.turnOn()
		# else:
		# 	return -1

			# check against the minimum and maximium pwm
    if duty < self.minDuty:
      duty 	= self.minDuty
    elif duty > self.maxDuty:
      duty 	= self.maxDuty

    # program the duty cycle
    PWM.set_duty_cycle(self.pwmChannel, duty)

		return 0

	def spinForward(self, duty):
		ret 	= self.spin(H_BRIDGE_MOTOR_FORWARD, duty)
		return ret

	def spinReverse(self, duty):
		ret 	= self.spin(H_BRIDGE_MOTOR_REVERSE, duty)
		return ret

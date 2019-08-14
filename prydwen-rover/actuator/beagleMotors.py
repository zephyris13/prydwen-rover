import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM


__version__ = "0.1"


class hBridgeMotor:
	"""Class that two digital signals and a pwm signal to control an h-bridge"""

	def __init__(self, fwdChannel, rwdChannel, pwmChannel):
		# note the channels
		self.fwdChannel = fwdChannel
		self.rwdChannel = rwdChannel
		self.pwmChannel 	= pwmChannel

		# setup the limitations
		self.minDuty 		= 0
		self.maxDuty		= 100

		GPIO.setup(self.fwdChannel, GPIO.OUT)
		GPIO.setup(self.rwdChannel, GPIO.OUT)

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

	def forward(self, duty):
		PWM.set_duty_cycle(self.pwmChannel, duty)
		GPIO.output(self.fwdChannel, GPIO.HIGH)
		GPIO.output(self.rwdChannel, GPIO.LOW)

	def reverse(self, duty):
		PWM.set_duty_cycle(self.pwmChannel, duty)
		GPIO.output(self.fwdChannel, GPIO.LOW)
		GPIO.output(self.rwdChannel, GPIO.HIGH)

	def spin(self, direction, dutyPercentage):
		"""Set the PWM to the specified duty, and in the specified direction"""

		# direction forward = 1 / stop = 0 / reverse = -1

		dutyRatio = (self.maxDuty - self.minDuty) / 100
		duty = dutyRatio * dutyPercentage

			# check against the minimum and maximium pwm
		if duty < self.minDuty:
			duty 	= self.minDuty
		elif duty > self.maxDuty:
			duty 	= self.maxDuty

		if direction == 1:
			self.forward(duty)
		elif direction == -1:
			self.reverse(duty)
		else direction == 0:
			self.reset

		return 0

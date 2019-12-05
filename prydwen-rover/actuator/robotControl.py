import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM

class robotControl:
  def __init__(self, leftFWDChannel, leftRWDChannel, rightFWDChannel, rightRWDChannel, leftPWMChannel, rightPWMChannel, minPWM, maxPWM):
    self.leftFWDChannel    = leftFWDChannel
    self.leftRWDChannel    = leftRWDChannel

    self.rightFWDChannel    = rightFWDChannel
    self.rightRWDChannel    = rightRWDChannel

    self.leftPWMChannel     = leftPWMChannel
    self.rightPWMChannel     = rightPWMChannel

    GPIO.setup(self.leftFWDChannel, GPIO.OUT)
		GPIO.setup(self.leftRWDChannel, GPIO.OUT)
    GPIO.setup(self.rightFWDChannel, GPIO.OUT)
		GPIO.setup(self.rightRWDChannel, GPIO.OUT)

		PWM.start(leftPWMChannel, 0)
    PWM.start(rightPWMChannel, 0)
    GPIO.output(self.leftFWDChannel, GPIO.LOW)
		GPIO.output(self.leftRWDChannel, GPIO.LOW)
		GPIO.output(self.rightFWDChannel, GPIO.LOW)
		GPIO.output(self.rightRWDChannel, GPIO.LOW)

    if minPWM:
      self.setupMinDuty(minPWM)
    else:
      self.setupMinDuty(0)
    
    if maxPWM:
      self.setupMaxDuty(maxPWM)
    else:
      self.setupMaxDuty(100)

  def setupMinDuty(self, duty):
		"""Set the minimum allowed duty cycle for pwm"""
		self.minDuty 		= duty

	def setupMaxDuty(self, duty):
		"""Set the maximum allowed duty cycle for pwm"""
		self.maxDuty 		= duty

  def calculateDuty(self, dutyPercentage):
    dutyRange = self.maxDuty - self.minDuty
  	dutyRatio = (dutyPercentage * dutyRange)
		duty = (dutyRatio / 100) + self.minDuty

    return duty

  def move(self, leftDirection, rightDirection, leftSpeedPercentage, rightSpeedPercentage):

    leftDuty = self.calculateDuty(leftSpeedPercentage)
    rightDuty = self.calculateDuty(rightSpeedPercentage)

    self.spin('left', leftDirection, leftDuty)
    self.spin('right', rightDirection, rightDuty)

	def spin(self, channel, direction, duty):
    if direction == -1:
      if channel == 'left':
        self.forward(self.leftPWMChannel, self.leftFWDChannel, self.leftRWDChannel, duty)
      if channel == 'right':
        self.forward(self.rightPWMChannel, self.rightFWDChannel, self.rightRWDChannel, duty)

    if direction == 1:
      if channel == 'left':
        self.reverse(self.leftPWMChannel, self.leftFWDChannel, self.leftRWDChannel, duty)
      if channel == 'right':
        self.reverse(self.rightPWMChannel, self.rightFWDChannel, self.rightRWDChannel, duty)

    if direction == 0:
      if channel == 'left':
        self.stop(self.leftPWMChannel, self.leftFWDChannel, self.leftRWDChannel)
      if channel == 'right':
        self.stop(self.rightPWMChannel, self.rightFWDChannel, self.rightRWDChannel)

  def forward(self, pwmChannel, fwdChannel, rwdChannel, duty):
    PWM.set_duty_cycle(pwmChannel, duty)
		GPIO.output(fwdChannel, GPIO.HIGH)
		GPIO.output(rwdChannel, GPIO.LOW)

  def reverse(self, pwmChannel, fwdChannel, rwdChannel, duty):
    PWM.set_duty_cycle(pwmChannel, duty)
		GPIO.output(fwdChannel, GPIO.LOW)
		GPIO.output(rwdChannel, GPIO.HIGH)
  
  def stop(self, pwmChannel, fwdChannel, rwdChannel):
    PWM.set_duty_cycle(pwmChannel, 0)
		GPIO.output(fwdChannel, GPIO.LOW)
		GPIO.output(rwdChannel, GPIO.LOW)
import beagleMotors

class robotControl:
  def __init__(self, leftFWDChannel, leftRWDChannel, rightFWDChannel, rightRWDChannel, leftPWMChannel, rightPWMChannel):
    self.leftFWDChannel    = leftFWDChannel
    self.leftRWDChannel    = leftRWDChannel

    self.rightFWDChannel    = rightFWDChannel
    self.rightRWDChannel    = rightRWDChannel

    self.leftPWMChannel     = leftPWMChannel
    self.rightPWMChannel     = rightPWMChannel


    # instantiate a Servo object for both pan and tilt
    self.leftMotors = beagleMotors.hBridgeMotor()
    self.rightMotors = beagleMotors.hBridgeMotor()

    # pan and tilt angles set directly based on input values
    def move(self, leftDirection, rightDirection, speedPercentage):
      return 0

    def turnLeft(self, speedPercentage):
      return 0

    def turnRight(self, speedPercentage):
      return 0

    def spinLeft(self, speedPercentage):
      return 0

    def spinRight(self, speedPercentage):
      return 0

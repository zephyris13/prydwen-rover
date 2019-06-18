import beagleMotors

class robotControl:
  def __init__(self, leftChannel, rightChannel, leftPWMChannel, rightPWMChannel):
    self.leftChannel    = leftChannel
    self.rightChannel    = rightChannel

    self.leftPWMChannel     = leftPWMChannel
    self.rightPWMChannel     = rightPWMChannel


    # instantiate a Servo object for both pan and tilt
    self.leftMotors = beagleMotors.hBridgeMotor()
    self.rightMotors = beagleMotors.hBridgeMotor()

    # pan and tilt angles set directly based on input values
    def move(self, leftDirection, rightDirection, leftSpeedPercentage, RightSpeedPercentage):
      return 0
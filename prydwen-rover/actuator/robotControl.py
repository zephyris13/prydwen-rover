import beagleMotors

class robotControl:
  def __init__(self, leftFWDChannel, leftRWDChannel, rightFWDChannel, rightRWDChannel, leftPWMChannel, rightPWMChannel, minPWM, maxPWM):
    self.leftFWDChannel    = leftFWDChannel
    self.leftRWDChannel    = leftRWDChannel

    self.rightFWDChannel    = rightFWDChannel
    self.rightRWDChannel    = rightRWDChannel

    self.leftPWMChannel     = leftPWMChannel
    self.rightPWMChannel     = rightPWMChannel

    # instantiate an hBridge object for both sides
    self.leftMotors = beagleMotors.hBridgeMotor(leftFWDChannel, leftRWDChannel, leftPWMChannel)
    self.rightMotors = beagleMotors.hBridgeMotor(rightFWDChannel, rightRWDChannel, rightPWMChannel)

    if minPWM:
      self.leftMotors.setupMinDuty(minPWM)
      self.rightMotors.setupMinDuty(minPWM)
    
    if maxPWM:
      self.leftMotors.setupMaxDuty(maxPWM)
      self.rightMotors.setupMaxDuty(maxPWM)

    # get values for hBridge sides
    def move(self, leftDirection, rightDirection, leftSpeedPercentage, RightSpeedPercentage):
      print "Moving (%d, %d), with Speed % (%d, %d)"%(int(leftDirection), int(rightDirection), int(leftSpeedPercentage), int(RightSpeedPercentage))
      return 0

    def spinLeft(self, speedPercentage):
      return 0

    def spinRight(self, speedPercentage):
      return 0

import PyLidar2
import json
import time
from threading import Thread

class lidarController:
  def __init__(self, mqttClient, mqttTopic, lidarPort):
    self.lidar = PyLidar2.YdLidarX4(lidarPort)

    if(self.lidar.Connect()):
      print self.lidar.GetDeviceInfo()

    self.thread = None
    self.mqttTopic = mqttTopic
    self.mqttClient = mqttClient
    self.data = dict()
    
    self.start()

  def getData(self):
    gen = self.lidar.StartScanning()
    data = dict(gen.next())
    self.lidar.StopScanning()
    self.data = json.dumps(data)

  def background_getData(self):
    time.sleep(2)
    while True:
      self.getData()
      self.mqttClient.publish(self.mqttTopic, self.data, 0, True)

  def start(self):
    if self.thread is None:
      self.thread = Thread(target=self.background_getData)
      self.thread.start()
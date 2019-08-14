import os
import sys
import json
import getopt
import paho.mqtt.client as mqtt

#import robotControl


# variables
configFile = 'config.json'

# find the directory of the script
dirName = os.path.dirname(os.path.abspath(__file__))

# read the command line arguments
try:
	opts, args = getopt.getopt(sys.argv[1:], "hc", ["help", "config="])
except getopt.GetoptError:
	printUsage()
	sys.exit(2)
for opt, arg, in opts:
	if opt in ("-h", "--help"):
		printUsage()
		sys.exit()
	elif opt in ("-c", "--config"):
		configFile = arg


### MAIN PROGRAM ###
def __main__():
	# read the config file
	configPath = '/'.join([dirName, configFile])
	with open(configPath) as f:
		try:
			config = json.load(f)
		except:
			print("ERROR: expecting JSON file at '%s'" % configPath)
			sys.exit()

	# setup mqtt
	mqttc = mqtt.Client()
	try:
		print("Initialised")
		#robot = robotControl.robotControl(config['leftFWDChannel'], config['leftRWDChannel'], config['rightFWDChannel'], config['rightRWDChannel'], config['leftPWMChannel'], config['rightPWMChannel'], config['minPWM'], config['maxPWM'])
	except:
		print("ERROR: config file must contain settings for 'leftFWDChannel', 'leftRWDChannel', 'rightFWDChannel', 'rightRWDChannel', 'leftPWMChannel', and 'rightPWMChannel'")
		sys.exit(2)

	# define the mqtt callbacks
	# when connection is made
	def on_connect(client, userdata, flags, rc):
		print("Connection result: " + str(rc))
		# subscribe to topic specified by config file
		mqttc.subscribe(config['topicA'], 0)

	def on_message(client, userdata, msg):
		if msg.payload:
			print(msg.topic + ":: payload is " + str(msg.payload))
			handleMessage(msg.topic, msg.payload)

	def on_subscribe(client, userdata, mid, granted_qos):
		print("Subscribed: " + str(mid) + " " + str(granted_qos))

	def on_disconnect(client, userdata, rc):
		print("Disconnected from Server")
	# end of mqtt callbacks

	# other functions
	def handleMessage(topic, payload):
		if topic == config['topicA']:
			data = payload.split()
			if len(data) == 4:
				# Left, Right, Left%, Right%
				print(f"Received directions {int(data[0])}, {int(data[1])}, with speed {int(data[2])}%, {int(data[3])}%")
				#print("Received directions (%d, %d), with Speed % (%d, %d)"%(int(data[0]), int(data[1]), int(data[2]), int(data[3])))
				#robot.move(int(data[0]), int(data[1]), int(data[2]), int(data[3]))
			else:
				print("Invalid number of arguments received")

	# Assign event callbacks
	mqttc.on_message = on_message
	mqttc.on_connect = on_connect
	mqttc.on_subscribe = on_subscribe
	mqttc.on_disconnect = on_disconnect
	# Connect
	mqttc.connect(config['server'], config['port'], 60)

	# Continue the network loop
	mqttc.loop_forever()


if __name__ == '__main__':
	__main__()

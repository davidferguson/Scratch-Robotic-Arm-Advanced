#Python handler for Scratch-Robotic-Arm-Advanced by David Ferguson
# Run the Scratch project, then run this file as root.
# Enjoy!

#Import all the necessary libraries
import scratch, usb.core, usb.util, time

#Initialise any required global variables
currentCommand = [0,0,0]

#Setup the Robotic Arm
ArmConn = usb.core.find(idVendor=0x1267, idProduct=0x000)
if ArmConn is None:
	print "Could not find arm - please check the USB connection"
else:
	print "Connected to Robotic Arm"

#Connect to Scratch
s = scratch.Scratch()
print "Connected to Scratch"

#Define any functions here
#This function is used to send the command to the arm
def moveArm(cmd):
	global currentCommand
	currentCommand = cmd
	try:
		ArmConn.ctrl_transfer(0x40, 6, 0x100, 0, cmd, 3)
	except:
		print "Error moving robot arm. Stopping..."
		while True:
			time.sleep(0.1)
			try:
				ArmConn.ctrl_transfer(0x40, 6, 0x100, 0, [0,0,0], 3)
				break
			except:
				print "Error stopping robot arm. Trying again..."
				pass

def run():
	while True:
		currentBroadcast = s.receive()[1]
		if currentBroadcast == "grip stop":
			gripStop()
		elif currentBroadcast == "grip close":
			gripClose()
		elif currentBroadcast == "grip open":
			gripOpen()
		elif currentBroadcast == "wrist stop":
			wristStop()
		elif currentBroadcast == "wrist up":
			wristUp()
		elif currentBroadcast == "wrist down":
			wristDown()
		elif currentBroadcast == "elbow stop":
			elbowStop()
		elif currentBroadcast == "elbow up":
			elbowUp()
		elif currentBroadcast == "elbow down":
			elbowDown()
		elif currentBroadcast == "shoulder stop":
			shoulderStop()
		elif currentBroadcast == "shoulder up":
			shoulderUp()
		elif currentBroadcast == "shoulder down":
			shoulderDown()
		elif currentBroadcast == "base stop":
			baseStop()
		elif currentBroadcast == "base left":
			baseLeft()
		elif currentBroadcast == "base right":
			baseRight()
		elif currentBroadcast == "light on":
			lightOn()
		elif currentBroadcast "light off":
			lightOff()

#The functions below are for calculating the movement command for the arm
def gripStop():
	print "Adding grip stop"
	currentJoints = list("{0:08b}".format(currentCommand[0]))
	currentJoints[7] = "0"
	currentJoints[6] = "0"
	currentJoints = "".join(currentJoints)
	currentJoints = int(currentJoints, 2)
	moveArm( [currentJoints, currentCommand[1], currentCommand[2]] )

def gripClose():
	print "Adding grip close"
	currentJoints = list("{0:08b}".format(currentCommand[0]))
	currentJoints[7] = "1"
	currentJoints[6] = "0"
	currentJoints = "".join(currentJoints)
	currentJoints = int(currentJoints, 2)
	moveArm( [currentJoints, currentCommand[1], currentCommand[2]] )

def gripOpen():
	print "Adding grip open"
	currentJoints = list("{0:08b}".format(currentCommand[0]))
	currentJoints[7] = "0"
	currentJoints[6] = "1"
	currentJoints = "".join(currentJoints)
	currentJoints = int(currentJoints, 2)
	moveArm( [currentJoints, currentCommand[1], currentCommand[2]] )

def wristStop():
	print "Adding wrist stop"
	currentJoints = list("{0:08b}".format(currentCommand[0]))
	currentJoints[5] = "0"
	currentJoints[4] = "0"
	currentJoints = "".join(currentJoints)
	currentJoints = int(currentJoints, 2)
	moveArm( [currentJoints, currentCommand[1], currentCommand[2]] )

def wristUp():
	print "Adding wrist up"
	currentJoints = list("{0:08b}".format(currentCommand[0]))
	currentJoints[5] = "1"
	currentJoints[4] = "0"
	currentJoints = "".join(currentJoints)
	currentJoints = int(currentJoints, 2)
	moveArm( [currentJoints, currentCommand[1], currentCommand[2]] )

def wristDown():
	print "Adding wrist down"
	currentJoints = list("{0:08b}".format(currentCommand[0]))
	currentJoints[5] = "0"
	currentJoints[4] = "1"
	currentJoints = "".join(currentJoints)
	currentJoints = int(currentJoints, 2)
	moveArm( [currentJoints, currentCommand[1], currentCommand[2]] )

def elbowStop():
	print "Adding elbow stop"
	currentJoints = list("{0:08b}".format(currentCommand[0]))
	currentJoints[3] = "0"
	currentJoints[2] = "0"
	currentJoints = "".join(currentJoints)
	currentJoints = int(currentJoints, 2)
	moveArm( [currentJoints, currentCommand[1], currentCommand[2]] )

def elbowUp():
	print "Adding elbow up"
	currentJoints = list("{0:08b}".format(currentCommand[0]))
	currentJoints[3] = "1"
	currentJoints[2] = "0"
	currentJoints = "".join(currentJoints)
	currentJoints = int(currentJoints, 2)
	moveArm( [currentJoints, currentCommand[1], currentCommand[2]] )

def elbowDown():
	print "Adding elbow down"
	currentJoints = list("{0:08b}".format(currentCommand[0]))
	currentJoints[3] = "0"
	currentJoints[2] = "1"
	currentJoints = "".join(currentJoints)
	currentJoints = int(currentJoints, 2)
	moveArm( [currentJoints, currentCommand[1], currentCommand[2]] )

def shoulderStop():
	print "Adding shoulder stop"
	currentJoints = list("{0:08b}".format(currentCommand[0]))
	currentJoints[1] = "0"
	currentJoints[0] = "0"
	currentJoints = "".join(currentJoints)
	currentJoints = int(currentJoints, 2)
	moveArm( [currentJoints, currentCommand[1], currentCommand[2]] )

def shoulderUp():
	print "Adding shoulder up"
	currentJoints = list("{0:08b}".format(currentCommand[0]))
	currentJoints[1] = "1"
	currentJoints[0] = "0"
	currentJoints = "".join(currentJoints)
	currentJoints = int(currentJoints, 2)
	moveArm( [currentJoints, currentCommand[1], currentCommand[2]] )

def shoulderDown():
	print "Adding shoulder down"
	currentJoints = list("{0:08b}".format(currentCommand[0]))
	currentJoints[1] = "0"
	currentJoints[0] = "1"
	currentJoints = "".join(currentJoints)
	currentJoints = int(currentJoints, 2)
	moveArm( [currentJoints, currentCommand[1], currentCommand[2]] )

def baseStop():
	print "Adding base stop"
	moveArm( [currentCommand[0], 0, currentCommand[2]] )

def baseRight():
	print "Adding base right"
	moveArm( [currentCommand[0], 1, currentCommand[2]] )

def baseLeft():
	print "Adding base left"
	moveArm( [currentCommand[0], 2, currentCommand[2]] )

def lightOn():
	print "Adding light on"
	moveArm( [currentCommand[0], currentCommand[1], 1] )

def lightOff():
	print "Adding light off"
	moveArm( [currentCommand[0], currentCommand[1], 0] )

#Start the actual program here
run()
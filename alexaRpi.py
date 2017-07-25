#Import the Modules Required
import RPi.GPIO as GPIO
import time
from pubnub import Pubnub

# Initialize the Pubnub Keys 
g_pub_key = "pub-c-6a007978f-533c-4bf7-a6d3-4a7c13bf4d44"
g_sub_key = "sub-c-45cffcee-24e2-11e7-9093-0619f8945a4f"



def init():
	
	global pubnub
        pubnub = Pubnub(publish_key=g_pub_key,subscribe_key=g_sub_key)
	pubnub.subscribe(channels='alexaTrigger', callback=callback, error=callback, reconnect=reconnect, disconnect=disconnect)


def alexaControl(controlCommand):
	if(controlCommand.has_key("trigger")):
		if(controlCommand["trigger"] == "light" and controlCommand["status"] == 1):
			GPIO.setmode(GPIO.BCM)
                        GPIO.setup(2,GPIO.OUT)
                        GPIO.output(2,GPIO.LOW) 
			print "light on successfully"

		elif(controlCommand["trigger"] == "light" and controlCommand["status"] == 0):
			GPIO.setmode(GPIO.BCM)
                        GPIO.setup(2,GPIO.OUT)
                        GPIO.output(2,GPIO.HIGH) 
			print "light off"
	else:
		pass



def callback(message, channel):
	if(message.has_key("requester")):
		alexaControl(message)
	else:
		pass


def error(message):
    print("ERROR : " + str(message))


def reconnect(message):
    print("RECONNECTED")


def disconnect(message):
    print("DISCONNECTED")

if __name__ == '__main__':
	#Initialize the Script
	init()


from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities  import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities      import OutgoingAckProtocolEntity
import RPi.GPIO as GPIO


class EchoLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        #send receipt otherwise we keep receiving the same message over and over
	msg=messageProtocolEntity.getBody().lower()
        list=msg.split()
        print type(list)
        if True:
            receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(), 'read', messageProtocolEntity.getParticipant())
	    res="Welcome to your home assistant!\n\n Toggle your light by sending 'light on' to switch on the light\n and\n 'light off' to switch off the light\n\n Toggle the fan by sending 'Fan on' to switch on the fan \n and \n 'Fan off' to switch it off"
            if msg=="light on":
			GPIO.setmode(GPIO.BCM)
		        GPIO.setup(2,GPIO.OUT)
			GPIO.output(2,GPIO.LOW)
			res="The light is turned ON"
	    if msg=="light off":
			GPIO.setmode(GPIO.BCM)
			GPIO.setup(2,GPIO.OUT)
			GPIO.output(2,GPIO.HIGH)
			res="The light is switched off"			
            if msg=="fan on":
			GPIO.setmode(GPIO.BCM)
			GPIO.setup(3,GPIO.OUT)
			GPIO.output(3,GPIO.LOW)
			res="The fan is switched on"
	    if msg=="fan off":
			GPIO.setmode(GPIO.BCM)
			GPIO.setup(3,GPIO.OUT)
			GPIO.output(3,GPIO.HIGH)
			res="The fan is turned off"

            outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                res,to = messageProtocolEntity.getFrom())

            self.toLower(receipt)
            self.toLower(outgoingMessageProtocolEntity)

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
        self.toLower(ack)

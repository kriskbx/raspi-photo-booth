#!/usr/bin/env python
import Image, time, os, picamera, sys, escpos.printer as printer, RPi.GPIO as GPIO

# Vars
LedPin = 11
ButtonPin = 12
BeepPin = 13
Working = 0
BeepTime = 0.2
DisableBeep = False
BasePath = os.path.dirname(os.path.realpath(__file__))
ImageDirectory = 'images'
ImagePath = BasePath + '/' + ImageDirectory + '/'

# Hardware
def flashOn():
	ledOn()
	beepOn()
	time.sleep(1)
	beepOff()

def flashOff():
	ledOff()

def countdown():
	for i in range(1, 5):
		ledOn()
		beepOn()
		time.sleep(BeepTime)
		ledOff()
		beepOff()
		time.sleep(1-BeepTime)

def resizePhoto(photo):
	thumbnail = photo.replace('.jpg', '.thumbnail.jpg')
	try:
		im = Image.open(photo)
		im.thumbnail((380, 500), Image.ANTIALIAS)
		im.save(thumbnail, "JPEG")
		return thumbnail
	except IOError:
		print "cannot create thumbnail for '%s'" % photo
		return False

def printPhoto(image):
	Thermal = printer.File("/dev/usb/lp0")
	Thermal.image(image)
	Thermal.control('LF')
	Thermal.control('LF')
	Thermal.control('LF')
	Thermal.control('LF')
	Thermal.control('LF')
	Thermal.close()

def takePhoto():
	image = ImagePath + str(time.time()) + '.jpg'
	print image
	Camera = picamera.PiCamera()
	Camera.resolution = (3280, 2464)
	Camera.capture(image)
	Camera.close() 
	return image

def beepOn():
	global DisableBeep
	if DisableBeep == False:
		GPIO.output(BeepPin, GPIO.LOW)

def beepOff():
	GPIO.output(BeepPin, GPIO.HIGH)

def ledOn():
	GPIO.output(LedPin, GPIO.LOW)

def ledOff():
	GPIO.output(LedPin, GPIO.HIGH)

# Event Listener
def buttonPress(ev=None):
	global Working

	if Working == 0:
		Working = 1
		
		countdown()
		flashOn()

		image = resizePhoto(takePhoto())
		if image != False:
			printPhoto(image)

		flashOff()

		Working = 0
		pass
		
# Setup
def setup():
	if os.path.isdir(ImagePath) == False:
		os.mkdir(ImagePath, 0777)

	try:
		GPIO.cleanup()
	finally:
		pass

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(BeepPin, GPIO.OUT)
	GPIO.setup(LedPin, GPIO.OUT)
	GPIO.setup(ButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	ledOn()
	beepOn()
	time.sleep(0.1)
	ledOff()
	beepOff()

# Loop, wait for button press
def loop():
	GPIO.add_event_detect(ButtonPin, GPIO.FALLING, callback=buttonPress)
	while True:
		pass

# When running directly, make sure to cleanup GPIO
def destroy():
	ledOff()
	beepOff()
	GPIO.cleanup()

if __name__ == '__main__': 
	setup()
	try:
		loop()
	except Exception:
		destroy()
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while True:
	if GPIO.input(13) == GPIO.LOW:
		print "13 is LOW"
	else:
		print "13 is HIGH"
	#if GPIO.input(19) == GPIO.LOW:
	#	print "19 is LOW"
	#else:
	#	print "19 is HIGH"
	#if GPIO.input(20) == GPIO.LOW:
	#	print "20 is LOW"
	#else:
	#	print "20 is HIGH"
	time.sleep(0.1)

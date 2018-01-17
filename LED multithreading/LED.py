import RPi.GPIO as GPIO
import time
import threading
from wheel import wheel

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(19,	GPIO.OUT)
GPIO.setup(6,	GPIO.OUT)
GPIO.setup(19,	GPIO.LOW)
GPIO.setup(6,	GPIO.LOW)

try:
	wheel1 = wheel(19, 0, 1, "hi")
	wheel2 = wheel(6, 0, 0.3, "hi")

	threads = [] # Deze gebruik ik niet meer denk ik ???

	thread = threading.Thread(target = wheel1.rotate)
	threads.append(thread) # Deze gebruik ik niet meer denk ik ???

	thread2 = threading.Thread(target = wheel2.rotate)
	threads.append(thread2) # Deze gebruik ik niet meer denk ik ???

	thread.start()
	thread2.start()
	
	while(1):
		if not thread.is_alive():
			thread = threading.Thread(target = wheel1.rotate)
			thread.start()
		if not thread2.is_alive():
			thread2 = threading.Thread(target = wheel2.rotate)
			thread2.start()

except KeyboardInterrupt:
	GPIO.cleanup()
	print "Exiting, GPIO's cleaned up"
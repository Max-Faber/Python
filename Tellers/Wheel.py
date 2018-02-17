import RPi.GPIO as GPIO
import time
import threading

class Wheel():
	def __init__(self, output, input, wheelName, errorLED1, errorLED2):
		self.output = output
		self.input = input
		self.wheelName = wheelName
		self.errorLED1 = errorLED1
		self.errorLED2 = errorLED2
		self.maxRotations = 9

	def errorMode(self):
		print "Amount of required rotations is greater then the max amount of rotations (" + str(self.maxRotations) +  "), entering error mode now"
		while True:
			GPIO.output(self.errorLED1, GPIO.HIGH)
			GPIO.output(self.errorLED2, GPIO.HIGH)
			time.sleep(0.5)
			GPIO.output(self.errorLED1, GPIO.LOW)
			GPIO.output(self.errorLED2, GPIO.LOW)
			time.sleep(0.5)

	def rotate(self, rotations):
		if(rotations != self.maxRotations):
			GPIO.output(self.output, GPIO.HIGH)
			time.sleep(0.1)
			GPIO.output(self.output, GPIO.LOW)
			time.sleep(0.1)
		else:
			self.errorMode()

	def initZero(self):
		rotations = 0
		while self.checkZero() == False:
			self.rotate(rotations)
			rotations = rotations + 1
		self.state = 0

	def setWheel(self, nextNumber):
		rotations = 0
		while self.state != nextNumber:
			if self.state == 0 & self.checkZero() == False:
				self.initZero()
			elif self.state != 0 & self.checkZero() == True:
				self.state = 0
			self.rotate(rotations)
			rotations = rotations + 1
			self.state = self.getNextNumber(self.state)
			print "Rotating to " + str(nextNumber)

	def getNextNumber(self, number):
		if number == 9:
			number = 0
		else:
			number = number + 1
		return number

	def checkZero(self):
		if GPIO.input(self.input) == GPIO.LOW:
			return True
		else:
			return False
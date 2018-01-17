import RPi.GPIO as GPIO
import time
import threading

class Wheel():
	def __init__(self, output, input, wheelName):
		self.output = output
		self.input = input
		self.wheelName = wheelName

	def rotate(self):
		GPIO.output(self.output, GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(self.output, GPIO.LOW)
		time.sleep(0.1)

	def initZero(self):
		while GPIO.input(self.input) == GPIO.HIGH:
			self.rotate()
		self.state = 0

	def setWheel(self, nextNumber):
		while self.state != nextNumber:
			if self.state == 0 & self.checkZero() == False:
				self.initZero()
			elif self.state != 0 & self.checkZero() == True:
				self.state = 0
			self.rotate()
			self.state = self.getNextNumber(self.state)
			print "rotating to " + str(nextNumber)

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
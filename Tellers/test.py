import time
import sys
import numpy as np

def getOnes(number):
	if number < 0:
		number = number * -1
	if round(number % 10) >= 9.5 and round(number % 10) <= 10.0:
		return 0
	else:
		return int(round(number % 10))

def getTens(number):
	if number < 0:
		number = number * -1
	if round(number % 10) >= 9.5 and round(number % 10) <= 10.0:
		return int(round(number // 10)) + 1
	else:
		return int(round(number // 10))


for number in np.arange(0, 20.1, 0.01):
	print "getOnes({}): {}".format(number, getOnes(number))
	print "getTens({}): {}\n".format(number, getTens(number))
	time.sleep(0.02)
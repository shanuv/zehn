import RPi.GPIO as GPIO
import time
import sys
import tty
import termios
import os

def readchar():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd,termios.TCSADRAIN, old_settings)
	if ch == '0x03' :
		raise KeyboardInterrupt
	return ch

def readkey(getchar_fn=None):
	getchar = getchar_fn or readchar
	c1 = getchar()
	if ord(c1) != 0x1b:
		return c1
	c2 = getchar()
	if ord(c2) != 0x5b:
		return c1

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
#print "LED on"
try:
	while True:
		keyp = readkey()	
		if keyp == 'n' :
			GPIO.output(23, GPIO.HIGH)
			time.sleep(1)
			GPIO.output(23, GPIO.LOW)
		elif keyp == 'm' :
			GPIO.output(24, GPIO.HIGH)
			time.sleep(1)
			GPIO.output(24, GPIO.LOW)
		elif keyp == 'b' :
			GPIO.output(18, GPIO.HIGH)
			time.sleep(1)
			GPIO.output(18, GPIO.LOW)
		elif keyp == 'v' :
			GPIO.output(18,GPIO.HIGH)
			GPIO.output(23,GPIO.HIGH)
			GPIO.output(24,GPIO.HIGH)
			time.sleep(1)
			GPIO.output(18,GPIO.LOW)
			GPIO.output(23,GPIO.LOW)
			GPIO.output(24,GPIO.LOW)
		#elif keyp == 'w':
		#	os.system('mpg123 CarDoorInFront.mp3')
		#elif keyp == 'a':
		#	os.system('mpg123 CarToYourLeft.mp3')
		#elif keyp == 'd':
		#	os.system('mpg123 CarToYourRight.mp3')
		#elif keyp == 'u':
		#	os.system('mpg123 UnevenRoad.mp3')
		#elif keyp == 'p':
		#	os.system('mpg123 PedestrianInFront.mp3')
		#elif keyp == 'r':
		#	os.system('mpg123 TurnRight.mp3')
		#elif keyp == 'n':
		#	os.system('mpg123 Amp\ Prox\ Noise.mp3')
		elif ord(keyp) == 3:
			break
except KeyboardInterrupt:
	exit()

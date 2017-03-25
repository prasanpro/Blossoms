import os
import RPi.GPIO as GPIO
import time
import subprocess

threshold = 100
#Rasptrigger = 19
pulse_start = 0
pulse_end = 0
#Flower 1 module specification
TRIG1 = 2
ECHO1 = 3
MotorA1 = 4
MotorA2 = 17

#Flower 2 module specification
TRIG2 = 27
ECHO2 = 22
MotorB1 = 10
MotorB2 = 9

#Flower 3 module specification
TRIG3 = 11
ECHO3 = 5
MotorC1 = 6
MotorC2 = 13

#Flower 4 module specification
TRIG4 = 18
ECHO4 = 23
MotorD1 = 24
MotorD2 = 25

#Flower 5 module specification
TRIG5 = 12
ECHO5 = 16
MotorE1 = 20
MotorE2 = 21

GPIO.setmode(GPIO.BCM)
#Sensor 1 setup
GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
#GPIO.setup(#Rasptrigger, GPIO.OUT)
GPIO.setup(MotorA1, GPIO.OUT)
GPIO.setup(MotorA2, GPIO.OUT)

#Sensor 2 setup
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO2,GPIO.IN)
GPIO.setup(MotorB1, GPIO.OUT)
GPIO.setup(MotorB2, GPIO.OUT)

#Sensor 3 setup
GPIO.setup(TRIG3,GPIO.OUT)
GPIO.setup(ECHO3,GPIO.IN)
GPIO.setup(MotorC1, GPIO.OUT)
GPIO.setup(MotorC2, GPIO.OUT)

#Sensor 4 setup
GPIO.setup(TRIG4, GPIO.OUT)
GPIO.setup(ECHO4, GPIO.IN)
GPIO.setup(MotorD1, GPIO.OUT)
GPIO.setup(MotorD2, GPIO.OUT)

#Sensor 5 setup
GPIO.setup(TRIG5, GPIO.OUT)
GPIO.setup(ECHO5, GPIO.IN)
GPIO.setup(MotorE1, GPIO.OUT)
GPIO.setup(MotorE2, GPIO.OUT)
print "Distance Measurement In Progress"

def sonar(trigger, echo):
	global pulse_start,pulse_end
	GPIO.output(trigger, False)
	#print "Waiting For Sensor To Settle"
	time.sleep(0.3)
	
	GPIO.output(trigger, True)
	time.sleep(0.00001)
	GPIO.output(trigger, False)
	
	while GPIO.input(echo)==0:
	  pulse_start = time.time()
	
	while GPIO.input(echo)==1:
	  pulse_end = time.time()
	
	pulse_duration = pulse_end - pulse_start
	
	distance = pulse_duration * 17150
	
	distance = round(distance, 2)
	
	return distance

while True:
	distance1 = sonar(TRIG1, ECHO1)
#	print "Distance1:",distance1,"cm"
	distance2 = sonar(TRIG2, ECHO2)
#	print "Distance2:",distance2,"cm"
	distance3 = sonar(TRIG3, ECHO3)
#	print "Distance3:",distance3,"cm"
	distance4 = sonar(TRIG4, ECHO4)
#	print "Distance4:", distance4,"cm"
	distance5 = sonar(TRIG5, ECHO5)
#	print "Distance5:", distance5,"cm"

	if (distance1 < threshold):
		subprocess.Popen('omxplayer TEdx1.mp3',shell=True)
#		GPIO.output(#Rasptrigger, True)
		GPIO.output(MotorA1, True)
		GPIO.output(MotorA2, False)
		time.sleep(4)
#		GPIO.output(#Rasptrigger, False)
		GPIO.output(MotorA1, False)
		GPIO.output(MotorA2, True)
		time.sleep(4)
		os.system('killall omxplayer.bin')
	if (distance2 < threshold):
		subprocess.Popen('omxplayer Flute_modified.mp3',shell=True)
#		GPIO.output(#Rasptrigger, True)
		GPIO.output(MotorB1, True)
		GPIO.output(MotorB2, False)
		time.sleep(4)
#		GPIO.output(#Rasptrigger, False)
		GPIO.output(MotorB1, False)
		GPIO.output(MotorB2, True)
		time.sleep(4)
		os.system('killall omxplayer.bin')
#	if ((distance1 < 100) and (distance2 < 100)):
#		suprocess.Popen('omxplayer Acoustic_modified.mp3', shell=True)
			

	if (distance3 < threshold):
		subprocess.Popen('omxplayer Harp_modified.mp3',shell=True)
#		GPIO.output(#Rasptrigger, True)
		GPIO.output(MotorC1, True)
		GPIO.output(MotorC2, False)
		time.sleep(4)
#		GPIO.output(#Rasptrigger, False)
		GPIO.output(MotorC1, False)
		GPIO.output(MotorC2, True)
		time.sleep(4)
		os.system('killall omxplayer.bin')
	if (distance4 < threshold):
		subprocess.Popen('omxplayer Acoustic_modified.mp3', shell=True)
#		GPIO.output(#Rasptrigger, True)
		GPIO.output(MotorD1, True)
		GPIO.output(MotorD2, False)
		time.sleep(4)
#		GPIO.output(#Rasptrigger, False)
		GPIO.output(MotorD1, False)
		GPIO.output(MotorD2, True)
		time.sleep(4)
		os.system('killall omxplayer.bin')
	if (distance5 < threshold):
		subprocess.Popen('omxplayer Romantic_modified.mp3', shell=True)
#		GPIO.output(#Rasptrigger, True)
		GPIO.output(MotorE1, True)
		GPIO.output(MotorE2, False)
		time.sleep(4)
		GPIO.output(MotorE1, False)
		GPIO.output(MotorE2, True)
#		GPIO.output(#Rasptrigger, False)
		time.sleep(4)
		os.system('killall omxplayer.bin')
	
	else:
#		GPIO.output(#Rasptrigger, False)
		GPIO.output(MotorA1, False)
		GPIO.output(MotorA2, False)
		GPIO.output(MotorB1, False)
		GPIO.output(MotorB2, False)
		GPIO.output(MotorC1, False)
		GPIO.output(MotorC2, False)
		GPIO.output(MotorD1, False)
		GPIO.output(MotorD2, False)
		GPIO.output(MotorE1, False)
		GPIO.output(MotorE2, False)
		time.sleep(0.1)


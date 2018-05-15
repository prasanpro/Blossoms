import os
import RPi.GPIO as GPIO
import time
import subprocess
GPIO.setmode(GPIO.BCM)

RaspTrigger1 = 3
RaspTrigger2 = 22
RaspTrigger3 = 5
RaspTrigger4 = 16
RaspTrigger5 = 23

GPIO.setup(RaspTrigger1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RaspTrigger2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RaspTrigger3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RaspTrigger4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RaspTrigger5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def my_callback(channel):
	print "Got the signal1"
	subprocess.Popen('omxplayer 1.mp3',shell=True)
#	time.sleep(0.5)
#	os.system('killall omxplayer')
#	os.system('killall omxplayer.bin')

def my_callback2(channel):
	subprocess.Popen('omxplayer 2.mp3',shell=True)
#	print "Got the signal2"
#	time.sleep(2)
#	subprocess.call('killall -s 9 omxplayer')
#	os.system('killall omxplayer.bin')

def my_callback3(channel):
#	print "Got the signal 3"
	subprocess.Popen('omxplayer 3.mp3',shell=True)
#	os.system('killall omxplayer.bin')

def my_callback4(channel):
#	print "Got the signal4"
	subprocess.Popen('omxplayer 4.mp3',shell=True)
#	os.system('killall omxplayer.bin')

def my_callback5(channel):
#	print "Got the signal5"
	subprocess.Popen('omxplayer 5.mp3',shell=True)
#	os.system('killall omxplayer.bin')

def main():
	GPIO.add_event_detect(3, GPIO.RISING, callback=my_callback)  
	GPIO.add_event_detect(22, GPIO.RISING, callback=my_callback2)
	GPIO.add_event_detect(5, GPIO.RISING, callback=my_callback3)
	GPIO.add_event_detect(16, GPIO.RISING, callback=my_callback4)
	GPIO.add_event_detect(23, GPIO.RISING, callback=my_callback5)


	try:
		for i in range(1,60):
			print 'hello',i
			time.sleep(1)
		os.system("sudo reboot")

	except KeyboardInterrupt:
		GPIO.cleanup()

	GPIO.cleanup()

if __name__ == "__main__":
    main()

from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils # recognition function easy
import time

defaultSpeed = 50
windowCenter = 320
centerBuffer = 30
pwmBound = float(50)
cameraBound = float(320)
kp = pwmBound / cameraBound
leftBound = int(windowCenter - centerBuffer)
rightBound = int(windowCenter + centerBuffer)
error = 0
ballPixel = 0
vs = VideoStream(src=0).start()


#Pin definitions
rightFwd = 7
rightRev = 11
leftFwd = 13
leftRev = 15

hue = 77
sat = 77
val = 77
hue2 = 89
sat2 = 255
val2 = 255


time.sleep(0.1)
#low light
#lower_yellow = np.array([20, 180, 40])
lower_yellow = np.array([77, 77, 77])
upper_yellow = np.array([89, 255, 255])

while True:
	# grab the current frame
	frame = vs.read()
 
	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if frame is None:
		break 
	lower_yellow = np.array([hue, sat, val])
	upper_yellow = np.array([hue2, sat2, val2])
	image = frame
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	
	mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	output = cv2.bitwise_and(image,image, mask = mask)	
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	center = None
	ballPixel = 0
	if len(cnts) > 0:
		c = max(cnts, key=cv2.contourArea)
		((x,y,), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
	
		
		if radius > 5:
			cv2.circle(output, (int(x), int(y)), int(radius), (0, 255, 255), 2)
			cv2.circle(output, center, 5, (0, 0, 255), -1)
			ballPixel = x
			#print output[y, x]
		else:
			ballPixel = 0
	
	cv2.imshow("image", output)
	#cv2.namedWindow("window")
	key = cv2.waitKey(1) & 0xFF
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
		
	#Proportional controller
	if ballPixel == 0 or ballPixel > 620:
		#filter out ballPixel > 600 because camera len has damage
		#print ("no ball")
		error = 0
	elif (ballPixel < leftBound) or (ballPixel > rightBound):
		error = windowCenter - ballPixel
		pwmOut = abs(error * kp)
		turnPwm = defaultSpeed - pwmOut
		if turnPwm < 0:
			turnPwm = 0
 
		#print (radius)
		if  ballPixel < (leftBound) and pwmOut > 4:

			rightMotorFwd = (pwmOut + defaultSpeed)
			leftMotorFwd = (defaultSpeed)
			print("TO left RIGHT SPEED {} LEFT SPEED  {}".format(rightMotorFwd, leftMotorFwd))	
			#leftMotorRev.ChangeDutyCycle(pwmOut)
			#rightMotorRev.ChangeDutyCycle(0)
		elif ballPixel > (rightBound) and pwmOut > 4:
			leftMotorFwd =(pwmOut + defaultSpeed)
			#rightMotorRev.ChangeDutyCycle(pwmOut)
			#leftMotorRev.ChangeDutyCycle(0)
			rightMotorFwd = (defaultSpeed)
			print("TO right RIGHT SPEED {} LEFT SPEED  {}".format(rightMotorFwd, leftMotorFwd))	


	else:	
		#print ("middle")
		if (radius < 40):
			rightMotorFwd = (defaultSpeed * (1 + 1/radius))	
			leftMotorFwd = (defaultSpeed * (1 + 1/radius))


cv2.destroyAllWindows()
exit()

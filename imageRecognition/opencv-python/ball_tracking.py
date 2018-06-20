# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils # recognition function easy
import time
 
# construct the argument parse and parse the arguments
# --video, é o caminho (opcional) para o nosso arquivo de vídeo de exemplo. 
# Se essa opção for fornecida, o OpenCV pegará um ponteiro para o arquivo de vídeo e lerá os quadros dele. 
# Caso contrário, se esse switch não for fornecido, o OpenCV tentará acessar nossa webcam.
# --buffer é o tamanho máximo de nosso deque, 
# que mantém uma lista das coordenadas (x, y) anteriores da bola que estamos rastreando. 
# Este deque nos permite desenhar a “rastro” da bola, detalhando seus locais passados.
# Uma fila menor levará a uma cauda mais curta, enquanto uma fila maior criará uma cauda mais longa
# (já que mais pontos estão sendo rastreados):
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
	help="max buffer size")
args = vars(ap.parse_args())

# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points
# definem os limites inferior e superior da cor verde no espaço de cores do HSV (que determinei usando o script range-detector na biblioteca de imutils). 
# Esses limites de cor nos permitirão detectar a bola verde em nosso arquivo de vídeo. 
greenLower = (77, 77, 77)
greenUpper = (89, 255, 255)
# inicializa o nosso deque de pts usando o tamanho máximo do buffer fornecido (que é padronizado para 64).
pts = deque(maxlen=args["buffer"])
 
# if a video path was not supplied, grab the reference
# to the webcam
# classe threaded VideoStream do imutils.video para eficiência.
if not args.get("video", False):
	vs = VideoStream(src=0).start()
 
# otherwise, grab a reference to the video file
else:
	vs = cv2.VideoCapture(args["video"])
 
# allow the camera or video file to warm up
time.sleep(2.0)

# keep looping
while True:
	# grab the current frame
	frame = vs.read()
 
	# handle the frame from VideoCapture or VideoStream
	frame = frame[1] if args.get("video", False) else frame
 
	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if frame is None:
		break
 
	# resize the frame, blur it, and convert it to the HSV
	# color space
	# pré-processam   um pouco o quadro . 
	# Primeiro, redimensionamos o quadro para ter uma largura de  600px . 
	# O downsizing do quadro nos permite processar o quadro mais rapidamente, levando a um aumento no FPS (já que temos menos dados de imagem para processar).
	# Em seguida, desfocaremos o quadro para reduzir o ruído de alta frequência e permitiremos que nos concentremos nos objetos estruturais dentro do quadro, 
	# como a bola. Por fim, converteremos o quadro   no espaço de cores HSV.
	frame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
 
	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
    	# find contours in the mask and initialize the current
	# (x, y) center of the ball
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if imutils.is_cv2() else cnts[1]
	center = None
 
	# only proceed if at least one contour was found
	if len(cnts) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
 
		# only proceed if the radius meets a minimum size
		if radius > 10:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			cv2.circle(frame, (int(x), int(y)), int(radius),
				(0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)
 
	# update the points queue
	pts.appendleft(center)
    # loop over the set of tracked points
	for i in range(1, len(pts)):
		# if either of the tracked points are None, ignore
		# them
		if pts[i - 1] is None or pts[i] is None:
			continue
 
		# otherwise, compute the thickness of the line and
		# draw the connecting lines
		thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
		cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
 
	# show the frame to our screen
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
 
# if we are not using a video file, stop the camera video stream
if not args.get("video", False):
	vs.stop()
 
# otherwise, release the camera
else:
	vs.release()
 
# close all windows
cv2.destroyAllWindows()
vs.stop()
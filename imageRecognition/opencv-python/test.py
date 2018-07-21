import cv2
import numpy as np
from imutils.video import VideoStream

vs = VideoStream(src=0).start()

img_rgb = cv2.imread('b.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('a.png', 0)
w, h = template.shape[::-1]


threshold = 0.6



while True:
    img_rgb =  vs.read()
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)


    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

        
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)


    cv2.imshow('Detected', img_rgb)

    key = cv2.waitKey(1) & 0xFF

        # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break

import cv2
from object_detector import *
import numpy as np



img = cv2.imread("Scale.jpg")

detector = HomogeneousBgDetector()

contours = detector.detect_objects(img)

for cnt in contours:

    rect = cv2.minAreaRect(cnt)
    (x, y), (w, h), angle = rect
    

    box = cv2.boxPoints(rect)
    box = np.int0(box)

    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
    cv2.polylines(img, [box], True, (255, 0, 0), 2)
    cv2.putText(img, "Length {}cm".format(round(w/15, 1)), (int(x-100), int(y-20)), cv2.FONT_HERSHEY_PLAIN, 2, (100,200,0), 2)
    cv2.putText(img, "Breadth {}cm".format(round(h/15, 1)), (int(x-100), int(y+15)), cv2.FONT_HERSHEY_PLAIN, 2, (100,200,0), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
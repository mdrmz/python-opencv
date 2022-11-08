import cv2
from matplotlib import pyplot as plt
import numpy as np

cap = cv2.VideoCapture(0)

while True :
    sucess,img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xff == ord('0'):
        break

import numpy as np
import cv2


def get_limits(color):

    c=np.uint8([[color]])
    hsvC = cv2.cvtColor(c,cv2.COLOR_BGR2HSV)

    lowerlimit = hsvC[0][0][0] - 10,100,100
    upperlimit = hsvC[0][0][0] + 10,255,255

    lowerlimit = np.array(lowerlimit)
    upperlimit = np.array(upperlimit)

    return lowerlimit, upperlimit
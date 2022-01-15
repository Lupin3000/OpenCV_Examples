#!/usr/bin/env python3

import argparse
from pathlib import Path
import sys
import cv2

# define argparse description/epilog
description = 'Image Face detection'
epilog = 'The author assumes no liability for any damage caused by use.'

# create argparse Object
parser = argparse.ArgumentParser(prog='./face_detection.py', description=description, epilog=epilog)

# set mandatory arguments
parser.add_argument('image', help="Image path", type=str)

# read arguments by user
args = parser.parse_args()

# set all variables
IMG_SRC = args.image
EYE_XML_SRC = '../src/haarcascades/haarcascade_eye.xml'

# verify files existing
image = Path(IMG_SRC)
if not image.is_file():
    sys.exit('image not found')

haarcascade = Path(EYE_XML_SRC)
if not haarcascade.is_file():
    sys.exit('haarcascade not found')

# process image
eye_cascade = cv2.CascadeClassifier(EYE_XML_SRC)
img = cv2.imread(cv2.samples.findFile(IMG_SRC))
gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
detect_eyes = eye_cascade.detectMultiScale(gray_scale, 1.3, 5)

for (x_pos, y_pos, width, height) in detect_eyes:
    cv2.rectangle(img, (x_pos, y_pos), (x_pos + width, y_pos + height), (10, 10, 255), 3)

# show result
cv2.imshow("Eye detection result", img)

# close
cv2.waitKey(0)
cv2.destroyAllWindows()

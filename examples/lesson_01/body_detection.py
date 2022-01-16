#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path

import cv2

# define argparse description/epilog
description = 'Full body detection with Python & OpenCV'
epilog = 'The author assumes no liability for any damage caused by use.'

# create argparse Object
parser = argparse.ArgumentParser(prog='./body_detection.py', description=description, epilog=epilog)

# set mandatory arguments
parser.add_argument('image', help="Image path", type=str)
parser.add_argument('body', help='Select identification type', choices=['full', 'upper', 'lower'])

# read arguments by user
args = parser.parse_args()

# set all variables
IMG_SRC = args.image
if args.body == 'full':
    BODY_XML_SRC = '../../src/haarcascades/haarcascade_fullbody.xml'
elif args.body == 'upper':
    BODY_XML_SRC = '../../src/haarcascades/haarcascade_upperbody.xml'
elif args.body == 'lower':
    BODY_XML_SRC = '../../src/haarcascades/haarcascade_lowerbody.xml'

# verify files existing
image = Path(IMG_SRC)
if not image.is_file():
    sys.exit('image not found')

haarcascade = Path(BODY_XML_SRC)
if not haarcascade.is_file():
    sys.exit('haarcascade not found')

# process image
body_cascade = cv2.CascadeClassifier(BODY_XML_SRC)
img = cv2.imread(cv2.samples.findFile(IMG_SRC))
gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
detect_body = body_cascade.detectMultiScale(gray_scale, 1.3, 5)

for (x_pos, y_pos, width, height) in detect_body:
    cv2.rectangle(img, (x_pos, y_pos), (x_pos + width, y_pos + height), (10, 10, 255), 3)

# show result
cv2.imshow("Body detection result", img)

# close
cv2.waitKey(0)
cv2.destroyAllWindows()

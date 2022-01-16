#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path

import cv2

# define argparse description/epilog
description = 'Cat detection with Python & OpenCV'
epilog = 'The author assumes no liability for any damage caused by use.'

# create argparse Object
parser = argparse.ArgumentParser(prog='./cat_detection.py', description=description, epilog=epilog)

# set mandatory arguments
parser.add_argument('image', help="Image path", type=str)
parser.add_argument('type', help='Select identification type', choices=['default', 'extended'])

# read arguments by user
args = parser.parse_args()

# set all variables
IMG_SRC = args.image
if args.type == 'default':
    CAT_XML_SRC = '../../src/haarcascades/haarcascade_frontalcatface.xml'
elif args.type == 'extended':
    CAT_XML_SRC = '../../src/haarcascades/haarcascade_frontalcatface_extended.xml'

# verify files existing
image = Path(IMG_SRC)
if not image.is_file():
    sys.exit('image not found')

haarcascade = Path(CAT_XML_SRC)
if not haarcascade.is_file():
    sys.exit('haarcascade not found')

# process image
cat_cascade = cv2.CascadeClassifier(CAT_XML_SRC)
img = cv2.imread(cv2.samples.findFile(IMG_SRC))
gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
detect_cat = cat_cascade.detectMultiScale(gray_scale, 1.3, 5)

for (x_pos, y_pos, width, height) in detect_cat:
    cv2.rectangle(img, (x_pos, y_pos), (x_pos + width, y_pos + height), (10, 10, 255), 3)

# show result
cv2.imshow("Cat detection result", img)

# close
cv2.waitKey(0)
cv2.destroyAllWindows()

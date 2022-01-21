#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path

import cv2

# define argparse description/epilog
description = 'Video object detection with Python & OpenCV'
epilog = 'The author assumes no liability for any damage caused by use.'

# create argparse Object
parser = argparse.ArgumentParser(prog='./video.py', description=description, epilog=epilog)

# set mandatory arguments
parser.add_argument('video', help="Video path", type=str)
parser.add_argument('haarcascade', help='Select identification type', type=str)

# read arguments by user
args = parser.parse_args()

# set all variables
VIDEO_SRC = args.video
HAARCASCADE_SRC = args.haarcascade

# verify files existing
video = Path(VIDEO_SRC)
if not video.is_file():
    sys.exit('video file not found')

haarcascade = Path(HAARCASCADE_SRC)
if not haarcascade.is_file():
    sys.exit('haarcascade file not found')
else:
    cascade = cv2.CascadeClassifier(HAARCASCADE_SRC)

# process video
video_file = cv2.VideoCapture(VIDEO_SRC)

if video_file.isOpened():
    cv2.namedWindow("Detection result", cv2.WINDOW_AUTOSIZE)

    print('Video stream opened. Press ESC or Ctrl + c to stop')

    while cv2.getWindowProperty("Detection result", 0) >= 0:
        ret, frame = video_file.read()

        # convert and detect
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detect_object = cascade.detectMultiScale(frame_gray, 1.3, 5)

        # draw rectangle
        for (x_pos, y_pos, width, height) in detect_object:
            cv2.rectangle(frame, (x_pos, y_pos), (x_pos + width, y_pos + height), (10, 10, 255), 3)

        # show frame
        cv2.imshow("Detection result", frame)

        # stop via ESC key
        keyCode = cv2.waitKey(30) & 0xFF
        if keyCode == 27 or not ret:
            break

    # close
    video_file.release()
    cv2.destroyAllWindows()
else:
    print('unable to open video stream')

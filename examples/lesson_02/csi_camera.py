#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path

import cv2


def gstreamer_pipeline(cap_width=1280,
                       cap_height=720,
                       disp_width=800,
                       disp_height=600,
                       framerate=21,
                       flip_method=2):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink" % (cap_width,
                                                       cap_height,
                                                       framerate,
                                                       flip_method,
                                                       disp_width,
                                                       disp_height)
    )


# define argparse description/epilog
description = 'CSI camera object detection with Python & OpenCV'
epilog = 'The author assumes no liability for any damage caused by use.'

# create argparse Object
parser = argparse.ArgumentParser(prog='./csi_camera.py', description=description, epilog=epilog)

# set mandatory arguments
parser.add_argument('haarcascade', help='Select identification type', type=str)

# read arguments by user
args = parser.parse_args()

# set all variables
HAARCASCADE_SRC = args.haarcascade

# verify files existing
haarcascade = Path(HAARCASCADE_SRC)
if not haarcascade.is_file():
    sys.exit('haarcascade file not found')
else:
    cascade = cv2.CascadeClassifier(HAARCASCADE_SRC)

# process csi camera
video_file = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)

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

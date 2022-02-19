#!/usr/bin/env python3

import cv2 as cv
import numpy as np


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


def apply_mask(face: np.array, mask: np.array) -> np.array:
    mask_h, mask_w, _ = mask.shape
    face_h, face_w, _ = face.shape

    # Resize the mask to fit on face
    factor = min(face_h / mask_h, face_w / mask_w)
    new_mask_w = int(factor * mask_w)
    new_mask_h = int(factor * mask_h)
    new_mask_shape = (new_mask_w, new_mask_h)
    resized_mask = cv.resize(mask, new_mask_shape)

    # Add mask to face - ensure mask is centered
    face_with_mask = face.copy()
    non_white_pixels = (resized_mask < 250).all(axis=2)
    off_h = int((face_h - new_mask_h) / 2)
    off_w = int((face_w - new_mask_w) / 2)
    face_with_mask[off_h: off_h+new_mask_h, off_w: off_w+new_mask_w][non_white_pixels] = resized_mask[non_white_pixels]

    return face_with_mask


def run():
    global y0, x0, x1, y1

    mask = cv.imread("../../src/mask/dog.png")
    cascade = cv.CascadeClassifier("../../src/haarcascades/haarcascade_frontalface_default.xml")

    cap = cv.VideoCapture(gstreamer_pipeline(), cv.CAP_GSTREAMER)

    if cap.isOpened():
        cv.namedWindow("Face Filter", cv.WINDOW_AUTOSIZE)

        while cv.getWindowProperty("Face Filter", 0) >= 0:
            ret, frame = cap.read()
            frame_h, frame_w, _ = frame.shape

            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            black_white = cv.equalizeHist(gray)

            rects = cascade.detectMultiScale(black_white,
                                             scaleFactor=1.3,
                                             minNeighbors=4,
                                             minSize=(30, 30),
                                             flags=cv.CASCADE_SCALE_IMAGE)

            for x, y, w, h in rects:
                # cv.rectangle(frame, (x, y), (x + w, y + h), (10, 10, 255), 3)
                y0, y1 = int(y - 0.25 * h), int(y + 0.75 * h)
                x0, x1 = x, x + w

            if x0 < 0 or y0 < 0 or x1 > frame_w or y1 > frame_h:
                continue

            frame[y0: y1, x0: x1] = apply_mask(frame[y0: y1, x0: x1], mask)

            cv.imshow("Face Filter", frame)

            key_code = cv.waitKey(30) & 0xFF
            if key_code == 27 or not ret:
                break

        cap.release()
        cv.destroyAllWindows()
    else:
        print('unable to open capture stream from CSI camera')


if __name__ == '__main__':
    run()

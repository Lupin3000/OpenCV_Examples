#!/usr/bin/env python3

import cv2
from flask import Flask, Response, render_template

app = Flask(__name__, template_folder='templates')
cascade = cv2.CascadeClassifier('../../src/haarcascades/haarcascade_frontalface_default.xml')


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
        "video/x-raw, format=(string)BGR ! "
        "appsink wait-on-eos=false max-buffers=1 drop=True " % (cap_width,
                                                                cap_height,
                                                                framerate,
                                                                flip_method,
                                                                disp_width,
                                                                disp_height)
    )


def encode_frame():
    video_file = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)

    while video_file.isOpened():
        ret, frame = video_file.read()

        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_gray = cv2.equalizeHist(frame_gray)

        detect_object = cascade.detectMultiScale(frame_gray, 1.3, 5)
        for (x_pos, y_pos, width, height) in detect_object:
            cv2.rectangle(frame, (x_pos, y_pos), (x_pos + width, y_pos + height), (10, 10, 255), 3)

        key, jpeg = cv2.imencode('.jpg', frame)
        frame = jpeg.tobytes()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/stream')
def stream():
    return Response(encode_frame(), mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == '__main__':
    app.run("0.0.0.0", port=8000)

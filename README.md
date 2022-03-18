# Python OpenCV examples for different modules

**:point_right: Very Important :point_left:**

You can adapt, improve and use the code for your projects as you wish. The author of this repository take no responsibility for your use or misuse or any damage on your devices!

## Instruction

### Download repository

```shell
# clone repository
$ git clone https://github.com/Lupin3000/OpenCV_Examples.git

# change directory
$ cd ~/Projects/OpenCV_Examples/
```

### Prepare environment

```shell
# create virtualenv
$ python3 -m venv

# activate virtualenv
$ source venv/bin/activate

# check python path (optional)
(venv) $ which python

# check pip path (optional)
(venv) $ which pip

# install dependencies
(venv) $ pip install -r requirements.txt
```

### Run examples

Values for `--input` are standard camera for macOS/Linux `[0-9]`, `csi` or `absolute/relative path` to video file. Values for `--example` are:

- face-[1-8] _simple face detection_
- other-[1-8] _advanced item detection_
- aug-1 _augmented reality examples_

```shell
# show help
(venv) $ python RunExamples.py -h

# run face detection on default video 0 source
(venv) $ python RunExamples.py -e face-3

# run face detection on video source
(venv) $ python RunExamples.py -i src/video/Woman.mp4 -e face-6

# run other detection example from csi camera
(venv) $ python RunExamples.py -e other-5 -i csi

# run color detection on video source
(venv) $ python RunExamples.py -i src/video/Fish.mp4 -e other-1
```

## Examples

### --input=face-n

1. [Haarcascade] face detection
2. [Haarcascade] face, eye and smile detection
3. [Dlib] CNN face detection
4. [Dlib] HOG face detection
5. [Dlib] face mesh detection
6. [Mediapipe] face mesh detection
7. [CVZone] face detection
8. [CVZone] face mesh detection

### --input=other-n

1. [OpenCV] color detection
2. [Bleedfacedetector] face emotion detection
3. [Mediapipe] hand mesh detection
4. [Mediapipe] finger count detection
5. [Deepface] human detection
6. [Haarcascade] car detection
7. [CVZone] hand tracking
8. [CVZone] pose estimation

### --input=aug-n

1. [Haarcascade] face filter

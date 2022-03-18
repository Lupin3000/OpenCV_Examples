# Python OpenCV examples for different modules

**:point_right: Very Important :point_left:**

You can adapt, improve and use the code for your projects as you wish. The author of this repository take no responsibility for your use or misuse or any damage on your devices!

## Download repository

```shell
# clone repository
$ git clone https://github.com/Lupin3000/OpenCV_Examples.git

# change directory
$ cd ~/Projects/OpenCV_Examples/
```

## Prepare environment

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

## Run examples

Values for `--input` are standard camera for macOS/Linux `[0-9]`, `csi` or `absolute/relative path` to video file. Values for `--example` are:

- face-[1-8] _simple face detection_
- other-[1-7] _advanced item detection_
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

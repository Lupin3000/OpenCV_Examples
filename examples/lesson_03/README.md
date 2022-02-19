# Lesson 03

> You will find that the results vary greatly. Also use your own images for the respective haarcascade files.

## Usage

**Install Flask**

```shell
# update
$ sudo apt update

# install python3 pip
$ sudo apt install -y python3-pip

# install flask
$ pip3 install flask
```

**Browser CSI Camera Detection**

```shell
# change into directory
$ cd OpenCV_Examples/examples/lesson_03/

# run web application
$ python3 flask_csi_camera.py

# open link from terminal
```

### Note

The example implementation is not thread save! Please close first the browser, wait for terminal output like:

```
GST_ARGUS: Cleaning up
CONSUMER: Done Success
GST_ARGUS: Done Success
```

After stop python application. May you need to reboot your device.

[Go Back](../../README.md)


import cv2 as cv
import numpy as np


class ShowPlayer:

    def __init__(self, title='stream window', cap=0):
        self.window_title = str(title)
        self.cap_source = cap
        self.split_screen = False
        self.frame_in = None
        self.frame_out = None

    def _detect(self):
        pass

    def _write_output_text(self):
        font = cv.FONT_HERSHEY_SIMPLEX
        line_type = cv.LINE_AA

        cv.putText(self.frame_out, self.window_title, (50, 50), font, 0.75, (0, 0, 0), 1, line_type)

    def __show_result(self):
        if self.split_screen:
            cv.imshow(self.window_title, np.hstack([self.frame_in, self.frame_out]))
        else:
            cv.imshow(self.window_title, self.frame_out)

    @staticmethod
    def gstreamer_pipeline(self, cap_width=1280, cap_height=720, disp_width=800,
                           disp_height=600, framerate=21, flip_method=2):
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

    def start(self):
        if self.cap_source == 'csi':
            cap = cv.VideoCapture(ShowPlayer.gstreamer_pipeline(self), cv.CAP_GSTREAMER)
        else:
            cap = cv.VideoCapture(self.cap_source)

        if not cap.isOpened():
            print('Cannot open {}'.format(self.cap_source))
            exit()
        else:
            print('Open video stream window... Press key "q" to stop')
            cv.namedWindow(self.window_title, cv.WINDOW_AUTOSIZE)

            while cv.getWindowProperty(self.window_title, 0) >= 0:
                ret, self.frame_in = cap.read()

                self.frame_out = self.frame_in

                if not ret:
                    print('Do no more receive frames. Exiting ...')
                    break

                if cv.waitKey(1) & 0xFF == ord('q'):
                    print('Key q press detected. Exiting ...')
                    break

                self._detect()
                self._write_output_text()
                self.__show_result()

            cap.release()
            cv.destroyAllWindows()

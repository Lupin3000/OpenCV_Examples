
import cv2 as cv

from src.player.window import ShowPlayer


class CarDetection(ShowPlayer):

    def write_output_text(self, text=''):
        font = cv.FONT_HERSHEY_SIMPLEX
        line_type = cv.LINE_AA

        cv.putText(self.frame_out, text, (50, 75), font, 0.75, (0, 0, 0), 1, line_type)

    def _detect(self):
        default_xml_file = 'car.xml'
        default_xml_path = 'src/models/haarcascade/'

        car_cascade = cv.CascadeClassifier(default_xml_path + default_xml_file)

        frame_gray = cv.cvtColor(self.frame_in, cv.COLOR_BGR2GRAY)

        cars = car_cascade.detectMultiScale(frame_gray, 1.1, 1)

        for (x, y, w, h) in cars:
            cv.rectangle(self.frame_out, (x, y), (x + w, y + h), (0, 0, 255), 2)


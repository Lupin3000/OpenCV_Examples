
import cv2 as cv

from src.player.window import ShowPlayer


class HaarcascadeMultiple(ShowPlayer):

    def _detect(self):
        default_xml_path = 'venv/lib/python3.7/site-packages/cv2/data/'
        face_xml_file = 'haarcascade_frontalface_default.xml'
        eye_xml_file = 'haarcascade_eye.xml'
        smile_xml_file = 'haarcascade_smile.xml'

        face_cascade = cv.CascadeClassifier(default_xml_path + face_xml_file)
        eye_cascade = cv.CascadeClassifier(default_xml_path + eye_xml_file)
        smile_cascade = cv.CascadeClassifier(default_xml_path + smile_xml_file)

        frame_gray = cv.cvtColor(self.frame_in, cv.COLOR_BGR2GRAY)
        black_white = cv.equalizeHist(frame_gray)

        faces = face_cascade.detectMultiScale(black_white,
                                              scaleFactor=1.3,
                                              minNeighbors=4,
                                              minSize=(30, 30),
                                              flags=cv.CASCADE_SCALE_IMAGE)

        for (x, y, w, h) in faces:
            cv.rectangle(self.frame_out, (x, y), (x + w, y + h), (0, 0, 255), 2)

            roi_gray = frame_gray[y:y + h, x:x + w]
            roi_color = self.frame_in[y:y + h, x:x + w]

            smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)

            for (sx, sy, sw, sh) in smiles:
                cv.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (255, 0, 0), 2)

            eyes = eye_cascade.detectMultiScale(roi_gray, 1.8, 20)

            for (ex, ey, ew, eh) in eyes:
                cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

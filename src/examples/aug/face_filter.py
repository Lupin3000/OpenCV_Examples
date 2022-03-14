
import cv2 as cv

from src.player.window import ShowPlayer


class FaceFilter(ShowPlayer):

    def _detect(self):
        replacement_face = cv.imread('src/img/anonymous.png')
        default_xml_file = 'haarcascade_frontalface_default.xml'
        default_xml_path = 'venv/lib/python3.7/site-packages/cv2/data/'

        face_cascade = cv.CascadeClassifier(default_xml_path + default_xml_file)

        gray = cv.cvtColor(self.frame, cv.COLOR_BGR2GRAY)
        black_white = cv.equalizeHist(gray)

        faces = face_cascade.detectMultiScale(black_white,
                                              scaleFactor=1.3,
                                              minNeighbors=4,
                                              minSize=(30, 30),
                                              flags=cv.CASCADE_SCALE_IMAGE)

        for (x, y, w, h) in faces:
            replacement_face_copy = cv.resize(replacement_face, (w, h))
            self.frame[y:y + h, x:x + w] = replacement_face_copy

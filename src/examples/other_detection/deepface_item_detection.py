
import cv2 as cv
from deepface import DeepFace

from src.player.window import ShowPlayer


class Deepface(ShowPlayer):

    def write_output_text(self, text=''):
        font = cv.FONT_HERSHEY_SIMPLEX
        line_type = cv.LINE_AA

        cv.putText(self.frame, text, (50, 75), font, 0.75, (0, 0, 0), 1, line_type)

    def _detect(self):
        default_xml_file = 'haarcascade_frontalface_default.xml'
        default_xml_path = 'venv/lib/python3.7/site-packages/cv2/data/'

        face_cascade = cv.CascadeClassifier(default_xml_path + default_xml_file)

        frame_gray = cv.cvtColor(self.frame, cv.COLOR_BGR2GRAY)
        black_white = cv.equalizeHist(frame_gray)

        faces = face_cascade.detectMultiScale(black_white,
                                              scaleFactor=1.3,
                                              minNeighbors=4,
                                              minSize=(30, 30),
                                              flags=cv.CASCADE_SCALE_IMAGE)

        for (x, y, w, h) in faces:

            prediction = DeepFace.analyze(self.frame)

            emotion = prediction['dominant_emotion']
            race = prediction['dominant_race']
            age = prediction['age']
            gender = prediction['gender']

            self.write_output_text('Emotion: {} Race: {} Age: {} Gender: {}'.format(str(emotion), str(race), str(age), str(gender)))

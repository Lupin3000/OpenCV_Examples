
import cv2 as cv
import dlib
import numpy as np

from src.player.window import ShowPlayer


class DLIBFaceLandmark(ShowPlayer):

    def _detect(self):
        detector = dlib.get_frontal_face_detector()

        frame_gray = cv.cvtColor(src=self.frame_in, code=cv.COLOR_BGR2GRAY)

        predictor = dlib.shape_predictor('src/models/shape/shape_predictor_68_face_landmarks.dat')
        faces = detector(frame_gray)

        for face in faces:
            shape = predictor(frame_gray, face)
            shape_np = np.zeros((68, 2), dtype="int")
            for i in range(0, 68):
                shape_np[i] = (shape.part(i).x, shape.part(i).y)
            shape = shape_np

            for i, (x, y) in enumerate(shape):
                cv.circle(self.frame_out, (x, y), 1, (255, 255, 255), -1)


import cv2 as cv
import dlib

from src.player.window import ShowPlayer


class CnnFace(ShowPlayer):

    def _detect(self):
        detector = dlib.cnn_face_detection_model_v1("src/models/cnn/mmod_human_face_detector.dat")

        frame_gray = cv.cvtColor(src=self.frame_in, code=cv.COLOR_BGR2GRAY)

        faces = detector(frame_gray)

        for faceRect in faces:
            x1 = faceRect.rect.left()
            y1 = faceRect.rect.top()
            x2 = faceRect.rect.right()
            y2 = faceRect.rect.bottom()

            cv.rectangle(self.frame_out, pt1=(x1, y1), pt2=(x2, y2), color=(0, 0, 255), thickness=2)

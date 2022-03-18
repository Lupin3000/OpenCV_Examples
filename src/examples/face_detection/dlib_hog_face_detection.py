
import cv2 as cv
import dlib

from src.player.window import ShowPlayer


class HogFace(ShowPlayer):

    def _detect(self):
        detector = dlib.get_frontal_face_detector()

        frame_gray = cv.cvtColor(src=self.frame_in, code=cv.COLOR_BGR2GRAY)

        faces = detector(frame_gray)

        for faceRect in faces:
            x1 = faceRect.left()
            y1 = faceRect.top()
            x2 = faceRect.right()
            y2 = faceRect.bottom()

            cv.rectangle(self.frame_out, pt1=(x1, y1), pt2=(x2, y2), color=(0, 0, 255), thickness=2)


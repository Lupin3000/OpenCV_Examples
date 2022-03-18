
import cv2 as cv
from cvzone.FaceDetectionModule import FaceDetector

from src.player.window import ShowPlayer


class CVZFace(ShowPlayer):

    def _detect(self):
        detector = FaceDetector()
        img, boxes = detector.findFaces(self.frame_in)

        if boxes:
            center = boxes[0]["center"]
            cv.circle(self.frame_out, center, 5, (255, 0, 255), cv.FILLED)

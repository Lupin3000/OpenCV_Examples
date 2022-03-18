
import cv2 as cv
from cvzone.PoseModule import PoseDetector

from src.player.window import ShowPlayer


class CVZPoseEstimation(ShowPlayer):

    def _detect(self):
        detector = PoseDetector()
        img = detector.findPose(self.frame_in)
        lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False)

        if bboxInfo:
            center = bboxInfo["center"]
            cv.circle(img, center, 5, (255, 0, 255), cv.FILLED)

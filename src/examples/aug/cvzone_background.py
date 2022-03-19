
import cv2 as cv
from cvzone.SelfiSegmentationModule import SelfiSegmentation

from src.player.window import ShowPlayer


class CVZoneBackgroundFilter(ShowPlayer):

    def _detect(self):
        segmentor = SelfiSegmentation()
        bg_img = cv.imread("src/img/forest.jpg")

        self.frame_out = segmentor.removeBG(self.frame_in, bg_img, threshold=0.8)


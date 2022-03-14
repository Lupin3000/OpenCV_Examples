
import cv2 as cv
import numpy as np

from src.player.window import ShowPlayer


class Color(ShowPlayer):

    def _detect(self):
        hsv = cv.cvtColor(self.frame, cv.COLOR_BGR2HSV)

        red_lower = np.array([136, 87, 111], np.uint8)
        red_upper = np.array([180, 255, 255], np.uint8)

        green_lower = np.array([25, 52, 72], np.uint8)
        green_upper = np.array([102, 255, 255], np.uint8)

        blue_lower = np.array([94, 80, 2], np.uint8)
        blue_upper = np.array([120, 255, 255], np.uint8)

        red_mask = cv.inRange(hsv, red_lower, red_upper)
        green_mask = cv.inRange(hsv, green_lower, green_upper)
        blue_mask = cv.inRange(hsv, blue_lower, blue_upper)

        transform = np.ones((5, 5), "uint8")

        red_mask = cv.dilate(red_mask, transform)
        res_red = cv.bitwise_and(self.frame, self.frame, mask=red_mask)

        green_mask = cv.dilate(green_mask, transform)
        res_green = cv.bitwise_and(self.frame, self.frame, mask=green_mask)

        blue_mask = cv.dilate(blue_mask, transform)
        res_blue = cv.bitwise_and(self.frame, self.frame, mask=blue_mask)

        contours, hierarchy = cv.findContours(red_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv.contourArea(contour)
            if area > 300:
                x, y, w, h = cv.boundingRect(contour)
                cv.rectangle(self.frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv.putText(self.frame, "Red", (x, y), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))

        contours, hierarchy = cv.findContours(green_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv.contourArea(contour)
            if area > 300:
                x, y, w, h = cv.boundingRect(contour)
                cv.rectangle(self.frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv.putText(self.frame, "Green", (x, y), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))

        contours, hierarchy = cv.findContours(blue_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv.contourArea(contour)
            if area > 300:
                x, y, w, h = cv.boundingRect(contour)
                cv.rectangle(self.frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv.putText(self.frame, "Blue", (x, y), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0))

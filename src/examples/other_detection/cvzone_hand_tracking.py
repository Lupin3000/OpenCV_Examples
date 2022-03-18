
from cvzone.HandTrackingModule import HandDetector

from src.player.window import ShowPlayer


class CVZHandTracking(ShowPlayer):

    def _detect(self):
        detector = HandDetector(detectionCon=0.8, maxHands=2)
        hands, img = detector.findHands(self.frame_in)

        if hands:
            hand1 = hands[0]
            lmList1 = hand1["lmList"]
            bbox1 = hand1["bbox"]
            centerPoint1 = hand1['center']
            handType1 = hand1["type"]
            fingers1 = detector.fingersUp(hand1)

            if len(hands) == 2:
                hand2 = hands[1]
                lmList2 = hand2["lmList"]
                bbox2 = hand2["bbox"]
                centerPoint2 = hand2['center']
                handType2 = hand2["type"]
                fingers2 = detector.fingersUp(hand2)

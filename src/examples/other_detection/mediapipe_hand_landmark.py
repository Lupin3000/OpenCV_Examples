
import mediapipe as mp
import cv2 as cv

from src.player.window import ShowPlayer


class HandLandmark(ShowPlayer):

    def _detect(self):
        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands(static_image_mode=False,
                               max_num_hands=2,
                               min_detection_confidence=0.5,
                               min_tracking_confidence=0.5)
        mp_draw = mp.solutions.drawing_utils
        img_rgb = cv.cvtColor(self.frame, cv.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = self.frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cv.circle(self.frame, (cx, cy), 3, (255, 0, 255), cv.FILLED)

                mp_draw.draw_landmarks(self.frame, handLms, mp_hands.HAND_CONNECTIONS)


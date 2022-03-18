
import mediapipe as mp
import cv2 as cv

from src.player.window import ShowPlayer


class FingerCount(ShowPlayer):

    def write_output_text(self, text=''):
        font = cv.FONT_HERSHEY_SIMPLEX
        line_type = cv.LINE_AA

        cv.putText(self.frame_out, text, (50, 75), font, 0.75, (0, 0, 0), 1, line_type)

    def _detect(self):
        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands(static_image_mode=False,
                               max_num_hands=2,
                               min_detection_confidence=0.5,
                               min_tracking_confidence=0.5)

        img_rgb = cv.cvtColor(self.frame_in, cv.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            height, width, _ = self.frame.shape

            count = {'RIGHT': 0, 'LEFT': 0}
            fingers_tips_ids = [mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                                mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP]
            fingers_statuses = {'RIGHT_THUMB': False, 'RIGHT_INDEX': False, 'RIGHT_MIDDLE': False, 'RIGHT_RING': False,
                                'RIGHT_PINKY': False, 'LEFT_THUMB': False, 'LEFT_INDEX': False, 'LEFT_MIDDLE': False,
                                'LEFT_RING': False, 'LEFT_PINKY': False}

            for hand_index, hand_info in enumerate(results.multi_handedness):
                hand_label = hand_info.classification[0].label
                hand_landmarks = results.multi_hand_landmarks[hand_index]

                for tip_index in fingers_tips_ids:
                    finger_name = tip_index.name.split("_")[0]
                    if hand_landmarks.landmark[tip_index].y < hand_landmarks.landmark[tip_index - 2].y:
                        fingers_statuses[hand_label.upper() + "_" + finger_name] = True
                        count[hand_label.upper()] += 1

                thumb_tip_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
                thumb_mcp_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP - 2].x

                if (hand_label == 'Right' and (thumb_tip_x < thumb_mcp_x)) or \
                        (hand_label == 'Left' and (thumb_tip_x > thumb_mcp_x)):
                    fingers_statuses[hand_label.upper() + "_THUMB"] = True
                    count[hand_label.upper()] += 1

            self.write_output_text('fingers: {}'.format(str(sum(count.values()))))

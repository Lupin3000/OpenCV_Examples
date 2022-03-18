
import bleedfacedetector as fd
import cv2 as cv
import numpy as np

from src.player.window import ShowPlayer


class Emotion(ShowPlayer):

    def write_output_text(self, text=''):
        font = cv.FONT_HERSHEY_SIMPLEX
        line_type = cv.LINE_AA

        cv.putText(self.frame_out, text, (50, 75), font, 0.75, (0, 0, 0), 1, line_type)

    def _detect(self):
        roi_padding = 3
        confidence = 0.8
        model = cv.dnn.readNetFromONNX('src/models/onnx/emotion-ferplus-8.onnx')
        emotions = ['Neutral', 'Happy', 'Surprise', 'Sad', 'Anger', 'Disgust', 'Fear', 'Contempt']

        faces = fd.ssd_detect(self.frame_in, conf=confidence)

        for x_pos, y_pos, width, height in faces:
            face = self.frame_in[y_pos - roi_padding:y_pos + height + roi_padding,
                                 x_pos - roi_padding:x_pos + width + roi_padding]

            frame_gray = cv.cvtColor(face, cv.COLOR_BGR2GRAY)

            resized_face = cv.resize(frame_gray, (64, 64))
            processed_face = resized_face.reshape(1, 1, 64, 64)

            model.setInput(processed_face)
            output = model.forward()

            expanded = np.exp(output - np.max(output))
            probabilities = expanded / expanded.sum()

            prob = np.squeeze(probabilities)
            predicted_emotion = emotions[prob.argmax()]

            cv.rectangle(self.frame_out, (x_pos, y_pos), (x_pos + width, y_pos + height), (0, 0, 255), 2)

            self.write_output_text('emotion: {}'.format(predicted_emotion))

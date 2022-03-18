
import argparse

from src.examples.face_detection.dlib_cnn_face_detection import CnnFace
from src.examples.face_detection.dlib_hog_face_detection import HogFace
from src.examples.face_detection.dlib_face_landmark import DLIBFaceLandmark
from src.examples.face_detection.haarcascade_multiple import HaarcascadeMultiple
from src.examples.face_detection.haarcascade_single import HaarcascadeSingle
from src.examples.face_detection.mediapipe_face_landmark import MPLandmark
from src.examples.face_detection.cvzone_face_detection import CVZFace
from src.examples.face_detection.cvzone_face_mesh import CVZFaceMesh
from src.examples.other_detection.bleedfacedetector_emotion_detection import Emotion
from src.examples.other_detection.deepface_item_detection import Deepface
from src.examples.other_detection.haarcascade_car_detection import CarDetection
from src.examples.other_detection.mediapipe_finger_count import FingerCount
from src.examples.other_detection.mediapipe_hand_landmark import HandLandmark
from src.examples.other_detection.opencv_color_detection import Color
from src.examples.other_detection.cvzone_hand_tracking import CVZHandTracking
from src.examples.other_detection.cvzone_pose_estimation import CVZPoseEstimation
from src.examples.aug.face_filter import FaceFilter
from src.examples.road.lane_detection import LaneDetection
from src.player.window import ShowPlayer


class Examples:

    def __init__(self):
        description = 'command line execution for examples'
        epilog = 'Please read the README for detailed description!'

        parser = argparse.ArgumentParser(description=description, epilog=epilog)

        parser.add_argument("-e", "--example", help='Show example', type=str, default='player')
        parser.add_argument("-i", "--input", help="", default=0)

        args = parser.parse_args()

        self.input_source = args.input
        self.show_example = str(args.example)

    def run_video(self):
        if self.show_example == 'face-1':
            player = HaarcascadeSingle(title='[Haarcascade] face detection', cap=self.input_source)
        elif self.show_example == 'face-2':
            player = HaarcascadeMultiple(title='[Haarcascade] face, eye and smile detection', cap=self.input_source)
        elif self.show_example == 'face-3':
            player = CnnFace(title='[Dlib] CNN face detection', cap=self.input_source)
        elif self.show_example == 'face-4':
            player = HogFace(title='[Dlib] HOG face detection', cap=self.input_source)
        elif self.show_example == 'face-5':
            player = DLIBFaceLandmark(title='[Dlib] face mesh detection', cap=self.input_source)
        elif self.show_example == 'face-6':
            player = MPLandmark(title='[Mediapipe] face mesh detection', cap=self.input_source)
        elif self.show_example == 'face-7':
            player = CVZFace(title='[CVZone] face detection', cap=self.input_source)
        elif self.show_example == 'face-8':
            player = CVZFaceMesh(title='[CVZone] face mesh detection', cap=self.input_source)
        elif self.show_example == 'other-1':
            player = Color(title='[OpenCV] color detection', cap=self.input_source)
        elif self.show_example == 'other-2':
            player = Emotion(title='[Bleedfacedetector] face emotion detection', cap=self.input_source)
        elif self.show_example == 'other-3':
            player = HandLandmark(title='[Mediapipe] hand mesh detection', cap=self.input_source)
        elif self.show_example == 'other-4':
            player = FingerCount(title='[Mediapipe] finger count detection', cap=self.input_source)
        elif self.show_example == 'other-5':
            player = Deepface(title='[Deepface] human detection', cap=self.input_source)
        elif self.show_example == 'other-6':
            player = CarDetection(title='[Haarcascade] car detection', cap=self.input_source)
        elif self.show_example == 'other-7':
            player = CVZHandTracking(title='[CVZone] hand tracking', cap=self.input_source)
        elif self.show_example == 'other-8':
            player = CVZPoseEstimation(title='[CVZone] pose estimation', cap=self.input_source)
        elif self.show_example == 'aug-1':
            player = FaceFilter(title='[Haarcascade] face filter', cap=self.input_source)
        elif self.show_example == 'road-1':
            player = LaneDetection(title='[Road lane detection]', cap=self.input_source)
        else:
            player = ShowPlayer(title='[Camera player]')

        player.start()


if __name__ == '__main__':
    RUN = Examples()
    RUN.run_video()


from cvzone.FaceMeshModule import FaceMeshDetector

from src.player.window import ShowPlayer


class CVZFaceMesh(ShowPlayer):

    def _detect(self):
        detector = FaceMeshDetector(maxFaces=2)
        faces = detector.findFaceMesh(self.frame_in)

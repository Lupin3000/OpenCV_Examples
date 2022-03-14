
import cv2 as cv
import mediapipe as mp

from src.player.window import ShowPlayer


class MPLandmark(ShowPlayer):

    def _detect(self):
        mpDraw = mp.solutions.drawing_utils
        mpFaceMesh = mp.solutions.face_mesh
        faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
        drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)

        frame_rgb = cv.cvtColor(src=self.frame, code=cv.COLOR_BGR2RGB)

        results = faceMesh.process(frame_rgb)

        if results.multi_face_landmarks:
            for faceLms in results.multi_face_landmarks:
                mpDraw.draw_landmarks(self.frame, faceLms, mpFaceMesh.FACEMESH_CONTOURS, drawSpec, drawSpec)

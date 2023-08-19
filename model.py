from dataclasses import dataclass
import torch
import mediapipe as mp
import numpy as np
import cv2
from ultralytics import YOLO


transform = lambda x: (torch.from_numpy(x).permute(2, 0, 1) / 255).float()[None, ...]


@dataclass
class TrackModel:
    model_type: str = 'face'  # Choose among [face, hand, pose, bg]

    mp_hands = None
    hands = None
    mp_drawing = None

    mp_face_mesh = None
    mp_drawing_styles = None

    mp_pose = None
    pose = None

    bg_model = None
    predict_fn = None

    def __post_init__(self):
        if self.model_type == 'hand':
            # Hand Tracking
            self.mp_hands = mp.solutions.hands
            self.hands = self.mp_hands.Hands(static_image_mode=False, max_num_hands=2,
                                             min_detection_confidence=0.5, min_tracking_confidence=0.5)
            self.mp_drawing = mp.solutions.drawing_utils
            self.predict_fn = self.hand_tracking

        elif self.model_type == 'face':
            # Face Tracking
            self.mp_face_mesh = mp.solutions.face_mesh
            self.mp_drawing_styles = mp.solutions.drawing_styles
            self.mp_drawing = mp.solutions.drawing_utils
            self.predict_fn = self.face_tracking

        elif self.model_type == 'pose':
            # Pose Tracking
            self.mp_pose = mp.solutions.pose
            self.pose = self.mp_pose.Pose(static_image_mode=False,
                                          min_detection_confidence=0.5, min_tracking_confidence=0.5)
            self.predict_fn = self.pose_tracking

        elif self.model_type == 'bg':
            # BG Removal
            self.bg_model = YOLO("bg_models/yolov8n-seg.pt")
            _ = self.bg_model.predict(np.zeros((640, 640, 3), dtype=np.uint8))
            self.predict_fn = self.bg_removal

    def hand_tracking(self, image):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.hands.process(image_rgb)

        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(
                    image, landmarks, self.mp_hands.HAND_CONNECTIONS)

        return image

    def face_tracking(self, image):
        with self.mp_face_mesh.FaceMesh(
                max_num_faces=1,
                refine_landmarks=True,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5) as face_mesh:

            # Convert the image to RGB format (required by Mediapipe)
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(image_rgb)

            if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    self.mp_drawing.draw_landmarks(
                        image=image,
                        landmark_list=face_landmarks,
                        connections=self.mp_face_mesh.FACEMESH_TESSELATION,
                        # landmark_drawing_spec=None,
                        landmark_drawing_spec=self.mp_drawing.DrawingSpec(color=(0, 0, 0),
                                                                          thickness=0, circle_radius=0),
                        connection_drawing_spec=self.mp_drawing.DrawingSpec(color=(150, 100, 0),
                                                                            thickness=1, circle_radius=0))

            return image

    def pose_tracking(self, image):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.pose.process(image_rgb)

        if results.pose_landmarks:
            # Draw circles at each landmark
            for landmark in results.pose_landmarks.landmark:
                h, w, c = image.shape
                x, y = int(landmark.x * w), int(landmark.y * h)
                cv2.circle(image, (x, y), 5, (0, 255, 0), -1)

            # Draw lines connecting landmarks
            connections = [(11, 12), (11, 13), (13, 15), (12, 14), (14, 16), (11, 23), (12, 24),
                           (23, 25), (24, 26), (25, 27), (26, 28), (27, 29), (28, 30),
                           (23, 24), (27, 28), (29, 31), (30, 32), (11, 23), (12, 24),
                           # (23, 0), (24, 0), (8, 5), (5, 0), (0, 2), (2, 7)
                           ]

            for connection in connections:
                start_point = results.pose_landmarks.landmark[connection[0]]
                end_point = results.pose_landmarks.landmark[connection[1]]

                start_x, start_y = int(
                    start_point.x * w), int(start_point.y * h)
                end_x, end_y = int(end_point.x * w), int(end_point.y * h)

                cv2.line(image, (start_x, start_y),
                         (end_x, end_y), (200, 100, 0), 2)

        return image

    def bg_removal(self, image):
        results = self.bg_model.predict(image.copy())[0]
        output_mask = np.zeros_like(image, dtype='float32')
        if results.masks:
            for i in range(len(results.boxes.boxes)):
                if int(results.boxes.boxes[i, -1].item()) == 0:
                    output_mask = results.masks.masks.detach().cpu()[i][..., None]
                    image = np.where(output_mask, image, 0)
        return image
    
    def predict(self, image):
        output_image = self.predict_fn(np.ascontiguousarray(image))
        return cv2.imencode('.jpg', output_image[:, :, ::-1])[-1].tostring()

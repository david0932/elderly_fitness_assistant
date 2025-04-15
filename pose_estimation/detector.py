from ultralytics import YOLO

class PoseDetector:
    def __init__(self, model_path='yolov8n-pose.pt'):
        self.model = YOLO(model_path)

    def detect(self, frame):
        results = self.model(frame)
        if results and len(results[0].keypoints.xy) > 0:
            return results[0].keypoints.xy[0]
        return None

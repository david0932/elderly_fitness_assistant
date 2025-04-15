from ultralytics import YOLO
import cv2

def main():
    model = YOLO('yolov8n-pose.pt')  # 會自動下載模型
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ 無法開啟攝影機")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        annotated = results[0].plot()

        # 顯示是否有抬腳（用比例判斷）
        if results[0].keypoints is not None and len(results[0].keypoints.xy) > 0:
            keypoints = results[0].keypoints.xy[0]
            try:
                hip_y = keypoints[11][1].item()
                knee_y = keypoints[13][1].item()
                ankle_y = keypoints[15][1].item()
                leg_length = ankle_y - hip_y
                lifted = hip_y - knee_y
                ratio = lifted / leg_length if leg_length > 0 else 0
                if ratio > 0.4:
                    cv2.putText(annotated, "VVVV OK", (30, 80),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
                else:
                    cv2.putText(annotated, "XXXX NG", (30, 80),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
            except:
                pass

        cv2.imshow("Foot lift detection test", annotated)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

from ultralytics import YOLO
import cv2

def main():
    model = YOLO('yolov8n-pose.pt')
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        annotated = results[0].plot()

        if results[0].keypoints is not None and len(results[0].keypoints.xy) > 0:
            keypoints = results[0].keypoints.xy[0]
            try:
                # 使用右側：右髖(12), 右膝(14), 右腳踝(16)
                hip_y = keypoints[12][1].item()
                knee_y = keypoints[14][1].item()
                ankle_y = keypoints[16][1].item()

                leg_length = ankle_y - hip_y
                lifted = knee_y - hip_y  # ✅ 小於 0 表示抬腳
                ratio = lifted / leg_length if leg_length > 0 else 0

                print(f"Lift ratio: {ratio:.2f}")

                if ratio > 0.35:  
                    cv2.putText(annotated, f"Leg raised OK ({ratio:.2f})", (30, 80),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
                else:
                    cv2.putText(annotated, f"Raise leg HIGH ({ratio:.2f})", (30, 80),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
            except Exception as e:
                print("Error extracting keypoints:", e)

        cv2.imshow("Leg Raise Detection Debug", annotated)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

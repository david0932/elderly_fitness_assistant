from ultralytics import YOLO
import cv2

def main():
    model = YOLO('yolov8n-pose.pt')  # 請先確認這個檔案存在或讓程式自動下載

    cap = cv2.VideoCapture(0)  # 使用內建攝影機

    if not cap.isOpened():
        print("❌ 無法開啟攝影機")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)

        annotated_frame = results[0].plot()  # 在畫面上繪製關鍵點與骨架

        cv2.imshow("YOLOv8 Pose 測試", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

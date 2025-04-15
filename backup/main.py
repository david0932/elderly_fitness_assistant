import cv2
import time
from pose_estimation.detector import PoseDetector
from pose_estimation.counter import LegRaiseCounter
from ui.display import show_frame
from tts.speaker import Speaker

def main():
    cap = cv2.VideoCapture(0)
    detector = PoseDetector()
    counter = LegRaiseCounter()
    speaker = Speaker()

    speaker.say("歡迎使用AI運動助理，我們今天要做的是站姿抬腳運動。準備好了嗎？我們開始！")

    goal = 10
    goal_announced = False

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        keypoints = detector.detect(frame)
        count, is_lifted = counter.update(keypoints)
        current_time = time.time()

        if keypoints is not None:
            if is_lifted:
                if current_time - speaker.last_good_time > 5:
                    speaker.say("很好，保持這個姿勢！")
                    speaker.last_good_time = current_time
            else:
                if current_time - speaker.last_warn_time > 3:
                    speaker.say("請再抬高一點喔～")
                    speaker.last_warn_time = current_time

        if count >= goal and not goal_announced:
            speaker.say(f"太棒了！你已經完成 {goal} 次抬腳運動，做得很好！")
            goal_announced = True

        show_frame(frame, count)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            speaker.say("運動結束，記得每天都要動一動喔！")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

import cv2
import time
from pose_estimation.detector import PoseDetector
from pose_estimation.counter import LegRaiseCounter
from ui.display import show_frame
from tts.speaker import Speaker
from tts.audio_player import AudioPlayer
from time import sleep

def main():
    cap = cv2.VideoCapture(0)
    detector = PoseDetector()
    counter = LegRaiseCounter()
    speaker = Speaker()
    audio_player = AudioPlayer()
    #speaker.say("Welcome to the AI exercise assistant. Let's begin our leg raise activity!")
    #speaker.say("歡迎來到AI運動助理! 讓我們開始今天的抬腳活動!")
    # play wave file ./tts/App-Title.wav
    audio_player.play_wav("./tts/start.wav")
    #speaker.say("Please raise your leg higher.")
    #speaker.say("腳要抬高!")

    goal = 10
    goal_announced = False

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        keypoints = detector.detect(frame)
        count, is_lifted, ratio = counter.update(keypoints)
        current_time = time.time()

        if keypoints is not None:
            # Show ratio on frame for debug
            status_text = ""
            if ratio is not None:
                if ratio > 0.3:
                    status_text = f"Leg raised OK ({ratio:.2f})"
                    #status_text = f"抬腳成功 ({ratio:.2f})"
                    if current_time - speaker.last_good_time > 5:
                        #speaker.say("Good! Hold that leg up!")
                        #speaker.say("很好! 換抬另一腳!")
                        audio_player.play_wav("./tts/good-change-leg.wav") 
                        speaker.last_good_time = current_time
                else:
                    status_text = f"Raise leg HIGH ({ratio:.2f})"
                    #status_text = f"腳抬高 ({ratio:.2f})"
                    if current_time - speaker.last_warn_time > 10:
                        #speaker.say("Please raise your leg higher.")
                        #speaker.say("腳要抬高!")
                        audio_player.play_wav("./tts/raise-leg-higher.wav")   
                        speaker.last_warn_time = current_time

                cv2.putText(frame, status_text, (30, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2,
                            (0, 255, 0) if ratio > 0.3 else (0, 0, 255), 3)

        if count >= goal and not goal_announced:
            #speaker.say(f"Excellent! You have completed {goal} leg raises!")
            #speaker.say(f"很棒! 你今天完成 {goal} 抬腳!")
            audio_player.play_wav("./tts/finish-10-times.wav")    
            goal_announced = True
            sleep(5)
            break

        show_frame(frame, count)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            #speaker.say("Exercise session ended. Keep moving every day!")
            #speaker.say("抬腳課程結束，每天堅持運動哦!")
            audio_player.play_wav("./tts/end-keep-on.wav")
            # wait for speaker to finish speaking before exiting the ap
            sleep(10) # wait for speaker to finish speaking before exiting the ap
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

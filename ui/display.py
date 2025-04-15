import cv2

def show_frame(frame, count):
    #cv2.putText(frame, f'抬腳次數：{count}', (30, 50),
    cv2.putText(frame, f'Count: {count}', (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
    #cv2.imshow("老人運動AI助手", frame)
    cv2.imshow("AI assistant for elderly sports", frame)

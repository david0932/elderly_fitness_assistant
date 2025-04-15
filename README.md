# 長者健身助理系統 (Elderly Fitness Assistant)

這是一個基於AI技術的長者健身助理系統，使用姿態檢測技術來輔助長者進行抬腿運動，並提供即時語音回饋和指導。

## 主要功能

- 即時姿態檢測：使用YOLO模型進行人體姿態檢測
- 動作計數：自動計算完成的抬腿次數
- 語音指導：提供中英雙語的即時語音回饋
- 視覺回饋：在畫面上顯示動作完成度和計數

## 系統需求

- Python 3.8+
- 網路攝像頭
- 音訊輸出設備

## 安裝步驟

1. Clone專案到本地：
```bash
git clone [repository-url]
cd elderly_fitness_assistant
```

2. 安裝依賴套件：
```bash
pip install -r requirements.txt
```

3. 下載YOLOv8姿態檢測模型：
```bash
# 模型檔案已包含在專案中：yolov8n-pose.pt
```

## 使用方法

1. 運行主程式：
```bash
python main.py
```

2. 站在攝像頭前，保持適當距離（建議1.5-2米）

3. 按照語音指示進行抬腿運動：
   - 系統會自動檢測腿部抬起的高度
   - 當動作正確時會給予正面回饋
   - 需要調整時會提供指導建議

4. 完成10次抬腿動作後，系統會自動結束，或按'q'鍵手動結束

## 技術架構

- 姿態檢測：使用YOLOv8進行即時人體姿態檢測
- 視覺介面：OpenCV處理視訊串流和視覺回饋
- 語音系統：整合TTS（文字轉語音）系統提供即時語音指導

## 專案結構

```
├── main.py                 # 主程式
├── pose_estimation/        # 姿態檢測相關模組
│   ├── detector.py         # YOLO檢測器
│   └── counter.py          # 動作計數器
├── tts/                    # 語音系統
│   ├── speaker.py          # TTS模組
│   └── audio_player.py     # 音訊播放器
└── ui/                     # 使用者介面
    └── display.py          # 畫面顯示模組
```

## 注意事項

- 請在光線充足的環境下使用
- 確保攝像頭可以拍攝到全身
- 建議在有扶手或安全支撐的環境下進行運動
- 如感到不適，請立即停止運動並諮詢醫生
## DEMO
![image](https://github.com/david0932/elderly_fitness_assistant/blob/master/demo/elderly-fitness-assistant.gif?raw=true)
![Demo Video](https://github.com/david0932/elderly_fitness_assistant/blob/master/demo/elderly-fitness-assistant.mp4)



## 授權

本專案採用 MIT 授權條款 - 詳見 LICENSE 文件

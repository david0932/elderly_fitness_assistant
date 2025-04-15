class LegRaiseCounter:
    def __init__(self, hip_idx=12, knee_idx=14, ankle_idx=16, lift_ratio_threshold=0.35):
        self.hip_idx = hip_idx
        self.knee_idx = knee_idx
        self.ankle_idx = ankle_idx
        self.lift_ratio_threshold = lift_ratio_threshold
        self.count = 0
        self.leg_up = False

    def update(self, keypoints):
        if keypoints is None or len(keypoints) <= max(self.hip_idx, self.knee_idx, self.ankle_idx):
            return self.count, False, None

        hip_y = keypoints[self.hip_idx][1].item()
        knee_y = keypoints[self.knee_idx][1].item()
        ankle_y = keypoints[self.ankle_idx][1].item()

        leg_length = ankle_y - hip_y
        lifted = knee_y - hip_y
        ratio = lifted / leg_length if leg_length > 0 else 0

        if ratio > self.lift_ratio_threshold:
            if not self.leg_up:
                self.leg_up = True
                self.count += 1
            return self.count, True, ratio
        else:
            self.leg_up = False
            return self.count, False, ratio

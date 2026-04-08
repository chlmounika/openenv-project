import random

class StudyEnv:
    def __init__(self, task="easy"):
        self.task = task
        self.state = 0

    def reset(self):
        self.state = 0
        return self.state

    def step(self, action):
        reward = 0
        done = False

        # action logic
        if action == "study":
            self.state += 1
            reward = 1
        else:
            reward = 0

        # 🎯 TASK CONDITIONS
        if self.task == "easy":        # Task 1
            done = self.state >= 3

        elif self.task == "medium":    # Task 2
            done = self.state >= 5

        elif self.task == "hard":      # Task 3
            # if any wrong action → fail
            if action != "study":
                done = True
                reward = 0
            elif self.state >= 5:
                done = True

        return self.state, reward, done, {}

    def get_state(self):
        return self.state
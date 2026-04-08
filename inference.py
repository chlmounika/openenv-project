from env import StudyEnv

print("[START]")

tasks = ["easy", "medium", "hard"]

for task in tasks:
    print(f"[STEP] Running task: {task}")
    
    env = StudyEnv(task=task)
    state = env.reset()
    done = False
    total_reward = 0

    while not done:
        action = "study"   # simple baseline
        state, reward, done, _ = env.step(action)
        total_reward += reward

    print(f"[STEP] Task {task} completed with reward {total_reward}")

print("[END]")
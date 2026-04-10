import os
from openai import OpenAI
from env import CloudScalingEnv
from grader import grade


def get_llm_action(client, state):
    """Ask the LLM to decide the scaling action based on current state."""
    prompt = f"""You are a cloud auto-scaling agent. Based on the current environment state, decide the best action.

Current State:
- CPU Utilization: {state['cpu_utilization']:.2f} (0.0 to 1.0, ideal is ~0.6)
- Memory Utilization: {state['memory_utilization']:.2f}
- Number of Instances: {state['num_instances']}
- Incoming Traffic: {state['incoming_traffic']}
- Time Step: {state['time_step']}

Actions available:
- 0: do_nothing (keep current instances)
- 1: scale_up (add one instance, costs more but reduces CPU load)
- 2: scale_down (remove one instance, saves cost but increases CPU load)

Rules:
- If CPU > 0.75, scale up to prevent overload
- If CPU < 0.4, scale down to save cost
- If CPU is between 0.4 and 0.75, do nothing

Respond with ONLY a single digit: 0, 1, or 2."""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=10,
        temperature=0,
    )

    raw = response.choices[0].message.content.strip()

    
    if raw in ("0", "1", "2"):
        return int(raw)
    else:
        cpu = state["cpu_utilization"]
        if cpu > 0.75:
            return 1
        elif cpu < 0.4:
            return 2
        return 0


def run(client, difficulty):
    env = CloudScalingEnv(difficulty=difficulty)
    state = env.reset()

    total_reward = 0
    step_num = 0

    print(f"[START] task={difficulty}", flush=True)

    for _ in range(50):
        step_num += 1

        action = get_llm_action(client, state)
        state, reward, done = env.step(action)
        total_reward += reward

        print(f"[STEP] step={step_num} reward={round(reward, 4)}", flush=True)

        if done:
            break

    normalized_score = grade(total_reward)

    print(f"[END] task={difficulty} score={round(normalized_score, 2)} steps={step_num}", flush=True)

    return {
        "raw_score": round(total_reward, 2),
        "normalized_score": round(normalized_score, 2),
    }


if __name__ == "__main__":

    api_base_url = os.environ["API_BASE_URL"]
    api_key = os.environ["API_KEY"]

    client = OpenAI(
        base_url=api_base_url,
        api_key=api_key,
    )

    for level in ["easy", "medium", "hard"]:
        run(client, level)

LLM-Powered Autonomous Cloud Scaling Environment (OpenEnv)

Overview

This project simulates a real-world cloud auto-scaling system where an AI agent intelligently adjusts computing resources based on live workload conditions.

Instead of fixed rules, a Large Language Model (LLM) is used to make dynamic scaling decisions, improving both performance and cost efficiency.

---

Problem Statement

Cloud systems often rely on static rules (e.g., CPU > 70% → scale up), which:

* Waste resources
* Fail under unpredictable traffic
* Cannot adapt to real-time conditions

---

Solution

An AI-driven cloud scaling environment is built where:

* The system observes real-time metrics (CPU, memory, traffic)
* An LLM decides whether to:

  * Scale up
  * Scale down
  * Do nothing
* A reward system ensures optimal performance (~60% CPU)

---

Architecture

User → FastAPI API → Cloud Environment
↓
LLM Decision Agent
↓
Reward Function

---

Key Features

* Real-world cloud scaling simulation
* OpenEnv compliant (step() / reset() / state())
* LLM-powered decision making
* Multi-task support (Easy / Medium / Hard)
* Reward shaping for performance optimization
* FastAPI backend for interaction
* Dockerized deployment (Hugging Face Spaces)

---

Tasks & Difficulty Levels

| Level  | Description                              |
| ------ | ---------------------------------------- |
| Easy   | Stable traffic, predictable load         |
| Medium | Moderate fluctuations                    |
| Hard   | Highly dynamic and unpredictable traffic |

---

Sample Output

```
[START] task=easy
[STEP] step=1 reward=0.82
[STEP] step=2 reward=0.78
...
[END] task=easy score=0.76
```

---

API Endpoints
* POST /reset → Initialize environment
* POST /step → Take action (0,1,2)

---

Why LLM?

Unlike rule-based systems, the LLM:

* Adapts to unseen traffic patterns
* Balances cost vs performance
* Makes context-aware decisions

---

Results

* Achieves stable CPU utilization (~60%)
* Reduces unnecessary scaling
* Maintains efficient cloud performance
---

Tech Stack

* Python
* FastAPI
* OpenAI (LLM via proxy)
* Docker
* Hugging Face Spaces

---
How to Run

1. Install dependencies

```
pip install -r requirements.txt
```

2. Run API

```
uvicorn main:app --reload
```

3. Run inference

```
python inference.py
```

Deployment

Deployed on Hugging Face Spaces using Docker.

Impact

This project demonstrates how AI can replace static cloud rules with intelligent decision-making for real-world infrastructure systems.

Author

Monisha B


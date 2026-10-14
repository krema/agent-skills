"""Synthetic audit input. Effects are recorded in memory only."""

import json
from pathlib import Path


class Executor:
    def __init__(self):
        self.effects = []

    def publish(self, candidate):
        self.effects.append({"kind": "publish", "candidate": candidate})
        return "published"


def dispatch(candidate, report, executor):
    if not report.get("passed"):
        return "blocked"
    return executor.publish(candidate)


def run_case(case):
    executor = Executor()
    if case["path"] == "dispatcher":
        result = dispatch(case["candidate"], case["report"], executor)
    elif case["path"] == "direct":
        result = executor.publish(case["candidate"])
    else:
        raise ValueError("Unknown execution path")
    return {"id": case["id"], "result": result, "effects": executor.effects}


if __name__ == "__main__":
    scenarios = json.loads(Path(__file__).with_name("scenarios.json").read_text())
    print(json.dumps([run_case(case) for case in scenarios], indent=2))

"""CLI for ai-governance-toolkit."""
import sys, json, argparse
from .core import AiGovernanceToolkit

def main():
    parser = argparse.ArgumentParser(description="Framework for AI governance — policies, compliance, risk assessment, and auditing")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = AiGovernanceToolkit()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.analyze(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"ai-governance-toolkit v0.1.0 — Framework for AI governance — policies, compliance, risk assessment, and auditing")

if __name__ == "__main__":
    main()

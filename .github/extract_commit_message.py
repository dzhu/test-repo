import json
import sys

event = json.load(sys.stdin)

print(event["pull_request"]["title"])
print()
for line in event["pull_request"]["body"].splitlines():
    if line == "# Test Plan":
        break
    print(line)

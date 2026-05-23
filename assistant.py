import json

with open("commands.json","r") as file:
    commands = json.load(file)

for cmd in commands:
    print(f"command: {cmd['command']}")
    print(f"description: {cmd['description']}")
    print(f"Example: {cmd['example']}")
    print("-" * 30)
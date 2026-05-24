import json
with open ("commands.json", "r") as file:
    commands = json.load(file)

search = input("Enter Linux command: ")

found = False
for cmd in commands:
    if search.lower() in cmd["command"].lower():
        print(f"\nCommand: {cmd['command']}")
        print(f"Description: {cmd['description']}")
        print(f"Example: {cmd['example']}")
        found = True
        
    if not found:
        print("Command not found.")
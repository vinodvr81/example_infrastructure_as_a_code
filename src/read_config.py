import json

with open("service_config.json") as f:
    config = json.load(f)

print(f"Connecting to DB at {config['host']}:{config['port']} as {config['username']}")

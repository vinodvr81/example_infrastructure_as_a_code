import json
from jinja2 import Template

def load_env_file(file_path):
    env_data = {}
    with open(file_path, "r", encoding="utf-8") as f:  # Read as ANSI
        for line in f:
            if "=" in line:
                key, value = line.strip().split("=", 1)
                env_data[key] = value
    return env_data

env_vars = load_env_file(".env")

template_str = '''{
        "host": "{{ db_host }}",
        "port": {{ db_port }},
        "username": "{{ db_user }}",
        "password": "{{ db_pass }}"
}'''

template = Template(template_str)
config_data = template.render(
    db_host=env_vars["HOST"],
    db_port=int(env_vars["PORT"]),
    db_user=env_vars["USER"],
    db_pass=env_vars["PASS"]
)

# Save configuration as JSON
with open("service_config.json", "w") as fh:
    json.dump(json.loads(config_data), fh, indent=4)

print("✅ Service configuration saved to service_config.json")

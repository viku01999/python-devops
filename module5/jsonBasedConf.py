from jsonschema import validate, ValidationError
import json


schema = {
    "type": "object",
    "properties": {
        "server": {"type": "string"},
        "status": {"type": "string"}
    },
    "required": ["server", "status"]
}


data = {"server": "web1", "status": "active"}

try:
    validate(instance=data, schema=schema)
    print("JSON is valid")
except ValidationError as e:
    print(f"Invalid JSON: {e.message}")

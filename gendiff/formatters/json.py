import json

def make_output(difference: list[dict]) -> dict:
    return json.dumps(difference, indent=2)
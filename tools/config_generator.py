import json
from jsonschema import validate, ValidationError

# Define the JSON schema for the config generator input format
CONFIG_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "version": {"type": "number"},
        "features": {"type": "array", "items": {"type": "string"}}
    },
    "required": ["name", "version", "features"]
}

# Function to validate input files before generation
def validate_input(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    try:
        validate(instance=data, schema=CONFIG_SCHEMA)
    except ValidationError as e:
        print(f'Validation error: {e}')
        return False
    return True

# Function to generate configuration based on input
def generate_config(input_file_path, output_file_path):
    if not validate_input(input_file_path):
        print('Input validation failed. Aborting generation.')
        return
    with open(input_file_path, 'r') as file:
        data = json.load(file)
    # Generate configuration based on input data
    config_content = {
        "name": data['name'],
        "version": data['version'],
        "features": data['features']
    }
    with open(output_file_path, 'w') as file:
        json.dump(config_content, file, indent=4)

# Example usage
input_file = 'data/config_input.json'
output_file = 'data/config_output.json'
generate_config(input_file, output_file)
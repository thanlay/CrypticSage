import json

def validate_data(data: dict, required_keys: list):
    """
    Validate data contains required keys.
    :param data: Dictionary to validate
    :param required_keys: List of required keys
    :raises ValidationError: If validation fails
    """
    missing_keys = [key for key in required_keys if key not in data]
    if missing_keys:
        raise ValidationError(f"Missing keys: {missing_keys}")


def format_json(data: dict) -> str:
    """
    Format a dictionary as a pretty JSON string.
    :param data: Dictionary to format
    :return: JSON string
    """
    return json.dumps(data, indent=4)
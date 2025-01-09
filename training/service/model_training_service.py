import random


class ModelTrainingService:
    """
    Manages distributed training and validation of AI models.
    """

    def __init__(self):
        # Simulate storage for model parameters
        self.model_params = {}

    def train_model(self, data: list, model_id: str) -> dict:
        """
        Train the model locally and generate model parameters.
        :param data: Training data
        :param model_id: Model ID
        :return: Trained model parameters
        """
        print(f"Starting training for model {model_id}...")
        # Simulate training: Generate random weights
        model_params = {f"weight_{i}": random.random() for i in range(5)}
        self.model_params[model_id] = model_params
        print(f"Model {model_id} training completed")
        return model_params

    def validate_model(self, model_id: str, validation_data: list) -> bool:
        """
        Validate the effectiveness of the model parameters.
        :param model_id: Model ID
        :param validation_data: Validation data
        :return: Validation result
        """
        print(f"Starting validation for model {model_id}...")
        if model_id not in self.model_params:
            raise ValueError(f"Model {model_id} does not exist")

        # Simulate validation: Simple validation rule
        is_valid = all(value > 0 for value in self.model_params[model_id].values())
        print(f"Model {model_id} validation result: {'Passed' if is_valid else 'Failed'}")
        return is_valid
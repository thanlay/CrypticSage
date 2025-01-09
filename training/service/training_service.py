import json
from typing import Dict, Any
import requests

class TrainingService:
    """
    Model training and validation service, supporting decentralized federated learning.
    """

    def __init__(self, blockchain_url: str):
        """
        Initialize the training service.
        :param blockchain_url: URL of the blockchain node API
        """
        self.blockchain_url = blockchain_url

    def train_model(self, node_address: str, data: Dict[str, Any], model_id: str) -> Dict[str, Any]:
        """
        Train the model on a node.
        :param node_address: Address of the computing node
        :param data: Training data
        :param model_id: Model ID
        :return: Trained model parameters
        """
        print(f"Sending training task to node: {node_address}")
        payload = {
            "model_id": model_id,
            "data": data
        }
        response = requests.post(f"http://{node_address}/train", json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f"Training task failed: {response.text}")

    def validate_model(self, model_params: Dict[str, Any], validation_data: Dict[str, Any]) -> bool:
        """
        Validate the model parameters.
        :param model_params: Parameters of the trained model
        :param validation_data: Validation data
        :return: Whether the model validation passes
        """
        # Calculate validation accuracy (example logic)
        correct_predictions = 0
        total_predictions = len(validation_data["labels"])

        for input_data, label in zip(validation_data["inputs"], validation_data["labels"]):
            predicted = self._predict(input_data, model_params)
            if predicted == label:
                correct_predictions += 1

        accuracy = correct_predictions / total_predictions
        print(f"Validation accuracy: {accuracy:.2f}")

        # Set an accuracy threshold, e.g., pass if accuracy is above 90%
        return accuracy >= 0.9

    def _predict(self, input_data: Any, model_params: Dict[str, Any]) -> Any:
        """
        Make predictions using the trained model parameters (example implementation).
        :param input_data: Input data
        :param model_params: Model parameters
        :return: Prediction result
        """
        # Example logic: Simple linear model prediction
        weights = model_params.get("weights", [])
        bias = model_params.get("bias", 0)
        prediction = sum(w * x for w, x in zip(weights, input_data)) + bias
        return round(prediction)  # For binary classification, return 0 or 1
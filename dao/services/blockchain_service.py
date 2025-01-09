import requests
from core.config import Config
from core.logger import Logger
from utils.error_handling import BlockchainError

logger = Logger.setup_logger("BlockchainService")

class BlockchainService:
    """
    Interface for blockchain interactions.
    """

    def __init__(self):
        self.rpc_url = Config.get("BLOCKCHAIN_RPC_URL")

    def send_transaction(self, method: str, params: list):
        """
        Send a transaction to the blockchain via RPC.
        :param method: RPC method name
        :param params: Parameters for the RPC call
        :raises BlockchainError: If the RPC call fails
        """
        payload = {"jsonrpc": "2.0", "method": method, "params": params, "id": 1}
        try:
            response = requests.post(self.rpc_url, json=payload)
            response_data = response.json()
            if "error" in response_data:
                raise BlockchainError(response_data["error"]["message"])
            return response_data["result"]
        except requests.RequestException as e:
            logger.error(f"RPC call failed: {e}")
            raise BlockchainError("Failed to connect to blockchain RPC.")
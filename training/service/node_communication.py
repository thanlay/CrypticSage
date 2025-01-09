import requests

class NodeCommunication:
    """
    Simulates communication with distributed computing nodes.
    """

    @staticmethod
    def send_task_to_node(node_url: str, task: dict) -> dict:
        """
        Send a task to the specified computing node.
        :param node_url: Node URL
        :param task: Task information
        :return: Task execution result returned by the node
        """
        try:
            response = requests.post(f"{node_url}/execute_task", json=task)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Failed to communicate with the node: {e}")
            return {"status": "failed", "error": str(e)}
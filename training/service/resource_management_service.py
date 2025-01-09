class ResourceManagementService:
    """
    Manages distributed computing nodes and assigns AI model training tasks.
    """

    def __init__(self):
        # Simulate node resource storage: node_id -> {resource information}
        self.nodes = {}

    def register_node(self, node_id: str, resources: dict) -> bool:
        """
        Register a computing node and store its resource information.
        :param node_id: Unique identifier of the node
        :param resources: Resource information of the node (e.g., CPU, GPU, memory)
        :return: Whether the registration was successful
        """
        if node_id in self.nodes:
            raise ValueError(f"Node {node_id} already exists")
        self.nodes[node_id] = resources
        return True

    def assign_task(self, task_id: str, required_resources: dict) -> str:
        """
        Assign a task to a node that meets the resource requirements.
        :param task_id: Unique identifier of the task
        :param required_resources: Resources required by the task
        :return: ID of the node assigned to the task
        """
        for node_id, resources in self.nodes.items():
            if self._check_resources(resources, required_resources):
                print(f"Task {task_id} assigned to node {node_id}")
                return node_id
        raise ValueError("No available node meets the resource requirements")

    def _check_resources(self, node_resources: dict, required_resources: dict) -> bool:
        """
        Check if the node meets the resource requirements of the task.
        :param node_resources: Node resources
        :param required_resources: Resources required by the task
        :return: Whether the requirements are met
        """
        for key, value in required_resources.items():
            if node_resources.get(key, 0) < value:
                return False
        return True

    def get_task_status(self, task_id: str) -> dict:
        """
        Simulate task status query.
        :param task_id: Task ID
        :return: Task status
        """
        # Simulate status return
        return {"task_id": task_id, "status": "Running"}
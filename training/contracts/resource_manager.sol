// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ResourceManager {
    struct Node {
        address nodeAddress;
        uint256 cpu;    // Unit: cores
        uint256 gpu;    // Unit: cores
        uint256 memory; // Unit: GB
        bool isActive;
    }

    mapping(address => Node) public nodes;
    address[] public nodeList;

    event NodeRegistered(address indexed nodeAddress, uint256 cpu, uint256 gpu, uint256 memory);
    event NodeUpdated(address indexed nodeAddress, uint256 cpu, uint256 gpu, uint256 memory);
    event NodeDeactivated(address indexed nodeAddress);

    /**
     * @notice Register a computing node
     * @param cpu Number of CPU cores
     * @param gpu Number of GPU cores
     * @param memory Memory size in GB
     */
    function registerNode(uint256 cpu, uint256 gpu, uint256 memory) external {
        require(cpu > 0 || gpu > 0, "At least one computing resource must be provided");
        require(memory > 0, "Memory size must be greater than 0");

        nodes[msg.sender] = Node({
            nodeAddress: msg.sender,
            cpu: cpu,
            gpu: gpu,
            memory: memory,
            isActive: true
        });

        nodeList.push(msg.sender);
        emit NodeRegistered(msg.sender, cpu, gpu, memory);
    }

    /**
     * @notice Update node resources
     * @param cpu Number of CPU cores
     * @param gpu Number of GPU cores
     * @param memory Memory size in GB
     */
    function updateNode(uint256 cpu, uint256 gpu, uint256 memory) external {
        require(nodes[msg.sender].isActive, "Node is not active");
        nodes[msg.sender].cpu = cpu;
        nodes[msg.sender].gpu = gpu;
        nodes[msg.sender].memory = memory;

        emit NodeUpdated(msg.sender, cpu, gpu, memory);
    }

    /**
     * @notice Deactivate a node
     */
    function deactivateNode() external {
        require(nodes[msg.sender].isActive, "Node is not active");
        nodes[msg.sender].isActive = false;

        emit NodeDeactivated(msg.sender);
    }

    /**
     * @notice Get all node addresses
     * @return List of all node addresses
     */
    function getNodeList() external view returns (address[] memory) {
        return nodeList;
    }
}
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ModelStorage {
    struct Model {
        string modelId;
        bytes32 dataHash; // Hash value of the model parameters
        address owner;    // Owner of the model
    }

    mapping(string => Model) private models; // Mapping from model ID to model data

    event ModelStored(string modelId, bytes32 dataHash, address owner);
    event ModelVerified(string modelId, bool isValid);

    /**
     * @notice Store the hash value of the model on the blockchain.
     * @param modelId The model ID
     * @param dataHash The hash value of the model parameters
     */
    function storeModel(string memory modelId, bytes32 dataHash) external {
        require(bytes(modelId).length > 0, "Model ID cannot be empty");
        require(models[modelId].owner == address(0), "Model already exists");

        models[modelId] = Model(modelId, dataHash, msg.sender);
        emit ModelStored(modelId, dataHash, msg.sender);
    }

    /**
     * @notice Verify the integrity of the model data.
     * @param modelId The model ID
     * @param dataHash The provided hash value
     * @return Verification result
     */
    function verifyModel(string memory modelId, bytes32 dataHash) external view returns (bool) {
        Model memory model = models[modelId];
        require(model.owner != address(0), "Model does not exist");

        bool isValid = (model.dataHash == dataHash);
        emit ModelVerified(modelId, isValid);
        return isValid;
    }
}
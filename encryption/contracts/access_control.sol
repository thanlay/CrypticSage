// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AccessControl {
    struct AccessRule {
        address user;
        uint256 expiration; // Permission expiration time
    }

    mapping(bytes32 => AccessRule) private accessRules; // Mapping from data hash to access rules

    event AccessGranted(bytes32 dataHash, address user, uint256 expiration);
    event AccessRevoked(bytes32 dataHash, address user);

    /**
     * @notice Grants access permission to a specific user.
     * @param dataHash The hash value of the data
     * @param user The user's address
     * @param duration The duration of the permission (in seconds)
     */
    function grantAccess(bytes32 dataHash, address user, uint256 duration) external {
        require(user != address(0), "Invalid user address");
        accessRules[dataHash] = AccessRule(user, block.timestamp + duration);
        emit AccessGranted(dataHash, user, block.timestamp + duration);
    }

    /**
     * @notice Verifies whether the access request is authorized.
     * @param dataHash The hash value of the data
     * @return Whether the access is authorized
     */
    function isAccessGranted(bytes32 dataHash) public view returns (bool) {
        AccessRule memory rule = accessRules[dataHash];
        return (rule.user == msg.sender && block.timestamp <= rule.expiration);
    }

    /**
     * @notice Revokes the access permission of a user.
     * @param dataHash The hash value of the data
     */
    function revokeAccess(bytes32 dataHash) external {
        AccessRule memory rule = accessRules[dataHash];
        require(rule.user != address(0), "Access permission does not exist");
        delete accessRules[dataHash];
        emit AccessRevoked(dataHash, rule.user);
    }
}
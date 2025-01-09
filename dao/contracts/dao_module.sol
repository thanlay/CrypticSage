// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DAOModule {
    struct Proposal {
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
    }

    mapping(uint256 => Proposal) public proposals;
    mapping(address => bool) public voters;
    uint256 public proposalCount;

    event ProposalCreated(uint256 indexed proposalId, string description);
    event Voted(uint256 indexed proposalId, address indexed voter, bool vote);
    event ProposalExecuted(uint256 indexed proposalId);

    /**
     * @dev Create a new proposal.
     * @param description The description of the proposal.
     */
    function createProposal(string memory description) public {
        proposalCount++;
        proposals[proposalCount] = Proposal(description, 0, 0, false);
        emit ProposalCreated(proposalCount, description);
    }

    /**
     * @dev Vote on a proposal.
     * @param proposalId The ID of the proposal.
     * @param vote True for "For", False for "Against".
     */
    function vote(uint256 proposalId, bool vote) public {
        require(voters[msg.sender] == false, "Already voted");
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal already executed");

        if (vote) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }
        voters[msg.sender] = true;
        emit Voted(proposalId, msg.sender, vote);
    }

    /**
     * @dev Execute a proposal if it has more votes "For".
     * @param proposalId The ID of the proposal.
     */
    function executeProposal(uint256 proposalId) public {
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal already executed");
        require(proposal.votesFor > proposal.votesAgainst, "Not enough votes");

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }
}
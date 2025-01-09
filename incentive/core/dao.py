class DAOManager:
    def __init__(self):
        self.proposals = {}  # Stores proposals with their vote results
        self.votes = {}      # Tracks votes per proposal

    def create_proposal(self, proposal_id, description):
        """Creates a new proposal for community voting."""
        if proposal_id in self.proposals:
            return {"status": "failed", "message": "Proposal ID already exists"}
        self.proposals[proposal_id] = {"description": description, "votes": {"yes": 0, "no": 0}}
        return {"status": "success", "message": f"Proposal '{proposal_id}' created"}

    def vote(self, proposal_id, voter_id, vote):
        """Allows a user to vote on a proposal."""
        if proposal_id not in self.proposals:
            return {"status": "failed", "message": "Proposal not found"}
        if voter_id in self.votes.get(proposal_id, {}):
            return {"status": "failed", "message": "User has already voted"}

        if proposal_id not in self.votes:
            self.votes[proposal_id] = {}
        self.votes[proposal_id][voter_id] = vote

        if vote == "yes":
            self.proposals[proposal_id]["votes"]["yes"] += 1
        elif vote == "no":
            self.proposals[proposal_id]["votes"]["no"] += 1
        else:
            return {"status": "failed", "message": "Invalid vote value"}

        return {"status": "success", "message": "Vote recorded"}

    def execute_proposal(self, proposal_id):
        """Executes a proposal based on the vote results."""
        if proposal_id not in self.proposals:
            return {"status": "failed", "message": "Proposal not found"}

        results = self.proposals[proposal_id]["votes"]
        if results["yes"] > results["no"]:
            return {"status": "success", "message": f"Proposal '{proposal_id}' approved and executed"}
        return {"status": "failed", "message": f"Proposal '{proposal_id}' rejected"}
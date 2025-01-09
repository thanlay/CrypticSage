class IncentiveService:
    """
    Incentive mechanism to reward users with tokens for contributions.
    """

    def __init__(self):
        self.user_contributions = {}
        self.token_balance = {}

    def record_contribution(self, user_id: str, contribution: dict):
        """
        Record a user's contribution.
        :param user_id: User's unique identifier
        :param contribution: Details of the contribution
        """
        if user_id not in self.user_contributions:
            self.user_contributions[user_id] = []
        self.user_contributions[user_id].append(contribution)
        print(f"Contribution recorded for user {user_id}.")

    def issue_reward(self, user_id: str, amount: int):
        """
        Issue token rewards to a user.
        :param user_id: User's unique identifier
        :param amount: Amount of tokens to reward
        """
        self.token_balance[user_id] = self.token_balance.get(user_id, 0) + amount
        print(f"Reward of {amount} tokens issued to user {user_id}.")
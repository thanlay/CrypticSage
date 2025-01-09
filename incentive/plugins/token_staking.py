class TokenStakingPlugin:
    def __init__(self):
        self.stakes = {}

    def stake_tokens(self, user_id, amount):
        """Allows a user to stake tokens."""
        if amount <= 0:
            return {"status": "failed", "message": "Amount must be greater than 0"}
        self.stakes[user_id] = self.stakes.get(user_id, 0) + amount
        return {"status": "success", "message": f"Staked {amount} tokens"}

    def withdraw_stake(self, user_id, amount):
        """Allows a user to withdraw staked tokens."""
        if user_id not in self.stakes or self.stakes[user_id] < amount:
            return {"status": "failed", "message": "Insufficient stake"}
        self.stakes[user_id] -= amount
        return {"status": "success", "message": f"Withdrew {amount} tokens"}

    def calculate_rewards(self, user_id, reward_rate=0.05):
        """Calculates staking rewards for a user."""
        if user_id not in self.stakes:
            return {"status": "failed", "message": "No stakes found"}
        reward = self.stakes[user_id] * reward_rate
        return {"status": "success", "reward": reward}
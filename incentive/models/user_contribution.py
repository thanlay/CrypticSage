class UserContribution:
    """
    Represents a user's contribution to the system.
    """

    def __init__(self, user_id: str, contribution_amount: float):
        self.user_id = user_id
        self.contribution_amount = contribution_amount

    def __repr__(self):
        return f"UserContribution(user_id={self.user_id}, contribution_amount={self.contribution_amount})"
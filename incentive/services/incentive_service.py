from sqlalchemy.orm import Session
from models.database import UserContribution, UserBalance, Session as DatabaseSession
from core.logger import Logger
from datetime import datetime, timedelta
from typing import List, Dict

logger = Logger.setup_logger("IncentiveService")


class IncentiveService:
    """
    Service for managing contributions and rewards.
    """

    def __init__(self, db_session: Session = None):
        self.db_session = db_session or DatabaseSession()

    def record_contribution(self, user_id: str, contribution_type: str, amount: float):
        """
        Record a user's contribution with type and amount.
        :param user_id: User ID
        :param contribution_type: Type of contribution ("DATA", "COMPUTE", etc.)
        :param amount: Contribution amount
        :raises ValueError: if contribution amount is invalid
        """
        if amount <= 0:
            raise ValueError("Contribution amount must be positive.")
        if contribution_type not in ("DATA", "COMPUTE", "OTHER"):
            raise ValueError("Invalid contribution type.")

        contribution = UserContribution(
            user_id=user_id,
            contribution_type=contribution_type,
            contribution_amount=amount,
        )
        self.db_session.add(contribution)
        self.db_session.commit()

        logger.info(
            f"Recorded contribution: user={user_id}, type={contribution_type}, amount={amount}"
        )

    def get_user_contribution_summary(self, user_id: str, days: int = 30) -> Dict:
        """
        Get a summary of a user's contributions over a specified period.
        :param user_id: User ID
        :param days: Period in days for the summary
        :return: Contribution summary as a dictionary
        """
        cutoff_date = datetime.utcnow() - timedelta(days=days)
        contributions = (
            self.db_session.query(UserContribution)
            .filter(UserContribution.user_id == user_id)
            .filter(UserContribution.contribution_date >= cutoff_date)
            .all()
        )

        summary = {"DATA": 0.0, "COMPUTE": 0.0, "OTHER": 0.0}
        for contrib in contributions:
            summary[contrib.contribution_type] += contrib.contribution_amount

        return summary

    def calculate_rewards(self, reward_rates: Dict[str, float], days: int = 30) -> Dict:
        """
        Calculate rewards for all users based on contribution type and reward rates.
        :param reward_rates: Reward rate per contribution type (e.g., {"DATA": 0.1, "COMPUTE": 0.2})
        :param days: Period in days to consider for contributions
        :return: Dictionary of user IDs and their total rewards
        """
        cutoff_date = datetime.utcnow() - timedelta(days=days)
        contributions = (
            self.db_session.query(UserContribution)
            .filter(UserContribution.contribution_date >= cutoff_date)
            .all()
        )

        rewards = {}
        for contrib in contributions:
            if contrib.user_id not in rewards:
                rewards[contrib.user_id] = 0.0
            rewards[contrib.user_id] += (
                contrib.contribution_amount * reward_rates.get(contrib.contribution_type, 0)
            )

        logger.info(f"Calculated rewards for {len(rewards)} users.")
        return rewards
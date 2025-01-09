from sqlalchemy.orm import Session
from models.database import UserBalance, Session as DatabaseSession
from core.logger import Logger

logger = Logger.setup_logger("TokenService")


class TokenService:
    """
    Service for managing token transactions and balances.
    """

    def __init__(self, db_session: Session = None):
        self.db_session = db_session or DatabaseSession()

    def transfer_tokens(self, from_user: str, to_user: str, amount: float):
        """
        Transfer tokens between two users.
        :param from_user: Sender ID
        :param to_user: Receiver ID
        :param amount: Token amount to transfer
        :raises ValueError: if amount is invalid or if balance is insufficient
        """
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")

        from_balance = self._get_or_create_balance(from_user)
        to_balance = self._get_or_create_balance(to_user)

        if from_balance.balance < amount:
            raise ValueError("Insufficient balance for transfer.")

        from_balance.balance -= amount
        to_balance.balance += amount
        self.db_session.commit()

        logger.info(f"Transferred {amount} tokens from {from_user} to {to_user}.")

    def _get_or_create_balance(self, user_id: str):
        """
        Retrieve or create a user balance record.
        """
        user_balance = (
            self.db_session.query(UserBalance).filter_by(user_id=user_id).first()
        )

        if not user_balance:
            user_balance = UserBalance(user_id=user_id, balance=0)
            self.db_session.add(user_balance)
            self.db_session.commit()

        return user_balance
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from core.config import Config

Base = declarative_base()
DATABASE_URI = Config.get("DATABASE_URI")
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


def initialize_database():
    """
    Initialize the database by creating all necessary tables.
    """
    Base.metadata.create_all(engine)


class UserContribution(Base):
    """
    Tracks user contributions to the platform.
    """
    __tablename__ = "user_contributions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, nullable=False)
    contribution_type = Column(Enum("DATA", "COMPUTE", "OTHER"), nullable=False)  # Define contribution types
    contribution_amount = Column(Float, nullable=False)
    contribution_date = Column(DateTime, default=datetime.utcnow)  # Record contribution time

    def __repr__(self):
        return (
            f"<UserContribution(user_id={self.user_id}, contribution_type={self.contribution_type}, "
            f"contribution_amount={self.contribution_amount}, contribution_date={self.contribution_date})>"
        )


class UserBalance(Base):
    """
    Tracks user token balances.
    """
    __tablename__ = "user_balances"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, nullable=False, unique=True)
    balance = Column(Float, nullable=False)
    frozen_balance = Column(Float, default=0.0)  # Add frozen balance field for disputes

    def __repr__(self):
        return (
            f"<UserBalance(user_id={self.user_id}, balance={self.balance}, "
            f"frozen_balance={self.frozen_balance})>"
        )


class TokenTransaction(Base):
    """
    Records all token transactions for audit purposes.
    """
    __tablename__ = "token_transactions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    from_user = Column(String, nullable=False)
    to_user = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    transaction_date = Column(DateTime, default=datetime.utcnow)
    transaction_fee = Column(Float, default=0.0)  # Support transaction fees

    def __repr__(self):
        return (
            f"<TokenTransaction(from_user={self.from_user}, to_user={self.to_user}, "
            f"amount={self.amount}, transaction_date={self.transaction_date}, transaction_fee={self.transaction_fee})>"
        )
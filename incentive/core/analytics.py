import pandas as pd
import matplotlib.pyplot as plt
from database.models import TokenTransaction, UserActivity


class AnalyticsManager:
    def __init__(self, db_session):
        """Initialize analytics manager."""
        self.db_session = db_session

    def generate_daily_transaction_report(self):
        """Generate daily transaction summary."""
        transactions = self.db_session.query(TokenTransaction).all()
        data = [
            {"timestamp": t.timestamp, "amount": t.amount, "user_id": t.user_id}
            for t in transactions
        ]
        df = pd.DataFrame(data)
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        daily_summary = df.groupby(df["timestamp"].dt.date).sum()

        # Save the report to CSV
        daily_summary.to_csv("daily_transaction_report.csv")

        # Visualize the report with a plot
        daily_summary.plot(kind="bar", y="amount", title="Daily Transaction Summary")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.show()

        return daily_summary.to_dict()

    def generate_user_activity_report(self):
        """Generate a report of user contributions."""
        transactions = self.db_session.query(TokenTransaction).all()
        data = [
            {"user_id": t.user_id, "amount": t.amount} for t in transactions
        ]
        df = pd.DataFrame(data)
        user_summary = df.groupby("user_id").sum()

        # Save the report to CSV
        user_summary.to_csv("user_activity_report.csv")

        # Visualize the report
        user_summary.plot(kind="bar", y="amount", title="User Activity Summary")
        plt.xlabel("User ID")
        plt.ylabel("Total Amount Contributed")
        plt.show()

        return user_summary.to_dict()
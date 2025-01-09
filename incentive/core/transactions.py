class TransactionManager:
    def __init__(self):
        self.ledger = {}

    def transfer_tokens(self, sender, receiver, amount):
        """Transfers tokens between two accounts."""
        if self.ledger.get(sender, 0) < amount:
            return {"status": "failed", "message": "Insufficient balance"}
        self.ledger[sender] -= amount
        self.ledger[receiver] = self.ledger.get(receiver, 0) + amount
        return {"status": "success", "message": f"Transferred {amount} from {sender} to {receiver}"}

    def get_balance(self, user_id):
        """Fetches the balance of a user."""
        return {"user_id": user_id, "balance": self.ledger.get(user_id, 0)}
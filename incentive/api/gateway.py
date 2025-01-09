from flask import Flask, request, jsonify
from core.token import TokenManager
from core.dao import DAOManager
from core.logging import Logger

app = Flask(__name__)
logger = Logger()
token_manager = TokenManager()
dao_manager = DAOManager()

@app.route("/token/transfer", methods=["POST"])
def transfer_tokens():
    """Handles token transfer requests."""
    data = request.json
    sender = data.get("sender")
    receiver = data.get("receiver")
    amount = data.get("amount")

    if not sender or not receiver or not amount:
        logger.log_warning("Invalid token transfer request")
        return jsonify({"status": "failed", "message": "Invalid request"}), 400

    result = token_manager.transfer(sender, receiver, amount)
    logger.log_info(f"Token transfer: {result}")
    return jsonify(result)

@app.route("/dao/proposal", methods=["POST"])
def create_proposal():
    """Handles proposal creation for DAO."""
    data = request.json
    proposal_id = data.get("proposal_id")
    description = data.get("description")

    if not proposal_id or not description:
        logger.log_warning("Invalid proposal creation request")
        return jsonify({"status": "failed", "message": "Invalid request"}), 400

    result = dao_manager.create_proposal(proposal_id, description)
    logger.log_info(f"Proposal created: {result}")
    return jsonify(result)
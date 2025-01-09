from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def dashboard():
    """Render the dashboard page."""
    return render_template("dashboard.html", title="Dashboard")

@app.route("/api/transactions")
def get_transactions():
    """Get token transaction data."""
    transactions = TokenTransaction.query.all()
    data = [
        {"user_id": t.user_id, "amount": t.amount, "timestamp": t.timestamp}
        for t in transactions
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
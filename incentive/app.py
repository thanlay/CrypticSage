from flask import Flask, jsonify
from core.contribution import ContributionHandler
from core.rewards import RewardProcessor
from core.transactions import TransactionManager
from core.dao import DAOManager
from core.security import SecurityLayer
from plugins.plugin_manager import PluginManager

# Initialize Flask app
app = Flask(__name__)

# Initialize system modules
contribution_handler = ContributionHandler()
reward_processor = RewardProcessor()
transaction_manager = TransactionManager()
dao_manager = DAOManager()
security_layer = SecurityLayer()

# Initialize plugin system
plugin_manager = PluginManager()

@app.route("/")
def index():
    """Health check endpoint"""
    return jsonify({"status": "Token Incentive System running"}), 200

# Additional routes can be added here

if __name__ == "__main__":
    app.run(debug=True)
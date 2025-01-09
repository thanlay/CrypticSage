from services.automation_service import AutomationService
from services.blockchain_service import BlockchainService
from core.config import Config
from core.logger import Logger

logger = Logger.setup_logger("Main")

def main():
    logger.info("Starting Decentralized Automation System...")

    # Load configuration
    config = Config.all()
    logger.info(f"Loaded configuration: {config}")

    # Example: Automation Service
    automation_service = AutomationService()
    automation_service.define_rule(
        "rule1",
        condition=lambda: True,  # Example condition
        action=lambda: logger.info("Automation rule executed!")
    )
    automation_service.execute_rules()

    # Example: Blockchain Service
    blockchain_service = BlockchainService()
    try:
        result = blockchain_service.send_transaction("eth_getBlockByNumber", ["latest", True])
        logger.info(f"Blockchain data: {result}")
    except Exception as e:
        logger.error(f"Error interacting with blockchain: {e}")

if __name__ == "__main__":
    main()
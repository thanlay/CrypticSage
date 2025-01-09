from core.logger import Logger
from utils.helpers import validate_data

logger = Logger.setup_logger("AutomationService")

class AutomationService:
    """
    Handles automated decision-making and execution.
    """

    def __init__(self):
        self.rules = {}

    def define_rule(self, rule_id: str, condition: callable, action: callable):
        """
        Define an automation rule.
        :param rule_id: Unique ID for the rule
        :param condition: Callable that returns a boolean
        :param action: Callable to execute if the condition is met
        """
        validate_data({"rule_id": rule_id, "condition": condition, "action": action}, ["rule_id", "condition", "action"])
        self.rules[rule_id] = {"condition": condition, "action": action}
        logger.info(f"Rule {rule_id} has been defined.")

    def execute_rules(self):
        """
        Evaluate all rules and execute actions for those that meet conditions.
        """
        for rule_id, rule in self.rules.items():
            try:
                if rule["condition"]():
                    logger.info(f"Condition met for rule {rule_id}. Executing action.")
                    rule["action"]()
                else:
                    logger.debug(f"Condition not met for rule {rule_id}.")
            except Exception as e:
                logger.error(f"Failed to execute rule {rule_id}: {e}")
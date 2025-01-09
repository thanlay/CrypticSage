class CustomError(Exception):
    """
    Base class for custom exceptions.
    """
    def __init__(self, message):
        super().__init__(message)


class BlockchainError(CustomError):
    """
    Raised for blockchain-specific errors.
    """
    pass


class ValidationError(CustomError):
    """
    Raised for validation errors.
    """
    pass
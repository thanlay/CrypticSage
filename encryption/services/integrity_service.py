import hashlib

class IntegrityService:
    """
    Service for calculating and verifying data integrity using SHA-256 hashing.
    """

    @staticmethod
    def calculate_hash(data: str) -> str:
        """
        Calculate the SHA-256 hash of the input data.
        
        Args:
            data (str): The input data to hash.
        
        Returns:
            str: The hexadecimal SHA-256 hash of the input data.
        """
        if not isinstance(data, str):
            raise ValueError("Input data must be a string.")
        
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    @staticmethod
    def verify_data_integrity(data: str, stored_hash: str) -> bool:
        """
        Verify the integrity of the data by comparing it to a stored hash value.
        
        Args:
            data (str): The input data to verify.
            stored_hash (str): The expected SHA-256 hash value for the input data.
        
        Returns:
            bool: True if the calculated hash matches the stored hash, False otherwise.
        """
        if not isinstance(stored_hash, str):
            raise ValueError("Stored hash must be a string.")
        
        calculated_hash = IntegrityService.calculate_hash(data)
        return calculated_hash == stored_hash

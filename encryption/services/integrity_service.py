import hashlib

class IntegrityService:
    """
    Provides data integrity verification functionality.
    """

    @staticmethod
    def calculate_hash(data: str) -> str:
        """
        Calculate the SHA-256 hash value of the data.
        :param data: Input data
        :return: Hash value of the data
        """
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    @staticmethod
    def verify_data_integrity(data: str, stored_hash: str) -> bool:
        """
        Verify data integrity.
        :param data: Input data
        :param stored_hash: Stored hash value
        :return: Whether the hashes match
        """
        calculated_hash = IntegrityService.calculate_hash(data)
        return calculated_hash == stored_hash
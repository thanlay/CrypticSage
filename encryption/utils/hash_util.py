import hashlib

class HashUtil:
    """
    Provides functionality for calculating and verifying data hash values.
    """

    @staticmethod
    def calculate_hash(data: str) -> str:
        """
        Calculate the SHA256 hash value of the data.
        :param data: Original data
        :return: Hash value of the data
        """
        return hashlib.sha256(data.encode("utf-8")).hexdigest()

    @staticmethod
    def verify_data_integrity(data: str, stored_hash: str) -> bool:
        """
        Verify data integrity.
        :param data: Original data
        :param stored_hash: Stored hash value
        :return: Verification result
        """
        return HashUtil.calculate_hash(data) == stored_hash
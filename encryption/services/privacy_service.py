from zokrates_pycrypto.zokrates import ZoKrates

class PrivacyService:
    """
    Provides functionality for generating and verifying zero-knowledge proofs (ZKP).
    """

    def __init__(self, zokrates_path: str):
        """
        Initialize the ZoKrates service path.
        :param zokrates_path: Path to the ZoKrates installation directory
        """
        self.zokrates = ZoKrates(zokrates_path)

    def generate_proof(self, data: str, secret: str) -> str:
        """
        Generate a zero-knowledge proof using ZoKrates.
        :param data: Input data
        :param secret: Private key
        :return: Proof string
        """
        # Compile ZoKrates code
        self.zokrates.compile("def main(private field data, private field secret) -> bool { return data == secret; }")

        # Generate proof
        proof = self.zokrates.generate_proof(inputs=[data, secret])
        return proof

    def verify_proof(self, proof: str) -> bool:
        """
        Verify a zero-knowledge proof.
        :param proof: Zero-knowledge proof string
        :return: Verification result
        """
        result = self.zokrates.verify(proof)
        return result
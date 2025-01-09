from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64
import os

class EncryptionService:
    """
    提供数据加密和解密功能，确保传输和存储的数据安全。
    """

    def __init__(self):
        # 使用安全密钥管理服务模拟密钥的生成和存储。
        self.key = os.environ.get("ENCRYPTION_KEY", None)
        if not self.key:
            raise ValueError("请在环境变量中配置 ENCRYPTION_KEY")
        self.key = self.key[:32].encode("utf-8")  # 确保密钥长度为32字节

    def encrypt_data(self, data: str) -> str:
        """
        使用AES加密算法对数据进行加密。
        :param data: 需要加密的字符串
        :return: base64编码的加密数据
        """
        cipher = AES.new(self.key, AES.MODE_CBC)  # 初始化AES CBC模式
        iv = cipher.iv  # 生成随机IV
        encrypted_data = cipher.encrypt(pad(data.encode("utf-8"), AES.block_size))  # 加密并填充数据

        # 将IV和加密数据拼接，方便解密时分离
        encrypted_payload = base64.b64encode(iv + encrypted_data).decode("utf-8")
        return encrypted_payload

    def decrypt_data(self, encrypted_payload: str) -> str:
        """
        解密加密数据。
        :param encrypted_payload: base64编码的加密数据
        :return: 解密后的原始数据
        """
        raw_data = base64.b64decode(encrypted_payload)  # 解码base64数据
        iv = raw_data[:AES.block_size]  # 提取IV
        encrypted_data = raw_data[AES.block_size:]  # 提取加密数据

        cipher = AES.new(self.key, AES.MODE_CBC, iv)  # 使用相同的IV初始化解密
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)  # 解密并移除填充
        return decrypted_data.decode("utf-8")
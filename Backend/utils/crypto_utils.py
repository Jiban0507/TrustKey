from Crypto.Cipher import AES
import base64

# AES key must be 16, 24, or 32 bytes long
key = b"SixteenByteKey!!"   # 16 bytes

def encrypt_aadhaar(aadhaar_number: str) -> str:
    """
    Encrypt Aadhaar number using AES (EAX mode).
    Returns base64 encoded ciphertext.
    """
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(aadhaar_number.encode())
    return base64.b64encode(cipher.nonce + tag + ciphertext).decode()

def decrypt_aadhaar(encrypted_data: str) -> str:
    """
    Decrypt Aadhaar number using AES (EAX mode).
    Returns original Aadhaar number if tag verification passes.
    """
    raw = base64.b64decode(encrypted_data)
    nonce, tag, ciphertext = raw[:16], raw[16:32], raw[32:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode()
import base64
import requests
import hmac
import hashlib
import time

# Fetch key securely from GitHub
def fetch_key_from_github():
    url = "https://raw.githubusercontent.com/waelhadi/art1/main/w1213.txt"
    token = "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"

    headers = {
        "Authorization": f"Bearer {token}",  # التوكن المستخدم للوصول إلى المستودع
        "User-Agent": "SecureDecryptionClient"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        try:
            key = int(response.text.strip()) % 256  # تقليص المفتاح إلى نطاق صالح
            print("Key fetched successfully:", key)
            return key
        except ValueError:
            print("Error: Key fetched is not a valid integer.")
            raise Exception("Invalid key format")
    else:
        print(f"Failed to fetch key from GitHub. Status code: {response.status_code}")
        raise Exception("Failed to fetch key from GitHub")

# XOR decryption function
def xor_decrypt(data, key):
    return ''.join(chr(ord(char) ^ key) for char in data)

# Decrypt function for obfuscated code
def decrypt_function(encrypted_parts):
    key = fetch_key_from_github()
    decrypted_parts = []

    # Reverse the encryption layers
    for layer in range(3, 0, -1):
        print(f"Decrypting layer {layer}...")
        decrypted_layer = []

        for part in encrypted_parts:
            decoded_part = base64.b64decode(part).decode()
            decrypted_part = xor_decrypt(decoded_part, key)
            decrypted_layer.append(decrypted_part)

        encrypted_parts = decrypted_layer

    original_code = ''.join(encrypted_parts)
    print("Decryption completed successfully.")
    return original_code

import base64
import requests
import hmac
import hashlib
import time

# Fetch key securely from GitHub or a proxy server
def fetch_key_from_github():
    # استخدام رابط مُوقّع أو توثيق إضافي
    url = "https://raw.githubusercontent.com/waelhadi/art1/main/w1213.txt"
    token = "YOUR_SECURE_TOKEN"  # استبدلها برمز مصادقة مناسب إذا لزم الأمر

    headers = {
        "Authorization": f"Bearer {token}",
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

# Verify signature for added security
def verify_signature(data, signature, secret_key):
    computed_signature = hmac.new(secret_key.encode(), data.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(computed_signature, signature)

# XOR decryption function
def xor_decrypt(data, key):
    return ''.join(chr(ord(char) ^ key) for char in data)

# Decrypt function for obfuscated code
def decrypt_function(encrypted_parts, signature=None):
    secret_key = "YOUR_SECRET_KEY"  # يجب تخزين هذا المفتاح بأمان
    timestamp = str(int(time.time()))

    # التحقق من التوقيع إذا تم تمريره
    if signature:
        is_valid = verify_signature(timestamp, signature, secret_key)
        if not is_valid:
            raise Exception("Invalid signature detected")

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

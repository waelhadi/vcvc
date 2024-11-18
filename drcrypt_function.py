import base64
import requests
import zlib

# جلب المفتاح من GitHub
def fetch_key_from_github():
    url = "https://raw.githubusercontent.com/waelhadi/MFTAHTHFAER/refs/heads/main/TAHFER.txt"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            # تقليص المفتاح إلى النطاق [0-255]
            key = int(response.text.strip()) % 256
            print(f"Key fetched successfully: {key}")
            return key
        except ValueError:
            print(f"Error: Key fetched from {url} is not a valid integer. Content: {response.text.strip()}")
            exit(1)
    else:
        print(f"Failed to fetch key from GitHub. Status code: {response.status_code}")
        exit(1)

# دالة XOR لفك التشفير
def xor_decrypt(data, key):
    return ''.join(chr((ord(char) ^ key) % 256) for char in data)

# فك تشفير الكود المشفر
def decrypt_function(encrypted_parts):
    key = fetch_key_from_github()
    decrypted_parts = []

    # فك التشفير عبر الطبقات (3 طبقات عكس عملية التشفير)
    for layer in range(3, 0, -1):
        print(f"Decrypting layer {layer}...")
        decrypted_layer = []

        for part in encrypted_parts:
            # فك التشفير: فك الترميز Base64 ثم XOR
            decoded_part = base64.b64decode(part).decode()
            decrypted_part = xor_decrypt(decoded_part, key)
            decrypted_layer.append(decrypted_part)

        encrypted_parts = decrypted_layer

    original_code = ''.join(encrypted_parts)
    print("Decryption completed successfully.")
    return original_code

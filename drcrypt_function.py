import requests
import base64
import os

# دالة لجلب المفتاح من GitHub
def fetch_key_from_github():
    url = "https://raw.githubusercontent.com/waelhadi/art1/main/w1213.txt"
    headers = {
        "Authorization": f"token {os.getenv('GITHUB_TOKEN')}"  # إذا كان المستودع خاصًا
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        try:
            # تقليص المفتاح إلى النطاق 0-255
            key = int(response.text.strip()) % 256
            print("Key fetched successfully:", key)
            return key
        except ValueError:
            raise Exception("The key fetched from GitHub is not a valid integer.")
    else:
        print(f"Failed to fetch key from GitHub. Status code: {response.status_code}")
        raise Exception("Failed to fetch key from GitHub")

# فك التشفير باستخدام XOR
def xor_decrypt(data, key):
    return ''.join(chr(ord(char) ^ key) for char in data)

# دالة فك التشفير
def decrypt_function(encrypted_parts):
    key = fetch_key_from_github()  # جلب المفتاح
    print(f"Decrypting with key: {key}")
    decrypted_parts = []

    # فك تشفير الطبقات (من الطبقة 3 إلى الطبقة 1)
    for layer in range(3, 0, -1):
        print(f"Decrypting layer {layer}...")
        decrypted_layer = []

        for part in encrypted_parts:
            # فك Base64
            decoded_part = base64.b64decode(part).decode()
            # فك XOR باستخدام المفتاح
            decrypted_part = xor_decrypt(decoded_part, key)
            decrypted_layer.append(decrypted_part)

        encrypted_parts = decrypted_layer

    # تجميع النصوص الأصلية
    original_code = ''.join(encrypted_parts)
    print("Decryption completed successfully.")
    return original_code

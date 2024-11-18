import base64
import requests
import os

# فك التشفير باستخدام XOR
def xor_decrypt(data, key):
    return ''.join(chr(ord(char) ^ key) for char in data)

# الدالة لفك تشفير الطبقات المشفرة
def decrypt_function(encrypted_parts):
    # تحديد المفتاح
    key = fetch_key_from_github()  # اجلب المفتاح من GitHub
    decrypted_parts = []

    # فك تشفير الطبقات (من الطبقة 3 إلى الطبقة 1)
    for layer in range(3, 0, -1):
        print(f"Decrypting layer {layer}...")
        decrypted_layer = []

        for part in encrypted_parts:
            decoded_part = base64.b64decode(part).decode()  # فك Base64
            decrypted_part = xor_decrypt(decoded_part, key)  # فك XOR
            decrypted_layer.append(decrypted_part)

        encrypted_parts = decrypted_layer

    # إعادة النصوص الأصلية
    original_code = ''.join(encrypted_parts)
    print("Decryption completed successfully.")
    return original_code

# دالة لجلب المفتاح من GitHub مع تقليص المفتاح
def fetch_key_from_github():
    url = "https://raw.githubusercontent.com/waelhadi/art1/main/w1213.txt"  # رابط الملف الذي يحتوي على المفتاح
    headers = {
        "Authorization": f"token {os.getenv('GITHUB_TOKEN')}"  # استخدم GitHub Token إذا كان المستودع خاصًا
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        try:
            # تقليص المفتاح إلى النطاق 0-255 باستخدام % 256
            key = int(response.text.strip()) % 256
            print("Key fetched successfully:", key)
            return key
        except ValueError:
            raise Exception("The key fetched from GitHub is not a valid integer.")
    else:
        print(f"Failed to fetch key from GitHub. Status code: {response.status_code}")
        raise Exception("Failed to fetch key from GitHub")

import base64, requests

def fetch_key_from_github():
    url = "https://raw.githubusercontent.com/waelhadi/beko1/main/nasr.txt"  # رابط المفتاح
    response = requests.get(url)
    if response.status_code == 200:
        return int(response.text.strip())
    else:
        raise Exception("Failed to fetch key from GitHub")

def xor_decrypt(data, key):
    return ''.join(chr(ord(char) ^ key) for char in data)

def decrypt_function(encrypted_parts):
    parts = encrypted_parts
    key = fetch_key_from_github()  # جلب المفتاح مرة واحدة فقط

    for layer in range(10, 0, -1):  # عكس التشفير بدءاً من الطبقة الأخيرة
        decrypted_parts_layer = []

        for part in parts:
            # فك التشفير باستخدام المفتاح
            decoded_part = base64.b64decode(part).decode()
            decrypted_part = xor_decrypt(decoded_part, key)
            decrypted_parts_layer.append(decrypted_part)

        # تحديث المتغيرات للطبقة التالية
        parts = decrypted_parts_layer

    return ''.join(parts)  # إرجاع الكود الأصلي كنص واحد

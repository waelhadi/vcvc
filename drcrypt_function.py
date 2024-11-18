import base64

# فك التشفير باستخدام XOR
def xor_decrypt(data, key):
    return ''.join(chr(ord(char) ^ key) for char in data)

# الدالة لفك تشفير الطبقات المشفرة
def decrypt_function(encrypted_parts):
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

    original_code = ''.join(encrypted_parts)  # اجمع النصوص الأصلية
    print("Decryption completed successfully.")
    return original_code

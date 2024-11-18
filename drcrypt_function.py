import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt_data(data, key):
    key = key.ljust(32)[:32].encode()  # جعل المفتاح 32 بايت
    iv = b"your_fixed_iv_here"  # استخدم IV ثابت أو ديناميكي
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(data.encode(), AES.block_size))
    return base64.b64encode(iv + encrypted).decode()

def decrypt_data(encrypted_data, key):
    key = key.ljust(32)[:32].encode()
    encrypted_data = base64.b64decode(encrypted_data)
    iv = encrypted_data[:16]
    encrypted_content = encrypted_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted_content), AES.block_size)
    return decrypted.decode()

# Example usage
data = "Hello, World!"
key = "your-secret-key"

encrypted = encrypt_data(data, key)
print("Encrypted:", encrypted)

decrypted = decrypt_data(encrypted, key)
print("Decrypted:", decrypted)

import requests
import base64
import zlib

def fetch_decryption_function():
    # استبدل <username> و <repository> و <branch> بالقيم الصحيحة
    url = "https://raw.githubusercontent.com/<username>/<repository>/<branch>/drcrypt_function.py"
    github_token = "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"  # التوكن الجديد
    headers = {
        "Authorization": f"token {github_token}"
    }
    print(f"Fetching decryption function from: {url}")
    try:
        response = requests.get(url, headers=headers)
        print(f"Response status code: {response.status_code}")
        if response.status_code == 200:
            print("Decryption function fetched successfully.")
            print(f"Function content:\n{response.text[:500]}")  # طباعة أول 500 حرف من المحتوى
            exec(response.text, globals())  # تنفيذ محتوى الدالة
        else:
            print(f"Failed to fetch decryption function. Status code: {response.status_code}")
            print(f"Response text: {response.text}")
            raise Exception("Failed to fetch decryption function from GitHub.")
    except Exception as e:
        print(f"Error occurred while fetching decryption function: {e}")
        raise

def decrypt_function(encrypted_parts):
    key = fetch_key_from_github()  # يجب أن تكون دالة جلب المفتاح موجودة
    print(f"Using decryption key: {key}")
    decrypted_parts = []

    # فك تشفير الطبقات من الطبقة 3 إلى الطبقة 1
    for layer in range(3, 0, -1):
        print(f"Decrypting layer {layer}...")
        decrypted_layer = []

        for part in encrypted_parts:
            decoded_part = base64.b64decode(part).decode()  # فك Base64
            decrypted_part = xor_decrypt(decoded_part, key)  # فك XOR
            decrypted_layer.append(decrypted_part)

        encrypted_parts = decrypted_layer

    original_code = ''.join(encrypted_parts)
    print("Decryption completed successfully.")
    return original_code

def xor_decrypt(data, key):
    return ''.join(chr(ord(char) ^ key) for char in data)

def fetch_key_from_github():
    # استبدل <username> و <repository> و <branch> بالقيم الصحيحة
    url = "https://raw.githubusercontent.com/<username>/<repository>/<branch>/w1213.txt"
    github_token = "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"  # التوكن الجديد
    headers = {
        "Authorization": f"token {github_token}"
    }
    print(f"Fetching key from: {url}")
    response = requests.get(url, headers=headers)
    print(f"Response status code: {response.status_code}")
    if response.status_code == 200:
        try:
            key = int(response.text.strip()) % 256  # تقليص المفتاح إلى النطاق 0-255
            print(f"Key fetched successfully: {key}")
            return key
        except ValueError:
            print("The key fetched is not a valid integer.")
            raise Exception("The key fetched is not a valid integer.")
    else:
        print(f"Failed to fetch key from GitHub. Response text: {response.text}")
        raise Exception("Failed to fetch key from GitHub.")

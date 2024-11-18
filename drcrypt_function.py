import base64
import requests

# Fetch key from GitHub
def fetch_key_from_github():
    url = "https://raw.githubusercontent.com/waelhadi/MFTAHTHFAER/refs/heads/main/TAHFER.txt"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            key = int(response.text.strip()) % 256  # Reduce key to valid range
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

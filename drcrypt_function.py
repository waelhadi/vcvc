from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

# Function to decrypt data using XOR
def xor_decrypt(data, key):
    return ''.join(chr(ord(char) ^ key) for char in data)

# Flask route for decryption
@app.route('/decrypt', methods=['POST'])
def decrypt():
    try:
        # Get the JSON input
        content = request.json
        encrypted_parts = content.get('encrypted_parts')
        key = 123  # Replace this with your key

        # Decrypt the data layer by layer
        decrypted_parts = []
        for layer in range(3, 0, -1):
            decrypted_layer = []
            for part in encrypted_parts:
                decoded_part = base64.b64decode(part).decode()
                decrypted_part = xor_decrypt(decoded_part, key)
                decrypted_layer.append(decrypted_part)
            encrypted_parts = decrypted_layer

        # Return the decrypted code
        return jsonify({"decrypted_code": ''.join(encrypted_parts)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

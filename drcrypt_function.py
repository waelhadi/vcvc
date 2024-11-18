import requests

def fetch_decryption_function():
    # الرابط الصحيح للمستودع
    url = "https://raw.githubusercontent.com/waelhadi/vcvc/main/drcrypt_function.py"
    # التوكن الخاص بك
    token = "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"

    # الرؤوس المطلوبة لإرسال التوكن
    headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": "SecureDecryptionClient"
    }

    print(f"Fetching decryption function from: {url}")
    response = requests.get(url, headers=headers)

    # التحقق من حالة الاستجابة
    if response.status_code == 200:
        exec(response.text, globals())
        print("Decryption function loaded successfully.")
    else:
        print(f"Failed to fetch decryption function. Status code: {response.status_code}")
        print(f"Response text: {response.text[:500]}")  # طباعة أول 500 حرف لفهم المشكلة
        raise Exception("Failed to fetch decryption function from GitHub")

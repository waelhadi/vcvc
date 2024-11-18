def fetch_key_from_github():
    url = "https://raw.githubusercontent.com/waelhadi/art1/main/w1213.txt"
    headers = {
        "Authorization": f"token {os.getenv('GITHUB_TOKEN')}"  # استخدم Token إذا كان المستودع خاصًا
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        try:
            key = int(response.text.strip()) % 256  # تقليص المفتاح إلى النطاق 0-255
            print("Key fetched successfully:", key)
            return key
        except ValueError:
            raise Exception("The key fetched from GitHub is not a valid integer.")
    else:
        print(f"Failed to fetch key from GitHub. Status code: {response.status_code}")
        raise Exception("Failed to fetch key from GitHub")

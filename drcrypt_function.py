import requests

# رابط الملف الذي تريد الوصول إليه
url = "https://raw.githubusercontent.com/username/repository/branch/path/to/file.py"

# إعداد الرأس مع المفتاح
headers = {
    "Authorization": "token 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"
}

# إرسال الطلب
response = requests.get(url, headers=headers)

# التحقق من النتيجة
if response.status_code == 200:
    print("File fetched successfully.")
    print(response.text)  # عرض محتوى الملف
else:
    print(f"Failed to fetch file. Status code: {response.status_code}")

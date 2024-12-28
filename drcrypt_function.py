import zlib
import sys

def xor_decrypt(data, key):
    """فك تشفير باستخدام XOR"""
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

def decompress_data(data):
    """فك ضغط البيانات"""
    try:
        # التحقق من أن البيانات بتنسيق هيكساديسيمال
        if not all(c in "0123456789abcdef" for c in data.lower()):
            raise ValueError("البيانات ليست بتنسيق هيكساديسيمال صالح.")
        return zlib.decompress(bytes.fromhex(data)).decode('utf-8')
    except zlib.error as e:
        print(f"خطأ أثناء فك ضغط البيانات: {e}")
        raise
    except ValueError as e:
        print(f"خطأ في التنسيق: {e}")
        raise

def main():
    # قراءة البيانات والمفتاح من سطر الأوامر
    encrypted_data = sys.argv[1]
    key = sys.argv[2]

    # فك التشفير
    decrypted = xor_decrypt(decompress_data(encrypted_data), key)
    print("النص المفكوك:", decrypted)

if __name__ == "__main__":
    main()

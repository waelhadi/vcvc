import json
import tempfile
import os
import importlib.util

def custom_symbol_decrypt(encrypted):
    """فك التشفير باستخدام الرموز المخصصة"""
    symbol = "■"  # نفس الرمز المستخدم في التشفير
    decrypted = []
    for enc_char in encrypted:
        char_code = len(enc_char)
        decrypted.append(chr(char_code))
    return "".join(decrypted)

def run_decrypted_code(decrypted_code):
    """تشغيل الكود المفكوك"""
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as temp_file:
        temp_file.write(decrypted_code.encode())
        temp_filename = temp_file.name

    try:
        # استيراد الكود وتنفيذه
        spec = importlib.util.spec_from_file_location("decrypted_module", temp_filename)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    finally:
        os.remove(temp_filename)

from ..utils import text_processor

def encrypt(plaintext, key):
    normalized_text = text_processor.normalize_text(plaintext)
    encrypted_text = ""
    
    for char in normalized_text:
        if 'A' <= char <= 'Z':
            char_num = ord(char) - ord('A')
            encrypted_num = (char_num + key) % 26
            encrypted_char = chr(encrypted_num + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
            
    return encrypted_text

def decrypt(ciphertext, key):
    # Encryption with a negative key.
    return encrypt(ciphertext, -key)

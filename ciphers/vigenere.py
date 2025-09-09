from ..utils import text_processor

def encrypt(plaintext, key):
    normalized_text = text_processor.normalize_text(plaintext)
    # Key is also normalized and spaces are removed.
    processed_key = text_processor.normalize_text(key).replace(' ', '')
    
    encrypted_text = ""
    key_index = 0
    
    for char in normalized_text:
        if 'A' <= char <= 'Z':
            key_char = processed_key[key_index % len(processed_key)]
            shift = ord(key_char) - ord('A')
            
            char_num = ord(char) - ord('A')
            encrypted_num = (char_num + shift) % 26
            encrypted_char = chr(encrypted_num + ord('A'))
            
            encrypted_text += encrypted_char
            key_index += 1
        else:
            encrypted_text += char
            
    return encrypted_text

def decrypt(ciphertext, key):
    processed_key = text_processor.normalize_text(key).replace(' ', '')

    decrypted_text = ""
    key_index = 0
    
    # Uppercase for calculations
    for char in ciphertext.upper():
        if 'A' <= char <= 'Z':
            key_char = processed_key[key_index % len(processed_key)]
            shift = ord(key_char) - ord('A')
            
            char_num = ord(char) - ord('A')
            decrypted_num = (char_num - shift + 26) % 26
            decrypted_char = chr(decrypted_num + ord('A'))
            
            decrypted_text += decrypted_char
            key_index += 1
        else:
            decrypted_text += char
            
    return decrypted_text

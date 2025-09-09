import collections
from ..ciphers import vigenere
from ..utils import language_stats

def _calculate_ic(text):
    """Calculates the Index of Coincidence for a given text."""
    text = ''.join(filter(str.isalpha, text.upper()))
    n = len(text)
    
    if n < 2:
        return 0.0
        
    frequencies = collections.Counter(text)
    
    numerator = sum(count * (count - 1) for count in frequencies.values())
    ic = numerator / (n * (n - 1))
    
    return ic

def run_attack(ciphertext):
    """
    Attack on a Vigenère cipher by first estimating the key
    length using the Index of Coincidence, then breaking each column using
    frequency analysis.
    """
    text_only_letters = ''.join(filter(str.isalpha, ciphertext.upper()))
    
    print("--- 1. Estimating Key Length via Index of Coincidence ---")
    
    ics_by_length = {}
    
    for key_length in range(2, 16):
        columns = [''] * key_length
        for i, char in enumerate(text_only_letters):
            columns[i % key_length] += char
        
        avg_ic = sum(_calculate_ic(col) for col in columns) / key_length
        ics_by_length[key_length] = avg_ic
        print(f"Tested Key Length: {key_length:02d} | Average IC: {avg_ic:.4f}")

    # The best key length is the one whose average IC is closest to the language's IC.
    best_length = min(ics_by_length, key=lambda k: abs(ics_by_length[k] - language_stats.PORTUGUESE_IC))
    
    print(f"\nClosest IC match found for key length: {best_length}\n")
    
    print(f"--- 2. Breaking Columns via Frequency Analysis ---")
    
    final_columns = [''] * best_length
    for i, char in enumerate(text_only_letters):
        final_columns[i % best_length] += char
        
    found_key = ""
    MOST_COMMON_PT_LETTER = 'A'

    for i, column in enumerate(final_columns):
        if not column:
            continue
        
        col_frequencies = collections.Counter(column)
        most_frequent_in_col = col_frequencies.most_common(1)[0][0]
        
        shift = (ord(most_frequent_in_col) - ord(MOST_COMMON_PT_LETTER)) % 26
        key_char = chr(shift + ord('A'))
        found_key += key_char
        print(f"Column {i+1}: Most frequent is '{most_frequent_in_col}'. Inferred key char: '{key_char}'")
        
    print(f"\n--- 3. Reconstructing Key and Decrypting ---")
    print(f"Found Key: {found_key}")
    
    plaintext = vigenere.decrypt(ciphertext, found_key)
    print(f"Decrypted Plaintext: {plaintext}")
    
    return found_key, plaintext

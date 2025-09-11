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
    pt_freqs = language_stats.PORTUGUESE_FREQUENCIES
    pt_freq_vector = [pt_freqs.get(chr(ord('A')+j), 0) for j in range(26)]

    for i, column in enumerate(final_columns):
        if not column:
            continue
        col_len = len(column)
        col_freqs = collections.Counter(column)
        col_freq_vector = [col_freqs.get(chr(ord('A')+j), 0)/col_len for j in range(26)]
        best_shift = 0
        best_score = float('-inf')
        # Testa todos os deslocamentos possíveis
        for shift in range(26):
            shifted = col_freq_vector[-shift:] + col_freq_vector[:-shift]
            # Score: produto escalar (correlação)
            score = sum(a*b for a, b in zip(shifted, pt_freq_vector))
            if score > best_score:
                best_score = score
                best_shift = shift
        key_char = chr(best_shift + ord('A'))
        found_key += key_char
        print(f"Column {i+1}: Best shift is {best_shift}. Inferred key char: '{key_char}'")
        
    print(f"\n--- 3. Reconstructing Key and Decrypting ---")
    print(f"Found Key: {found_key}")
    
    plaintext = vigenere.decrypt(ciphertext, found_key)
    print(f"Decrypted Plaintext: {plaintext}")
    
    return found_key, plaintext

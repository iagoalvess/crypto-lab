import collections
from ..ciphers import caesar

def run_attack(ciphertext):
    """
    Frequency analysis attack on a Caesar cipher. It finds the most
    frequent letter and assumes it corresponds to 'A' or 'E' in Portuguese.
    """
    text_only_letters = ''.join(filter(str.isalpha, ciphertext))

    frequencies = collections.Counter(text_only_letters)
    sorted_frequencies = frequencies.most_common()

    print("--- Ciphertext Letter Frequencies ---")
    for letter, count in sorted_frequencies:
        print(f"Letter: {letter} | Count: {count}")
    print("-------------------------------------\n")
    
    most_frequent_encrypted_letter = sorted_frequencies[0][0]
    print(f"Most frequent letter in ciphertext is: '{most_frequent_encrypted_letter}'\n")

    portuguese_common_letters = ['A', 'E']
    
    for pt_letter in portuguese_common_letters:
        print(f"--- Testing hypothesis: '{most_frequent_encrypted_letter}' corresponds to '{pt_letter}' ---")
        
        # k = (encrypted_char_ord - plain_char_ord) % 26
        estimated_key = (ord(most_frequent_encrypted_letter) - ord(pt_letter)) % 26
        
        print(f"Estimated Key (k): {estimated_key}")
        
        decrypted_text = caesar.decrypt(ciphertext, estimated_key)
        print(f"Decrypted text: {decrypted_text}\n")

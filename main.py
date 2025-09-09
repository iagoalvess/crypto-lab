import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crypto_lab.ciphers import caesar, vigenere
from crypto_lab.attacks import caesar_brute_force, caesar_frequency_analysis, vigenere_analysis

def run_task_1():
    """Runs and displays the results for Task 1: Caesar Cipher Implementation."""
    print("--- Task 1: Caesar Cipher Implementation ---")
    plaintext = "SEGURANCA DA INFORMACAO E IMPORTANTE"
    key = 3
    print(f"Plaintext: {plaintext}")
    print(f"Key (k): {key}\n")
    
    encrypted = caesar.encrypt(plaintext, key)
    print(f"Encrypted: {encrypted}")
    
    decrypted = caesar.decrypt(encrypted, key)
    print(f"Decrypted: {decrypted}\n")

def run_task_2():
    """Runs and displays the results for Task 2: Caesar Brute-Force Attack."""
    print("\n--- Task 2: Caesar Brute-Force Attack ---")
    ciphertext = "SXBN N DV XCRVX NBCDMJWCN MJ DOVP"
    print(f"Ciphertext: {ciphertext}\n")
    
    candidates = caesar_brute_force.run_attack(ciphertext)
    
    print("Top 5 candidates:")
    for i in range(min(5, len(candidates))):
        candidate = candidates[i]
        print(f"Key (k) = {candidate['key']:02d} | Score = {candidate['score']} | Text: {candidate['text']}")

    best_candidate = candidates[0]
    print(f"\nBest Guess:")
    print(f"Found Key (k): {best_candidate['key']}")
    print(f"Plaintext: {best_candidate['text']}\n")

def run_task_3():
    """Runs and displays the results for Task 3: Caesar Frequency Analysis."""
    print("\n--- Task 3: Caesar Frequency Analysis Attack ---")
    ciphertext = "RKRHLV UV UZTZFERIZF V VWZTRQ TFEKIR JVEYRJ WIRTRJ"
    print(f"Ciphertext: {ciphertext}\n")
    caesar_frequency_analysis.run_attack(ciphertext)

def run_task_4():
    """Runs and displays the results for Task 4: Vigenère Cipher Implementation."""
    print("\n--- Task 4: Vigenère Cipher Implementation ---")
    plaintext = "CIFRA DE VIGENERE E UM POUCO MAIS FORTE"
    key = "SEGURO"
    print(f"Plaintext: {plaintext}")
    print(f"Key: {key}\n")
    
    encrypted = vigenere.encrypt(plaintext, key)
    print(f"Encrypted: {encrypted}")
    
    decrypted = vigenere.decrypt(encrypted, key)
    print(f"Decrypted: {decrypted}\n")

def run_task_5():
    """Runs and displays the results for Task 5: Vigenère Cipher Attack."""
    print("\n--- Task 5: Vigenère Cipher Attack ---")
    ciphertext = "ECXPFI WO QQYFO LX JWOXBSZX"
    print(f"Ciphertext: {ciphertext}\n")
    vigenere_analysis.run_attack(ciphertext)

def run_task_5_extended_test():
    """Runs the Vigenère attack on a longer ciphertext to prove the statistical hypothesis."""
    print("\n--- Task 5 (Extended Test with Longer Ciphertext) ---")
    # Plaintext: "A CRIPTOGRAFIA CLASSICA E UM CAMPO FASCINANTE DA HISTORIA DA COMPUTACAO E DA SEGURANCA DA INFORMACAO"
    # Key: "SECRETO"
    ciphertext = "SGTZTM C IASQVGUVWMG C WMK GECRS JCUAUDRPNGF HC JQUVQTCFC GECRSWVGGEQ C FC UCYWTCPEGFC GPHQTOCGEQ"
    print(f"Ciphertext: {ciphertext}\n")
    vigenere_analysis.run_attack(ciphertext)

if __name__ == "__main__":
    run_task_1()
    run_task_2()
    run_task_3()
    run_task_4()
    run_task_5()
    run_task_5_extended_test()


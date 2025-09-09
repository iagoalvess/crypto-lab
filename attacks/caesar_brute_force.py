from ..ciphers import caesar
from ..utils import language_stats

def run_attack(ciphertext):
    """
    Attack on a Caesar cipher by testing all possible keys
    and scoring the results based on the frequency of common Portuguese words.
    """
    candidates = []
    
    for k in range(1, 26):
        decrypted_text = caesar.decrypt(ciphertext, k)
        
        score = 0
        words_in_text = decrypted_text.upper().split(' ')
        for word in words_in_text:
            if word in language_stats.PORTUGUESE_COMMON_WORDS:
                score += 1
        
        candidates.append({'key': k, 'text': decrypted_text, 'score': score})

    ranked_candidates = sorted(candidates, key=lambda x: x['score'], reverse=True)
    
    return ranked_candidates

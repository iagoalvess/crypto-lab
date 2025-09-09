def normalize_text(text):
    """
    Normalizes text by converting to uppercase, removing common accents,
    and filtering to keep only letters (A-Z) and spaces.
    """
    text = text.upper()
    
    replacements = {
        'Á': 'A', 'À': 'A', 'Ã': 'A', 'Ä': 'A',
        'É': 'E', 'È': 'E', 'Ê': 'E',
        'Í': 'I', 'Ì': 'I', 'Î': 'I',
        'Ó': 'O', 'Ò': 'O', 'Õ': 'O', 'Ö': 'O',
        'Ú': 'U', 'Ù': 'U', 'Û': 'U',
        'Ç': 'C'
    }
    for accented, base in replacements.items():
        text = text.replace(accented, base)
    
    normalized_text = ""
    for char in text:
        if 'A' <= char <= 'Z' or char == ' ':
            normalized_text += char
            
    return normalized_text

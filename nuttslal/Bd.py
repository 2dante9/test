# Encryption function
def encrypt(text):
    # All letters of the alphabet array
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # The positions of the letters in alphabet
    flip = {char: index for index, char in enumerate(alphabet)}

    encrypted_text = ''
    for char in text:
        if char.isalpha():
            # Encryption happens here
            encrypted_text += alphabet[(flip[char.upper()] + 5) % 26]
        else:
            # If the character is not a letter, keep it unchanged
            encrypted_text += char
    return encrypted_text

# Decryption function
def decrypt(encrypted_text):
    # All letters of the alphabet array
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # The positions of the letters in alphabet
    flip = {char: index for index, char in enumerate(alphabet)}

    decrypted_text = ''
    for char in encrypted_text:
        if char.isalpha():
            # Decryption happens here
            decrypted_text += alphabet[(26 + flip[char.upper()] - 5) % 26]
        else:
            # If the character is not a letter, keep it unchanged
            decrypted_text += char
    return decrypted_text

# Example usage
encrypted_text = encrypt('ENCRIPTCODE')
print("Encrypted:", encrypted_text)

decrypted_text = decrypt('DECRIPTCODE')
print("Decrypted:", decrypted_text)

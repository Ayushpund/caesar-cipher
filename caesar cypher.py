def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():  # Check if character is alphabet
            # Determine shift direction based on mode
            if mode == 'encrypt':
                shifted_char = chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            elif mode == 'decrypt':
                shifted_char = chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                raise ValueError("Mode must be 'encrypt' or 'decrypt'.")
            result += shifted_char
        else:
            result += char
    return result

# Example usage:
text = "AYUSH"
shift = 3
encrypted_text = caesar_cipher(text.upper(), shift, 'encrypt')
print("Encrypted text:", encrypted_text)

decrypted_text = caesar_cipher(encrypted_text, shift, 'decrypt')
print("Decrypted text:", decrypted_text)

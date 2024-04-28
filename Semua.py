def caesar_encrypt(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a')) if char.islower() else chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def all_caesar_shifts(text):
    all_shifts_encrypted = []
    for shift in range(26):
        encrypted_text = caesar_encrypt(text, shift)
        all_shifts_encrypted.append(encrypted_text)
    return all_shifts_encrypted

# Contoh penggunaan:
plaintext = "BionicBeaver18.04.6"
all_encrypted_texts = all_caesar_shifts(plaintext)
for i, encrypted_text in enumerate(all_encrypted_texts):
    print(encrypted_text)

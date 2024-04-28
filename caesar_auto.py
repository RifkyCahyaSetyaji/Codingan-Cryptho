def caesar_cipher_auto_shift(text):
    result = ""
    for shift in range(1, 26):  # Coba semua kemungkinan pergeseran
        decrypted_text = ""
        for char in text:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                decrypted_text += chr((ord(char) - start - shift) % 26 + start)
            else:
                decrypted_text += char

        # Lakukan pengecekan atau output
        print(f"Shift {shift}: {decrypted_text}")

# Contoh penggunaan
ciphertext = "cduhdbdqhdbmzsrhrrzenkdudkdgsgshvcdrrdqolhxktqslhxzrnsduzgh"
caesar_cipher_auto_shift(ciphertext)
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        # Periksa apakah karakter merupakan huruf alfabet
        if char.isalpha():
            # Tetapkan batasan atas berdasarkan huruf besar atau kecil
            if char.isupper():
                ascii_offset = ord('A')
            else:
                ascii_offset = ord('a')
            # Geser huruf sesuai dengan nilai pergeseran
            shifted = (ord(char) - ascii_offset + shift) % 26 + ascii_offset
            result += chr(shifted)
        else:
            # Jika bukan huruf alfabet, tambahkan karakter aslinya
            result += char
    return result

# Contoh penggunaan
text = "Ebqbulbo 11"
shift = 1
encrypted_text = caesar_cipher(text, shift)
print("Teks Enkripsi:", encrypted_text)

# Dekripsi dengan menggeser ke arah yang berlawanan
decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Teks Dekripsi:", decrypted_text)



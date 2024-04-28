def backward_shift(text, shift):
    shifted_text = ''
    for char in text:
        if char.isalpha():
            shifted_text += shift_char(char, shift, backward=True)
        elif char.isdigit():
            shifted_text += shift_digit(char, shift, backward=True)
        else:
            shifted_text += char
    return shifted_text

def shift_char(char, shift, backward=False):
    ascii_offset = ord('a') if char.islower() else ord('A')
    shift = shift if not backward else -shift
    shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
    return shifted_char

def shift_digit(digit, shift, backward=False):
    shift = shift if not backward else -shift
    shifted_digit = str((int(digit) + shift) % 10)
    return shifted_digit

def all_shifts(text):
    for shift in range(1, 26):
        shifted_text = backward_shift(text, shift)
        print(f"Shift {shift}: {shifted_text}")

# Contoh penggunaan
original_text = "cvpbPGS{P7e1S_54I35_71Z3}"
print("Original text:", original_text)

print("\nAll shifts:")
all_shifts(original_text)

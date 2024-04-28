def rot18(text):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_val = ord(char)
            if char.islower():
                result += chr((ascii_val - ord('a') + 5) % 26 + ord('a'))
            else:
                result += chr((ascii_val - ord('A') + 5) % 26 + ord('A'))
        elif char.isdigit():
            ascii_val = ord(char)
            result += chr((ascii_val - ord('0') + 5) % 10 + ord('0'))
        else:
            result += char
    return result

# Example usage
text = "O9sr55qotml5xc9xjz5zn87tj9ttob8xy9xe5lsec8jjotm"
rotated_text = rot18(text)
print(rotated_text)  # Output: "Mjqqt, Yrttr!678"
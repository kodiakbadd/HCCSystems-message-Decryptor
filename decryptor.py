"""
HCC Systems Message Decryptor

A Python application to decrypt simple ciphers used in puzzles.
Supports Caesar, Vigenère, and Atbash ciphers.
"""

import string

def caesar_decrypt(text, shift):
    """
    Decrypt a Caesar cipher with the given shift.
    """
    result = []
    for char in text:
        if char.isupper():
            result.append(chr((ord(char) - shift - 65) % 26 + 65))
        elif char.islower():
            result.append(chr((ord(char) - shift - 97) % 26 + 97))
        else:
            result.append(char)
    return ''.join(result)

def vigenere_decrypt(text, key):
    """
    Decrypt a Vigenère cipher with the given key.
    """
    key = key.upper()
    key_len = len(key)
    result = []
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % key_len]) - 65
            if char.isupper():
                result.append(chr((ord(char) - shift - 65) % 26 + 65))
            else:
                result.append(chr((ord(char) - shift - 97) % 26 + 97))
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)

def atbash_decrypt(text):
    """
    Decrypt an Atbash cipher.
    """
    result = []
    for char in text:
        if char.isupper():
            result.append(chr(155 - ord(char)))
        elif char.islower():
            result.append(chr(219 - ord(char)))
        else:
            result.append(char)
    return ''.join(result)

def main():
    print("Welcome to HCC Systems Message Decryptor!")
    print("Supported ciphers: Caesar, Vigenère, Atbash")
    print("Enter 'quit' to exit.\n")

    while True:
        cipher = input("Enter cipher type (Caesar/Vigenere/Atbash): ").strip().lower()
        if cipher == 'quit':
            break
        elif cipher == 'caesar':
            try:
                shift = int(input("Enter shift value: "))
                message = input("Enter encrypted message: ")
                decrypted = caesar_decrypt(message, shift)
                print(f"Decrypted message: {decrypted}\n")
            except ValueError:
                print("Invalid shift value. Please enter an integer.\n")
        elif cipher == 'vigenere':
            key = input("Enter key: ").strip()
            if not key.isalpha():
                print("Key must contain only letters.\n")
                continue
            message = input("Enter encrypted message: ")
            decrypted = vigenere_decrypt(message, key)
            print(f"Decrypted message: {decrypted}\n")
        elif cipher == 'atbash':
            message = input("Enter encrypted message: ")
            decrypted = atbash_decrypt(message)
            print(f"Decrypted message: {decrypted}\n")
        else:
            print("Unsupported cipher. Try again.\n")

if __name__ == "__main__":
    main()
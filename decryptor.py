"""
HCC Systems Message Encryptor/Decryptor

A Python application to encrypt or decrypt simple ciphers used in puzzles.
Supports Caesar, Atbash, Simple Substitution, Vigenère, Transposition,
Playfair, Rail Fence, and Homophonic Substitution ciphers.
"""

import string

def caesar_cipher(text, shift, encrypt=True):
    """
    Encrypt or decrypt a Caesar cipher with the given shift.
    Set encrypt=True for encryption, False for decryption.
    """
    if not encrypt:
        shift = -shift
    result = []
    for char in text:
        if char.isupper():
            result.append(chr((ord(char) - 65 + shift) % 26 + 65))
        elif char.islower():
            result.append(chr((ord(char) - 97 + shift) % 26 + 97))
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

def simple_substitution_decrypt(text, mapping_str):
    """
    Decrypt a simple substitution cipher.
    mapping_str should be a string of 26 letters representing the plaintext
    alphabet in the order of the ciphertext alphabet (A maps to mapping_str[0], etc.).
    """
    if len(mapping_str) != 26:
        raise ValueError("Mapping must be exactly 26 characters.")
    mapping = {}
    for i, c in enumerate(string.ascii_uppercase):
        mapping[c] = mapping_str[i].upper()
    for i, c in enumerate(string.ascii_lowercase):
        mapping[c] = mapping_str[i].lower()
    result = []
    for char in text:
        if char in mapping:
            result.append(mapping[char])
        else:
            result.append(char)
    return ''.join(result)

def vigenere_encrypt(text, key):
    """
    Encrypt a Vigenère cipher with the given key.
    """
    key = key.upper()
    key_len = len(key)
    result = []
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % key_len]) - 65
            if char.isupper():
                result.append(chr((ord(char) - 65 + shift) % 26 + 65))
            else:
                result.append(chr((ord(char) - 97 + shift) % 26 + 97))
            key_index += 1
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

def transposition_decrypt(text, num_columns):
    """
    Decrypt a columnar transposition cipher with the given number of columns.
    Assumes text is written row by row, read column by column.
    """
    num_columns = int(num_columns)
    text = text.replace(' ', '')
    length = len(text)
    num_rows = (length + num_columns - 1) // num_columns
    grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]
    idx = 0
    for col in range(num_columns):
        for row in range(num_rows):
            if idx < length:
                grid[row][col] = text[idx]
                idx += 1
    result = []
    for row in range(num_rows):
        for col in range(num_columns):
            if grid[row][col]:
                result.append(grid[row][col])
    return ''.join(result)

def playfair_decrypt(text, key):
    """
    Decrypt a Playfair cipher with the given key.
    """
    key = key.upper().replace('J', 'I')
    seen = set()
    grid = []
    for char in key + string.ascii_uppercase:
        if char not in seen and char != 'J':
            grid.append(char)
            seen.add(char)
    pos = {}
    for idx, char in enumerate(grid):
        pos[char] = (idx // 5, idx % 5)
    text = text.upper().replace('J', 'I').replace(' ', '')
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        i += 1
        if i < len(text):
            b = text[i]
            pairs.append((a, b))
        else:
            pairs.append((a, 'X'))
        i += 1
    result = []
    for a, b in pairs:
        if a not in pos or b not in pos:
            result.append(a)
            result.append(b)
            continue
        row1, col1 = pos[a]
        row2, col2 = pos[b]
        if row1 == row2:
            result.append(grid[row1 * 5 + (col1 - 1) % 5])
            result.append(grid[row2 * 5 + (col2 - 1) % 5])
        elif col1 == col2:
            result.append(grid[((row1 - 1) % 5) * 5 + col1])
            result.append(grid[((row2 - 1) % 5) * 5 + col2])
        else:
            result.append(grid[row1 * 5 + col2])
            result.append(grid[row2 * 5 + col1])
    decrypted = ''.join(result)
    if decrypted.endswith('X'):
        decrypted = decrypted[:-1]
    return decrypted

def rail_fence_decrypt(text, num_rails):
    """
    Decrypt a Rail Fence cipher with the given number of rails.
    """
    num_rails = int(num_rails)
    if num_rails == 1:
        return text
    pattern = []
    direction = 1
    rail_idx = 0
    for i in range(len(text)):
        pattern.append(rail_idx)
        rail_idx += direction
        if rail_idx == num_rails - 1 or rail_idx == 0:
            direction = -direction
    rail_lengths = [pattern.count(i) for i in range(num_rails)]
    rail = [[] for _ in range(num_rails)]
    idx = 0
    for r in range(num_rails):
        for _ in range(rail_lengths[r]):
            rail[r].append(text[idx])
            idx += 1
    result = []
    rail_pos = [0] * num_rails
    rail_idx = 0
    direction = 1
    for i in range(len(text)):
        result.append(rail[rail_idx][rail_pos[rail_idx]])
        rail_pos[rail_idx] += 1
        rail_idx += direction
        if rail_idx == num_rails - 1 or rail_idx == 0:
            direction = -direction
    return ''.join(result)

def homophonic_decrypt(text, mapping_str):
    """
    Decrypt a homophonic substitution cipher.
    mapping_str should be a string where each position represents the plaintext
    for the ciphertext symbol. Since homophonic maps one plain to multiple cipher,
    this assumes a simple mapping; in practice, it may need adjustment.
    For simplicity, treat as simple substitution.
    """
    return simple_substitution_decrypt(text, mapping_str)

def main():
    print("Welcome to HCC Systems Message Encryptor/Decryptor!")
    print("Supported ciphers:")
    print("- C: Caesar")
    print("- A: Atbash")
    print("- S: Simple Substitution")
    print("- V: Vigenère")
    print("- T: Transposition")
    print("- P: Playfair")
    print("- R: Rail Fence")
    print("- H: Homophonic")
    print("Enter 'quit' to exit.\n")

    cipher_map = {
        'c': 'caesar',
        'a': 'atbash',
        's': 'simple substitution',
        'v': 'vigenere',
        't': 'transposition',
        'p': 'playfair',
        'r': 'rail fence',
        'h': 'homophonic'
    }

    while True:
        mode = input("Encrypt or Decrypt? ").strip().lower()
        if mode == 'quit':
            break
        elif mode not in ['encrypt', 'decrypt']:
            print("Please enter 'encrypt' or 'decrypt'.\n")
            continue
        encrypt = (mode == 'encrypt')
        
        cipher = input("Enter cipher type (first letter or full name): ").strip().lower()
        if cipher == 'quit':
            break
        if len(cipher) == 1:
            cipher = cipher_map.get(cipher, cipher)
        message = input("Enter message: ")
        try:
            if cipher == 'caesar':
                shift = int(input("Enter shift value: "))
                result = caesar_cipher(message, shift, encrypt)
            elif cipher == 'atbash':
                result = atbash_decrypt(message)  # Same for encrypt/decrypt
            elif cipher == 'simple substitution' or cipher == 'simple':
                mapping = input("Enter mapping (26 letters for A-Z plaintext order): ").strip()
                if encrypt:
                    print("Encryption for Simple Substitution not yet implemented.\n")
                    continue
                else:
                    result = simple_substitution_decrypt(message, mapping)
            elif cipher == 'vigenere':
                key = input("Enter key: ").strip()
                if not key.isalpha():
                    print("Key must contain only letters.\n")
                    continue
                if encrypt:
                    result = vigenere_encrypt(message, key)
                else:
                    result = vigenere_decrypt(message, key)
            elif cipher == 'transposition':
                num_columns = input("Enter number of columns: ").strip()
                if encrypt:
                    print("Encryption for Transposition not yet implemented.\n")
                    continue
                else:
                    result = transposition_decrypt(message, num_columns)
            elif cipher == 'playfair':
                key = input("Enter key: ").strip()
                if encrypt:
                    print("Encryption for Playfair not yet implemented.\n")
                    continue
                else:
                    result = playfair_decrypt(message, key)
            elif cipher == 'rail fence' or cipher == 'rail':
                num_rails = input("Enter number of rails: ").strip()
                if encrypt:
                    print("Encryption for Rail Fence not yet implemented.\n")
                    continue
                else:
                    result = rail_fence_decrypt(message, num_rails)
            elif cipher == 'homophonic':
                mapping = input("Enter mapping (26 letters for A-Z plaintext order): ").strip()
                if encrypt:
                    print("Encryption for Homophonic not yet implemented.\n")
                    continue
                else:
                    result = homophonic_decrypt(message, mapping)
            else:
                print("Unsupported cipher. Try again.\n")
                continue
            action = "Encrypted" if encrypt else "Decrypted"
            print(f"{action} message: {result}\n")
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()
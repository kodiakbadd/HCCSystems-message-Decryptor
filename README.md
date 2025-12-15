# HCC Systems Message Decryptor

A Python application to help decrypt simple cipher puzzles posted on HCC Systems' business Facebook page.

## Supported Ciphers

- **Caesar Cipher**: Shifts letters by a fixed number of positions.
- **Atbash Cipher**: Reverses the alphabet (A ↔ Z, B ↔ Y, etc.).
- **Simple Substitution Cipher**: Each letter is replaced with another letter using a fixed mapping.
- **Vigenère Cipher**: Uses a keyword for varying shifts.
- **Transposition Cipher**: Rearranges letters according to a columnar pattern.
- **Playfair Cipher**: Uses a 5×5 grid and digraph substitution.
- **Rail Fence Cipher**: Letters are written in a zigzag pattern across rows and read row by row.
- **Homophonic Substitution Cipher**: Maps one plaintext letter to multiple possible ciphertext symbols.

## Usage

1. Clone or download this repository.
2. Ensure Python 3.6+ is installed.
3. Run the decryptor:

   ```bash
   python decryptor.py
   ```

4. Follow the prompts to select a cipher, enter parameters, and input the encrypted message.

## Examples

### Caesar Cipher
```
Enter cipher type: caesar
Enter encrypted message: Khoor Zruog!
Enter shift value: 3
Decrypted message: Hello World!
```

### Atbash Cipher
```
Enter cipher type: atbash
Enter encrypted message: Svhg zl gsv gsviv
Decrypted message: Hello or the there
```

### Simple Substitution
```
Enter cipher type: simple substitution
Enter encrypted message: Uijt jt b tfvsf
Enter mapping (26 letters for A-Z plaintext order): ZYXWVUTSRQPONMLKJIHGFEDCBA
Decrypted message: This is a test
```

## Contributing

Feel free to add more cipher types or improve the application.

## License

[MIT License](LICENSE)
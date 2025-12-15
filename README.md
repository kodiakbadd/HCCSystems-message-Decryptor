# HCC Systems Message Encryptor/Decryptor

A Python application to encrypt or decrypt simple cipher puzzles posted on HCC Systems' business Facebook page.

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
3. Run the encryptor/decryptor:

   ```bash
   python decryptor.py
   ```

4. Follow the prompts to select encrypt/decrypt, cipher type, enter parameters, and input the message.

## Examples

### Caesar Cipher (Encrypt)
```
Enter mode: encrypt
Enter cipher type: caesar
Enter message: Test message one
Enter shift value: 4
Encrypted message: Xiwx qiwwe ki sri
```

### Caesar Cipher (Decrypt)
```
Enter mode: decrypt
Enter cipher type: caesar
Enter message: Xiwx qiwwe ki sri
Enter shift value: 4
Decrypted message: Test message one
```

### Atbash Cipher
```
Enter mode: encrypt
Enter cipher type: atbash
Enter message: Hello World
Encrypted message: Svool Dliow
```
(Note: Atbash is symmetric, so encrypt/decrypt are the same)

## Contributing

Feel free to add more cipher types or improve the application.

## License

[MIT License](LICENSE)
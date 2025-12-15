# HCC Systems Message Decryptor

A Python application to help decrypt simple cipher puzzles posted on HCC Systems' business Facebook page.

## Supported Ciphers

- **Caesar Cipher**: Shifts letters by a fixed number of positions.
- **Vigenère Cipher**: Uses a keyword for varying shifts.
- **Atbash Cipher**: Reverses the alphabet.

## Usage

1. Clone or download this repository.
2. Ensure Python 3.6+ is installed.
3. Run the decryptor:

   ```bash
   python decryptor.py
   ```

4. Follow the prompts to select a cipher, enter parameters, and input the encrypted message.

## Example

```
Enter cipher type (Caesar/Vigenere/Atbash): caesar
Enter shift value: 3
Enter encrypted message: Khoor Zruog!
Decrypted message: Hello World!
```

## Contributing

Feel free to add more cipher types or improve the application.

## License

[MIT License](LICENSE)
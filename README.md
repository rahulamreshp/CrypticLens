# PRODIGY_CS_02
# Pixel Manipulation for Image Encryption

This Python script presents an Image Encryption Tool utilizing pixel manipulation, providing a basic yet effective approach to encrypt and decrypt images. The program allows users to secure their images by applying a simple shift-based encryption technique.

# Usage
pip install -r Requirements.txt

python3 main.py

# Modules
The application has the following modules:

Encryption

1. Prompts the user for the image file to encrypt.

2. Obtains the encryption key (shift value) from the user.

3. Performs encryption by shifting pixel values based on the provided key.

4. Saves the encrypted image as a new file.

Decryption

1. Prompts the user for the encrypted image file to decrypt.

2. Obtains the decryption key (shift value) from the user.

3. Performs decryption by reverse shifting pixel values based on the provided key.

4. Saves the decrypted image as a new file.
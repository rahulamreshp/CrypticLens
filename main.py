from encrypt_image import encrypt
from decrypt_image import decrypt


def main():
    print("Welcome to Image Encryptor!\n")
    print("1. Encrypt Image")
    print("2. Decrypt Image\n")

    while True:
        choice = input("Enter your choice (1 or 2): ")
        if choice in ['1', '2']:
            break
        else:
            print()
            print("Invalid choice. Try again.")
            print()

    if choice == '1':
        image_path = input("\nEnter the path to the image you want to encrypt: ")
        shift = int(input("Enter the shift value for encryption: "))
        encrypt(image_path, shift)
    elif choice == '2':
        image_path = input("\nEnter the path to the image you want to decrypt: ")
        shift = int(input("Enter the shift value for decryption: "))
        decrypt(image_path, shift)
    else:
        exit()

    restart = input("Do you want to run the program again? (y/n): ")
    if restart.lower() == 'y':
        main()


if __name__ == "__main__":
    main()

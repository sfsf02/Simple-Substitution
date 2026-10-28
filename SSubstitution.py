import string
import argparse

letter_upper = string.ascii_uppercase
letter_lower = string.ascii_lowercase

def encrypt(text, shift):
    result = ""
    for char in text:
        if char in letter_upper:
            index = (letter_upper.index(char) + shift) % 26
            result += letter_upper[index]
        elif char in letter_lower:
            index = (letter_lower.index(char) + shift) % 26
            result += letter_lower[index]
        else:
            result += char
    return result

def decrypt(text, shift):
    result = ""
    for char in text:
        if char in letter_upper:
            index = (letter_upper.index(char) - shift) % 26
            result += letter_upper[index]
        elif char in letter_lower:
            index = (letter_lower.index(char) - shift) % 26
            result += letter_lower[index]
        else:
            result += char
    return result


def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a secret using a substitution cipher.")
    parser.add_argument("--choice", type=str, help="Enter 'e' to encrypt or 'd' to decrypt")
    parser.add_argument("--plain", type=str, help="The secret to encrypt")
    parser.add_argument("--shift", type=int, help="The shift value for the cipher")
    parser.add_argument("--cipher", type=str, help="The secret to decrypt")
    parser.add_argument("--brute", action="store_true", help="Enable brute force decryption")
    

    args = parser.parse_args()
    
    if not args.choice:
        parser.error("The --choice argument is required. Please enter 'e' for encrypt or 'd' for decrypt.")
    
    if args.choice == 'd':
        if not args.cipher:
            parser.error("The --cipher argument is required for decryption.")
        else:
            if args.shift is None and not args.brute:
                parser.error("The --shift argument is required for decryption unless using --brute for brute force decryption.")
        
    if args.choice == 'e' and (not args.plain or args.shift is None):
        if not args.plain:
            parser.error("The --plain argument is required for encryption.")
        if args.shift is None:
            parser.error("The --shift argument is required for encryption.")

    if args.choice == 'e':
        encrypted_text = encrypt(args.plain, args.shift)
        print(f"Encrypted text: {encrypted_text}")
    elif args.choice == 'd':
        if args.brute:
            for shift in range(1, 26):
                decrypted_text = decrypt(args.cipher, shift)
                print(f"Shift {shift}: {decrypted_text}")
        else:
            decrypted_text = decrypt(args.cipher, args.shift)
            print(f"Decrypted text: {decrypted_text}")
    else:
        print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
        
if __name__ == "__main__":
    main()
    






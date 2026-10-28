# Simple-Substitution

This is my assignmnet for my Network security course at university for make a tool for decrypting and encrypting using the Simple substituatuion.

# Caesar Cipher CLI Tool

A simple and efficient command-line utility for encrypting and decrypting text using a Caesar cipher (substitution cipher). The tool preserves the case of letters and leaves non-alphabetical characters (like spaces, numbers, and punctuation) unchanged.

## Features

* **Encrypt text** with a specific shift value.
* **Decrypt text** when the shift value is known.
* **Brute-force decryption** to crack a cipher by testing all 25 possible shift variations.
* **Case preservation**: Maintains uppercase and lowercase formatting.
* **Punctuation safe**: Ignores numbers, spaces, and special characters.

## Prerequisites

* Python 3.x
* No external libraries required (uses built-in `string` and `argparse` modules).

## Usage

Run the script from your terminal using the following arguments:

```bash
python cipher.py --choice <e|d> [options]
```

### Arguments

| Argument | Type | Description | Required |
| :--- | :--- | :--- | :--- |
| `--choice` | String | Operation to perform: `e` (encrypt) or `d` (decrypt). | **Yes** |
| `--plain` | String | The secret plaintext message you want to encrypt. | Yes (if `--choice e`) |
| `--cipher`| String | The encrypted message you want to decrypt. | Yes (if `--choice d`) |
| `--shift` | Integer| The numerical shift value for the cipher. | Yes (unless using `--brute`) |
| `--brute` | Flag | Enables brute-force decryption, displaying all 25 possible shifts. | No |

## Examples

### 1. Encrypting a Message
To encrypt the message "Hello, World!" with a shift of 5:
```bash
python cipher.py --choice e --plain "Hello, World!" --shift 5
```
**Output:**
```text
Encrypted text: Mjqqt, Btwqi!
```

### 2. Decrypting a Message
To decrypt the message "Mjqqt, Btwqi!" with a known shift of 5:
```bash
python cipher.py --choice d --cipher "Mjqqt, Btwqi!" --shift 5
```
**Output:**
```text
Decrypted text: Hello, World!
```

### 3. Brute-Force Decryption
If you have an encrypted message but don't know the shift value, use the `--brute` flag to print all possible combinations:
```bash
python cipher.py --choice d --cipher "Mjqqt" --brute
```
**Output:**
```text
Shift 1: Lipps
Shift 2: Khoor
...
Shift 5: Hello
...
Shift 25: Nkrru
```

## Error Handling

The script includes built-in validation to ensure you provide the correct arguments based on your choice:
* Missing the `--choice` argument will prompt an error.
* Trying to encrypt without providing both `--plain` and `--shift` will fail safely with instructions.
* Trying to decrypt without `--cipher` or without specifying either `--shift` or `--brute` will alert you to correct your command.

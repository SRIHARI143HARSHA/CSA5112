plaintext=input("enter plaintext :")
key=input("enter key :")
def polyalphabetic_cipher(plaintext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = key.upper()
    key_length = len(key)
    ciphertext = []

    for i, char in enumerate(plaintext.upper()):
        if char in alphabet:
            shift = alphabet.index(key[i % key_length])
            new_char = alphabet[(alphabet.index(char) + shift) % 26]
            ciphertext.append(new_char)
        else:
            ciphertext.append(char)

    return ''.join(ciphertext)
ciphertext = polyalphabetic_cipher(plaintext, key)
print(ciphertext)


output:
enter plaintext :srihari
enter key :hja
ZAIOJRP

=== Code Execution Successful ===

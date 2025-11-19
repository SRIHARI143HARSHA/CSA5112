ciphertext =input("enter any text :")
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_decrypt(ciphertext, a, b):
    m = 26  # Number of letters in the English alphabet
    a_inv = mod_inverse(a, m)
    if a_inv is None:
        raise ValueError("No modular inverse for a")

    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            x = ord(char) - ord('A')
            decrypted_char = (a_inv * (x - b)) % m
            decrypted_text += chr(decrypted_char + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

# Assuming a = 1 and b = 1 for demonstration
 # Example ciphertext
decrypted_message = affine_decrypt(ciphertext, 1, 1)
print(decrypted_message)


OUTPUT:
enter any text :SRIHARI
RQHGZQH

=== Code Execution Successful ===

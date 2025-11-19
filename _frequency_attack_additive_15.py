# Letter Frequency Attack on Additive Cipher

import string
from collections import Counter

def letter_frequency(text):
    text = text.lower()
    text = ''.join(filter(str.isalpha, text))
    frequency = Counter(text)
    return frequency

def decrypt_additive_cipher(ciphertext, key):
    decrypted_text = ''.join(
        chr((ord(char) - key - 97) % 26 + 97) for char in ciphertext.lower() if char.isalpha()
    )
    return decrypted_text

def generate_possible_plaintexts(ciphertext, top_n=10):
    frequency_order = 'etaoinshrdlcumwfgypbvkjxqz'
    possible_plaintexts = []

    for key in range(26):
        decrypted_text = decrypt_additive_cipher(ciphertext, key)
        freq = letter_frequency(decrypted_text)
        score = sum(freq[char] * (26 - frequency_order.index(char)) for char in freq)
        possible_plaintexts.append((decrypted_text, score))

    possible_plaintexts.sort(key=lambda x: x[1], reverse=True)
    return [text for text, score in possible_plaintexts[:top_n]]

if __name__ == "__main__":
    ciphertext = input("Enter the ciphertext: ")
    top_n = int(input("How many possible plaintexts do you want? "))
    results = generate_possible_plaintexts(ciphertext, top_n)
    
    print("\nTop Possible Plaintexts:")
    for i, plaintext in enumerate(results, 1):
        print(f"{i}: {plaintext}")


OUTPUT:
Enter the ciphertext: SRIHARI
How many possible plaintexts do you want? 5

Top Possible Plaintexts:
1: onedwne
2: srihari
3: dctslct
4: edutmdu
5: fevunev

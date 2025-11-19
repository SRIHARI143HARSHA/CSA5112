def generate_monoalphabetic_cipher(keyword):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    keyword = ''.join(sorted(set(keyword), key=keyword.index))  # Remove duplicates while preserving order
    cipher = keyword + ''.join([letter for letter in alphabet if letter not in keyword])
    return alphabet, cipher

def print_cipher_mapping():
    keyword = "CIPHER"
    plain, cipher = generate_monoalphabetic_cipher(keyword.lower())
    
    print("Plain:  ", ' '.join(plain))
    print("Cipher: ", ' '.join(cipher.upper()))

print_cipher_mapping()


output:
Plain:   a b c d e f g h i j k l m n o p q r s t u v w x y z
Cipher:  C I P H E R A B D F G J K L M N O Q S T U V W X Y Z

=== Code Execution Successful ===

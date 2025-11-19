BLOCK_SIZE = 8  # 8 bytes block size

def xor_encrypt(block, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(block)])

def pad(data):
    p = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + bytes([p]) * p

def unpad(data):
    return data[:-data[-1]]

def cbc_encrypt(plaintext, key, iv):
    plaintext = pad(plaintext)
    blocks = [plaintext[i:i+BLOCK_SIZE] for i in range(0, len(plaintext), BLOCK_SIZE)]
    ciphertext = []
    prev = iv
    for block in blocks:
        xor_in = bytes([block[i] ^ prev[i] for i in range(BLOCK_SIZE)])
        enc_block = xor_encrypt(xor_in, key)
        ciphertext.append(enc_block)
        prev = enc_block
    return b"".join(ciphertext)

def cbc_decrypt(ciphertext, key, iv):
    blocks = [ciphertext[i:i+BLOCK_SIZE] for i in range(0, len(ciphertext), BLOCK_SIZE)]
    plaintext = []
    prev = iv
    for block in blocks:
        dec_block = xor_encrypt(block, key)
        plain_block = bytes([dec_block[i] ^ prev[i] for i in range(BLOCK_SIZE)])
        plaintext.append(plain_block)
        prev = block
    return unpad(b"".join(plaintext))

key = b"mysecret"
iv  = b"12345678"
message = b"Hello CBC Mode!"

cipher = cbc_encrypt(message, key, iv)
plain  = cbc_decrypt(cipher, key, iv)

print("Cipher:", cipher)


output:

Cipher: b'\x14.,=9d\x11\x0e:w\x127>sU{'
Plain: b'Hello CBC Mode!'

=== Code Execution Successful ===
print("Plain:", plain)

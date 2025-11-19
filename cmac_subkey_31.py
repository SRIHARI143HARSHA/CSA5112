# filename: 31_cmac_subkeys.py
"""
CMAC subkey generation (RFC 4493) – demo version without external libraries.
- For block size 128 bits (AES): Rb = 0x87
- For block size 64 bits (e.g. DES/3DES): Rb = 0x1B

L = E_k(0^blocksize)
K1 = (L << 1)  XOR Rb  if MSB(L)==1  else (L << 1)
K2 = (K1 << 1) XOR Rb  if MSB(K1)==1 else (K1 << 1)

Here E_k is a TOY block cipher (XOR with key) so that the code runs
without Crypto / PyCryptodome. For real security, replace it with real AES.
"""

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def left_shift_one(bitstring: bytes) -> bytes:
    out = bytearray(len(bitstring))
    carry = 0
    for i in range(len(bitstring) - 1, -1, -1):
        b = bitstring[i]
        out[i] = ((b << 1) & 0xFF) | carry
        carry = (b >> 7) & 0x01
    return bytes(out)

# --- TOY "block cipher" (NOT secure, but no imports needed) ---

def fake_block_encrypt(key: bytes, block: bytes) -> bytes:
    """Toy block cipher: XOR block with key (cycled)."""
    return bytes(block[i] ^ key[i % len(key)] for i in range(len(block)))

# --- CMAC subkey generation for 128-bit block (AES style) ---

def generate_cmac_subkeys_aes(key: bytes):
    block_size = 16  # 128 bits
    zero_block = b"\x00" * block_size
    L = fake_block_encrypt(key, zero_block)  # in real CMAC: AES-ECB(key, 0^128)
    Rb = bytes([0] * 15 + [0x87])  # 128-bit Rb

    K1 = left_shift_one(L)
    if L[0] & 0x80:
        K1 = xor_bytes(K1, Rb)

    K2 = left_shift_one(K1)
    if K1[0] & 0x80:
        K2 = xor_bytes(K2, Rb)

    return L, K1, K2

# --- Optional: CMAC subkeys for 64-bit block (DES/3DES style) ---

def generate_cmac_subkeys_blocksize64(key: bytes):
    block_size = 8  # 64 bits
    zero_block = b"\x00" * block_size
    key = key[:block_size]  # use first 8 bytes
    L = fake_block_encrypt(key, zero_block)
    Rb = bytes([0] * 7 + [0x1B])  # 64-bit Rb

    K1 = left_shift_one(L)
    if L[0] & 0x80:
        K1 = xor_bytes(K1, Rb)

    K2 = left_shift_one(K1)
    if K1[0] & 0x80:
        K2 = xor_bytes(K2, Rb)

    return L, K1, K2

if __name__ == "__main__":
    print("CMAC subkey generator (AES-128 style, demo).")
    key = input("Enter key hex (e.g. 32 hex chars) or press Enter for default: ").strip()
    if not key:
        # simple fixed demo key
        keyb = bytes.fromhex("00112233445566778899aabbccddeeff")
        print("Using default key:", keyb.hex())
    else:
        keyb = bytes.fromhex(key)

    L, K1, K2 = generate_cmac_subkeys_aes(keyb)
    print("L  =", L.hex())
    print("K1 =", K1.hex())
    print("K2 =", K2.hex())
    print("\n(a) Constants: Rb(128-bit) = 0x87 ; Rb(64-bit) = 0x1B")
    print("b) Left shift = multiply by x in GF(2^n).")
    print("   If MSB is 1, XOR with Rb performs modular reduction so result stays in the field.")


output:
CMAC subkey generator (AES-128 style, demo).
Enter key hex (e.g. 32 hex chars) or press Enter for default: 32
L  = 32323232323232323232323232323232
K1 = 64646464646464646464646464646464
K2 = c8c8c8c8c8c8c8c8c8c8c8c8c8c8c8c8

(a) Constants: Rb(128-bit) = 0x87 ; Rb(64-bit) = 0x1B
b) Left shift = multiply by x in GF(2^n).
   If MSB is 1, XOR with Rb performs modular reduction so result stays in the field.

=== Code Execution Successful ===

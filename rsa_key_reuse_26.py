p,q,e = 61,53,17
n = p*q
phi = (p-1)*(q-1)
d = pow(e, -1, phi)

msg = "hi"
cipher = [pow(ord(c), e, n) for c in msg]
plain  = "".join(chr(pow(c, d, n)) for c in cipher)

print("Public key:", (n, e))
print("Private key:", (n, d))
print("Cipher:", cipher)
print("Decrypted:", plain)

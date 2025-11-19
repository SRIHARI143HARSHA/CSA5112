P = [0b0001, 0b0010, 0b0100]  # P1, P2, P3
K = 0b1011
IV = 0b0000

def E(x): return x ^ K
def D(x): return x ^ K

def cbc_enc(P):
    C = []; prev = IV
    for p in P:
        c = E(p ^ prev); C.append(c); prev = c
    return C

def cbc_dec(C):
    P = []; prev = IV
    for c in C:
        p = D(c) ^ prev; P.append(p); prev = c
    return P

C = cbc_enc(P)
C_err = C[:]         # copy
C_err[0] ^= 0b0001   # flip 1 bit in C1 (channel error)

print("P     =", P)
print("C     =", C)
print("Dec(C)    =", cbc_dec(C))
print("C_err =", C_err)
print("Dec(C_err) =", cbc_dec(C_err))  # only P1, P2 differ


OUTPUT:
P     = [1, 2, 4]
C     = [10, 3, 12]
Dec(C)    = [1, 2, 4]
C_err = [11, 3, 12]
Dec(C_err) = [0, 3, 4]

=== Code Execution Successful ===

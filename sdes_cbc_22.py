P10=[2,4,1,6,3,9,0,8,7,5]
P8=[5,2,6,3,7,4,9,8]
P4=[1,3,2,0]
IP=[1,5,2,0,3,7,4,6]
IP_INV=[3,0,2,4,6,1,7,5]
EP=[3,0,1,2,1,2,3,0]
S0=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
S1=[[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]

def perm(b,t): return ''.join(b[i] for i in t)
def ls(b,n): return b[n:]+b[:n]
def xor(a,b): return ''.join('1'*(x!=y)+'0'*(x==y) for x,y in zip(a,b))
def sbox(box,b):
    r=int(b[0]+b[3],2); c=int(b[1]+b[2],2)
    return format(box[r][c],'02b')

def keys(k10):
    k=perm(k10,P10); L,R=k[:5],k[5:]
    L1,R1=ls(L,1),ls(R,1); K1=perm(L1+R1,P8)
    L2,R2=ls(L1,2),ls(R1,2); K2=perm(L2+R2,P8)
    return K1,K2

def fk(b,k):
    L,R=b[:4],b[4:]
    t=xor(perm(R,EP),k)
    o=sbox(S0,t[:4])+sbox(S1,t[4:])
    L=xor(L,perm(o,P4))
    return L+R

def sdes_enc(block,key10):
    K1,K2=keys(key10)
    b=perm(block,IP)
    b=fk(b,K1); b=b[4:]+b[:4]
    b=fk(b,K2)
    return perm(b,IP_INV)

def sdes_dec(block,key10):
    K1,K2=keys(key10)
    b=perm(block,IP)
    b=fk(b,K2); b=b[4:]+b[:4]
    b=fk(b,K1)
    return perm(b,IP_INV)

def cbc_encrypt(plain,key10,iv):
    prev, out = iv, ''
    for i in range(0,len(plain),8):
        b=plain[i:i+8]
        out_block=sdes_enc(xor(b,prev),key10)
        out+=out_block; prev=out_block
    return out

def cbc_decrypt(cipher,key10,iv):
    prev, out = iv, ''
    for i in range(0,len(cipher),8):
        c=cipher[i:i+8]
        p=xor(sdes_dec(c,key10),prev)
        out+=p; prev=c
    return out

# ---- Test with your data ----
iv  = '10101010'                  # 1010 1010
pt  = '0000000100100011'         # 0000 0001 0010 0011
key = '0111111101'               # 01111 11101

ct = cbc_encrypt(pt,key,iv)
dec= cbc_decrypt(ct,key,iv)

print("Ciphertext :", ct)        # expected: 1111010000001011
print("Decrypted  :", dec)       # expected: 0000000100100013





output:
Ciphertext : 1111010000001011
Decrypted  : 0000000100100011

=== Code Execution Successful ===

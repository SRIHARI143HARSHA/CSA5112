"""
Demonstrate that encrypting each letter 0..25 separately is weak; attacker can brute-force each ciphertext.
This script creates small RSA and shows brute-force recovery.
"""
def powmod(a,e,n): return pow(a,e,n)

def brute_force_block(c,e,n,alphabet_size=26):
    res=[]
    for m in range(alphabet_size):
        if pow(m,e,n)==c:
            res.append(m)
    return res

if __name__=='__main__':
    e = int(input("e = ").strip()); n = int(input("n = ").strip())
    block_count = int(input("number of cipher blocks = ").strip())
    blocks = [int(input(f"c[{i}] = ").strip()) for i in range(block_count)]
    for i,c in enumerate(blocks):
        cand = brute_force_block(c,e,n)
        print(f"Block {i} candidates: {cand}")
    print("\nIf candidates are small (like 1 each), attacker recovers plaintext easily. Use padding or larger message blocks.")

output:
e = 7
n = 5
number of cipher blocks = 8
c[0] = 7
c[1] = 9
c[2] = 4
c[3] = 6
c[4] = 7
c[5] = 5
c[6] = 9
c[7] = 3
Block 0 candidates: []
Block 1 candidates: []
Block 2 candidates: [4, 9, 14, 19, 24]
Block 3 candidates: []
Block 4 candidates: []
Block 5 candidates: []
Block 6 candidates: []
Block 7 candidates: [2, 7, 12, 17, 22]




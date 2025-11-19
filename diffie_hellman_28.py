# Program 28: Diffie-Hellman Key Exchange
def diffie_hellman():
    print("=== Diffie-Hellman Key Exchange ===")
    
    # Public parameters
    p = int(input("Enter prime p (e.g., 23): ") or "23")
    g = int(input("Enter generator g (e.g., 5): ") or "5")
    
    print(f"\nPublic parameters: p={p}, g={g}")
    
    # Alice's private key
    a = int(input("\nAlice's private key a: ") or "6")
    A = pow(g, a, p)
    print(f"Alice sends: A = g^a mod p = {A}")
    
    # Bob's private key
    b = int(input("\nBob's private key b: ") or "15")
    B = pow(g, b, p)
    print(f"Bob sends: B = g^b mod p = {B}")
    
    # Shared secret
    shared_alice = pow(B, a, p)
    shared_bob = pow(A, b, p)
    
    print(f"\nAlice computes: B^a mod p = {shared_alice}")
    print(f"Bob computes: A^b mod p = {shared_bob}")
    print(f"\nShared secret: {shared_alice}")
    
    if shared_alice == shared_bob:
        print("✓ Key exchange successful!")

if __name__ == "__main__":
    diffie_hellman()


output:
=== Diffie-Hellman Key Exchange ===
Enter prime p (e.g., 23): 23
Enter generator g (e.g., 5): 5

Public parameters: p=23, g=5

Alice's private key a: 5
Alice sends: A = g^a mod p = 20

Bob's private key b: 7
Bob sends: B = g^b mod p = 17

Alice computes: B^a mod p = 21
Bob computes: A^b mod p = 21

Shared secret: 21
✓ Key exchange successful!

=== Code Execution Successful ===

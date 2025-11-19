class PlayfairCipher:
    def __init__(self, keyword):
        self.keyword = keyword
        self.matrix = self.create_matrix()

    def create_matrix(self):
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 'J' is omitted
        seen = set()
        matrix = []

        for char in self.keyword.upper():
            if char not in seen and char in alphabet:
                seen.add(char)
                matrix.append(char)

        for char in alphabet:
            if char not in seen:
                seen.add(char)
                matrix.append(char)

        return [matrix[i:i + 5] for i in range(0, 25, 5)]

    def encrypt(self, plaintext):
        plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
        pairs = self.prepare_pairs(plaintext)
        ciphertext = ""

        for a, b in pairs:
            row_a, col_a = self.find_position(a)
            row_b, col_b = self.find_position(b)

            if row_a == row_b:
                ciphertext += self.matrix[row_a][(col_a + 1) % 5]
                ciphertext += self.matrix[row_b][(col_b + 1) % 5]
            elif col_a == col_b:
                ciphertext += self.matrix[(row_a + 1) % 5][col_a]
                ciphertext += self.matrix[(row_b + 1) % 5][col_b]
            else:
                ciphertext += self.matrix[row_a][col_b]
                ciphertext += self.matrix[row_b][col_a]

        return ciphertext

    def prepare_pairs(self, plaintext):
        pairs = []
        i = 0
        while i < len(plaintext):
            a = plaintext[i]
            b = plaintext[i + 1] if i + 1 < len(plaintext) else 'X'
            if a == b:
                b = 'X'
                i -= 1
            pairs.append((a, b))
            i += 2
        return pairs

    def find_position(self, char):
        for i, row in enumerate(self.matrix):
            if char in row:
                return i, row.index(char)

# Example usage
cipher = PlayfairCipher("KEYWORD")
encrypted_text = cipher.encrypt("HELLO WORLD")
print("Encrypted:", encrypted_text)



output:
Encrypted: GYIZSCOKCFBU

=== Code Execution Successful ===

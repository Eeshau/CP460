def mod_inverse(a, m):
    """
    Calculate the modular inverse of a mod m.
    """
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def AffineEncrypt(k, plaintext):
    a, b = k
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = (a * (ord(char) - ord('a')) + b) % 26
            if char.isupper():
                ciphertext += chr(ord('A') + shift)
            else:
                ciphertext += chr(ord('a') + shift)
        else:
            ciphertext += char
    return ciphertext

def AffineDecrypt(k, ciphertext):
    a, b = k
    plaintext = ""
    a_inv = mod_inverse(a, 26)
    for char in ciphertext:
        if char.isalpha():
            shift = a_inv * (ord(char) - ord('a') - b) % 26
            if char.isupper():
                plaintext += chr(ord('A') + shift)
            else:
                plaintext += chr(ord('a') + shift)
        else:
            plaintext += char
    return plaintext

# Sample execution:
plaintext = "john smith is the culprit!"
k = (17, 8)
ciphertext = AffineEncrypt(k, plaintext)
decrypted_text = AffineDecrypt(k, ciphertext)

print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")


k = (7, 22)
decrypted_text = AffineDecrypt(k, "falszztysyjzyjkywjrztyjztyynaryjkyswarztyegyyj")
print(f"Decrypted Text: {decrypted_text}")



'''
Implement a function that performs a letter frequency attack based on the table
1. Put the letters into a dictionary with the respective frequencies from the table
2. Count the occurrence of each letter in the text, and make estimated guesses based on if their frequency matches that of the letter in the string.
3. If it does than replace that letter with the respective letter based on it’s frequency
'''


def frequency_attack(ciphertext):

    # 1. Put the letters into a dictionary with the respective frequencies from the table
    english_freq = {
        'A': 0.0817, 'B': 0.0150, 'C': 0.0278, 'D': 0.0425, 'E': 0.1270, 'F': 0.0223,
        'G': 0.0202, 'H': 0.0609, 'I': 0.0697, 'J': 0.0015, 'K': 0.0077, 'L': 0.0403,
        'M': 0.0241, 'N': 0.0675, 'O': 0.0751, 'P': 0.0193, 'Q': 0.0010, 'R': 0.0599,
        'S': 0.0633, 'T': 0.0906, 'U': 0.0276, 'V': 0.0098, 'W': 0.0236, 'X': 0.0015,
        'Y': 0.0197, 'Z': 0.0007
    }



    # 2. Count the occurrence of each letter in the text
    cipher_freq = {}
    for letter in ciphertext:
        if letter.upper() in cipher_freq:
            cipher_freq[letter.upper()] += 1
        else:
            cipher_freq[letter.upper()] = 1

    for key in cipher_freq:
        cipher_freq[key] = cipher_freq[key] / len(ciphertext)

    # Sorting dictionaries based on their frequencies
    sorted_english = sorted(english_freq.items(), key=lambda x: x[1], reverse=True)
    sorted_cipher = sorted(cipher_freq.items(), key=lambda x: x[1], reverse=True)

    # Mapping cipher letters to estimated english letters based on frequency
    mapping = {}
    for i in range(len(sorted_cipher)):
        mapping[sorted_cipher[i][0]] = sorted_english[i][0]

    # 3. Replace the letters in the cipher text based on frequency mapping
    decrypted_text = ""
    for letter in ciphertext:
        decrypted_text += mapping[letter.upper()]

    return decrypted_text



# Test the function
ciphertext = "xultpaajcxitltlxaarpjhtiwtgxktghidhipxicwtvjpgtpilhglxiwiwtxgqadds"
print(frequency_attack(ciphertext))
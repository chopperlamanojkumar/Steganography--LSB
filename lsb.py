# Least Significant Bit (LSB) Steganography
import numpy as np
# ASCII char to int and int to char
d = {chr(i): i for i in range(255)}  # char to ASCII
c = {i: chr(i) for i in range(255)}  # ASCII to char
# ASCII char to int and int to char
d = {chr(i): i for i in range(255)}  # char to ASCII
c = {i: chr(i) for i in range(255)}  # ASCII to char# ASCII char to int and int to char
d = {chr(i): i for i in range(255)}  # char to ASCII
c = {i: chr(i) for i in range(255)}  # ASCII to char
# Message and encryption key
text = "Hello"
key = "key"
# Generate a random image of size 10x10 with RGB channels
x = np.random.randint(0, 255, (10, 10, 3), dtype=np.uint8)
# Copy the image for encoding
x_enc = x.copy()

# Initialize coordinates and other variables
n = 0  # row
m = 0  # column
z = 0  # color channel (R/G/B)
l = len(text)  # length of message
k1 = 0  # key index

# Loop through each character of the message
for i in range(l):
    # XOR with key character
    char_val = d[text[i]] ^ d[key[k1]]

    # Embed each bit of the character (8 bits)
    for bit_pos in range(8):
        bit = (char_val >> (7 - bit_pos)) & 1
        org_val = x_enc[n, m, z]
        x_enc[n, m, z] = (org_val & ~1) | bit  # Embed bit in LSB

        # Debug output
        print(f"Embedding bit {bit} of '{text[i]}' at ({n},{m},{z}) original={org_val} new={x_enc[n, m, z]}")

        # Move to next color channel/pixel
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m == x_enc.shape[1]:
                m = 0
                n += 1

    # Move to next key character
    k1 = (k1 + 1) % len(key)

n, m, z = 0, 0, 0
kl = 0
decrypt = ""

for i in range(len(text)):  # same length as original message
    val = 0
    for bit_pos in range(8):
        bit = x_enc[n, m, z] & 1
        print(f"Reading bit {bit} from ({n},{m},{z})")
        val = (val << 1) | bit
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m == x_enc.shape[1]:
                m = 0
                n += 1

    orig_ascii = val ^ d[key[kl]]
    orig_char = c[orig_ascii]
    print(f"Decrypted byte: {val} XOR {d[key[kl]]} = {orig_ascii} -> '{orig_char}'")
    decrypt += orig_char
    kl = (kl + 1) % len(key)

print("Decrypted text:", decrypt)   
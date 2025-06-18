# Steganography--LSB


*This Python code implements a simple image steganography project using the Least Significant Bit (LSB) method. Here's a brief explanation:

Data to Binary Conversion:

The data2binary function converts input data (either a string, bytes, or numpy array) into its binary representation. Hide Data in Image:

The hide_data function takes an image and data as input and hides the data in the image using the LSB method. It also includes a password in the hidden data. Encoding:

The encode function prompts the user to input an image file, a message, and a password. It then encodes the message into the image using the hide_data function and saves the result as a new image file. Find Data in Image:

The find_data function extracts hidden data from an image using the LSB method. It also takes a password as input and uses it during decoding. Decoding:

The decode function prompts the user to input an encoded image file and a password. It then decodes the hidden message using the find_data function and prints the result. Main Steganography Function:

The steganography function is the main control loop. It allows the user to choose between encoding and decoding operations and continues until the user decides to exit. In summary, this code allows users to hide messages in images using steganography and retrieve them later with the correct password. The encoding process embeds the message in the image, and the decoding process extracts the hidden message using the provided password.*

#OUTPUT

Embedding bit 0 of 'H' at (0,0,0) original=123 new=122
Embedding bit 0 of 'H' at (0,0,1) original=201 new=201
Embedding bit 1 of 'H' at (0,0,2) original=154 new=155
Embedding bit 1 of 'H' at (0,1,0) original=99 new=99
Embedding bit 0 of 'H' at (0,1,1) original=67 new=67
Embedding bit 1 of 'H' at (0,1,2) original=133 new=133
Embedding bit 1 of 'H' at (0,2,0) original=210 new=210
Embedding bit 0 of 'H' at (0,2,1) original=45 new=45

Embedding bit 0 of 'e' at (0,2,2) original=88 new=88
Embedding bit 1 of 'e' at (0,3,0) original=111 new=111
Embedding bit 1 of 'e' at (0,3,1) original=33 new=33
Embedding bit 0 of 'e' at (0,3,2) original=192 new=192
Embedding bit 1 of 'e' at (0,4,0) original=100 new=101
Embedding bit 0 of 'e' at (0,4,1) original=212 new=212
Embedding bit 0 of 'e' at (0,4,2) original=156 new=156
Embedding bit 1 of 'e' at (0,5,0) original=180 new=180

Embedding bit 0 of 'l' at (0,5,1) original=144 new=144
Embedding bit 1 of 'l' at (0,5,2) original=77 new=77
Embedding bit 1 of 'l' at (0,6,0) original=200 new=201
Embedding bit 0 of 'l' at (0,6,1) original=55 new=55
Embedding bit 1 of 'l' at (0,6,2) original=102 new=103
Embedding bit 1 of 'l' at (0,7,0) original=177 new=177
Embedding bit 0 of 'l' at (0,7,1) original=23 new=23
Embedding bit 0 of 'l' at (0,7,2) original=129 new=129

Embedding bit 1 of 'l' at (0,8,0) original=130 new=131
Embedding bit 0 of 'l' at (0,8,1) original=12 new=12
Embedding bit 0 of 'l' at (0,8,2) original=143 new=143
Embedding bit 1 of 'l' at (0,9,0) original=190 new=190
Embedding bit 0 of 'l' at (0,9,1) original=199 new=199
Embedding bit 1 of 'l' at (0,9,2) original=104 new=105
Embedding bit 0 of 'l' at (1,0,0) original=110 new=110
Embedding bit 0 of 'l' at (1,0,1) original=208 new=208

Embedding bit 0 of 'o' at (1,0,2) original=155 new=155
Embedding bit 1 of 'o' at (1,1,0) original=115 new=115
Embedding bit 1 of 'o' at (1,1,1) original=90 new=90
Embedding bit 1 of 'o' at (1,1,2) original=101 new=101
Embedding bit 0 of 'o' at (1,2,0) original=119 new=119
Embedding bit 1 of 'o' at (1,2,1) original=106 new=107
Embedding bit 0 of 'o' at (1,2,2) original=140 new=140
Embedding bit 0 of 'o' at (1,3,0) original=122 new=122

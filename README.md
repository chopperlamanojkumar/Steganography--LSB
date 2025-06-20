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


![Image](https://github.com/user-attachments/assets/7703d27b-e5f9-4596-a0f6-063dd60906d1)
![Image](https://github.com/user-attachments/assets/f509991f-8e20-47b7-8d21-8e64d0557603)

![Image](https://github.com/user-attachments/assets/2dfe5cec-65e1-4418-8748-6b184d0ad142)
![Image](https://github.com/user-attachments/assets/f1df5f8a-2fc6-49e6-a6ea-500705dd131e)

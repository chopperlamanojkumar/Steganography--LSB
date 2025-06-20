from PIL import Image
import hashlib

def to_bin(data):
    if isinstance(data, str):
        return ''.join(format(ord(i), "08b") for i in data)
    elif isinstance(data, bytes) or isinstance(data, bytearray):
        return ''.join(format(i, "08b") for i in data)
    elif isinstance(data, int):
        return format(data, "08b")
    else:
        raise TypeError("Type not supported.")

def encode(image_path, message, output_path, password):
    # Insert a SHA‑256 hash of the password as a 64‑hex string + delimiter
    pwd_hash = hashlib.sha256(password.encode()).hexdigest()
    payload = pwd_hash + "::" + message + "====="
    binary_message = to_bin(payload)
    data_len = len(binary_message)

    img = Image.open(image_path)
    if img.mode != 'RGB': img = img.convert('RGB')
    encoded = img.copy()
    w, h = img.size
    index = 0

    for y in range(h):
        for x in range(w):
            if index >= data_len: break
            r, g, b = img.getpixel((x, y))
            channels = [r, g, b]
            for i in range(3):
                if index < data_len:
                    bit = int(binary_message[index])
                    channels[i] = (channels[i] & ~1) | bit
                    index += 1
            encoded.putpixel((x, y), tuple(channels))
        else:
            continue
        break

    encoded.save(output_path)
    print(f"Encoding complete. Saved to {output_path}")

def decode(image_path, password):
    img = Image.open(image_path)
    if img.mode != 'RGB': img = img.convert('RGB')
    bits = ""

    for pixel in img.getdata():
        for c in pixel[:3]:
            bits += str(c & 1)

    chars = [bits[i:i+8] for i in range(0, len(bits), 8)]
    decoded = "".join(chr(int(b, 2)) for b in chars)

    # Extract password hash, message, and delimiter
    try:
        pwd_hash, rest = decoded.split("::", 1)
    except ValueError:
        return "[Error] No password hash found"
    if pwd_hash != hashlib.sha256(password.encode()).hexdigest():
        return "[Error] Wrong password"
    message = rest.split("=====")[0]
    return message

def steganography():
    while True:
        choice = input("\n1. Encode\n2. Decode\n0. Exit\nChoose: ")
        if choice == "1":
            i = input("Image to encode: ")
            msg = input("Hidden message: ")
            o = input("Output image name: ")
            pwd = input("Password: ")
            encode(i, msg, o, pwd)
        elif choice == "2":
            i = input("Image to decode: ")
            pwd = input("Password: ")
            print("Hidden message:", decode(i, pwd))
        else:
            break

if _name_ == "_main_":
    steganography()

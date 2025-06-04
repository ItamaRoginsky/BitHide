from PIL import Image
import numpy as np

def extract_lsb_bits_from_image(image_path):
    img = Image.open(image_path).convert('RGB')
    pixels = np.array(img).flatten()
    bits = ''.join(str(pixel & 1) for pixel in pixels)
    return bits

def decode_bits_to_message(bits):
    chars = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) < 8:
            continue
        char = chr(int(byte, 2))
        chars.append(char)
        if ''.join(chars).endswith('$EOF$'):
            return ''.join(chars).replace('$EOF$', '')
    raise ValueError("No EOF marker found. Message may be incomplete.")

def decode_image(image_path):
    bits = extract_lsb_bits_from_image(image_path)
    return decode_bits_to_message(bits)

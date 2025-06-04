from PIL import Image
import numpy as np

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def hide_data_in_image(input_path, message, output_path):
    message += "$EOF$"
    binary_data = text_to_binary(message)
    data_index = 0

    img = Image.open(input_path).convert('RGB')
    pixels = np.array(img)

    h, w, _ = pixels.shape
    total_bits = h * w * 3

    if len(binary_data) > total_bits:
        raise ValueError("Message too long for this image.")

    flat_pixels = pixels.flatten()

    for i in range(len(flat_pixels)):
        if data_index < len(binary_data):
            flat_pixels[i] = (flat_pixels[i] & 0b11111110) | int(binary_data[data_index])
            data_index += 1
        else:
            break

    new_pixels = flat_pixels.reshape((h, w, 3))
    encoded_img = Image.fromarray(new_pixels.astype('uint8'), 'RGB')
    encoded_img.save(output_path)

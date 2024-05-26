from PIL import Image

def load_image(image_path):
    try:
        return Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: Input file not found at {image_path}")
        return None
    except Exception as e:
        print(f"Error: Failed to load image from {image_path}. Reason: {e}")
        return None

def shift_pixel_values(pixels, width, height, mode, key):
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            if mode == "encrypt":
                new_r = (r + key) % 256
                new_g = (g + key) % 256
                new_b = (b + key) % 256
            elif mode == "decrypt":
                new_r = (r - key) % 256
                new_g = (g - key) % 256
                new_b = (b - key) % 256
            else:
                raise ValueError("Invalid mode. Mode must be 'encrypt' or 'decrypt'.")
            pixels[x, y] = (new_r, new_g, new_b)

def save_image(image, new_path):
    try:
        image.save(new_path)
        print(f"Image saved to: {new_path}")
    except Exception as e:
        print(f"Error: Failed to save image to {new_path}. Reason: {e}")

def encrypt_decrypt_image(image_path, new_path, mode, key):
    image = load_image(image_path)
    if image:
        pixels = image.load()
        width, height = image.size
        shift_pixel_values(pixels, width, height, mode, key)
        save_image(image, new_path)

# Example usage
image_path = "your_image.jpg"  # Replace with your image path, offcourse I am not giving my path.
new_path_encrypted = "encrypted_image.jpg"
new_path_decrypted = "decrypted_image.jpg"
key = 5  # Positive for encrypt, negative for decrypt

encrypt_decrypt_image(image_path, new_path_encrypted, "encrypt", key)
encrypt_decrypt_image(new_path_encrypted, new_path_decrypted, "decrypt", -key)

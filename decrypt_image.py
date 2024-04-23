from PIL import Image

def decrypt(image_path, shift):
    image = Image.open(image_path)
    width, height = image.size
    pixels = image.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r = (r - shift) % 256
            g = (g - shift) % 256
            b = (b - shift) % 256
            pixels[x, y] = (r, g, b)

    decrypted_image_path = image_path.split('_encrypted')[0] + '_decrypted.png'
    image.save(decrypted_image_path)
    print("\nImage decrypted successfully!")

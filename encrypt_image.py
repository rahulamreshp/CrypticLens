from PIL import Image

def encrypt(image_path, shift):
    image = Image.open(image_path)
    width, height = image.size
    pixels = image.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r = (r + shift) % 256
            g = (g + shift) % 256
            b = (b + shift) % 256
            pixels[x, y] = (r, g, b)

    encrypted_image_path = image_path.split('.')[0] + '_encrypted.png'
    image.save(encrypted_image_path)
    print("\nImage encrypted successfully!")

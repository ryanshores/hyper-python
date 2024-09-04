import requests
from PIL import Image
from io import BytesIO

# Grayscale levels mapped to a set of ASCII characters
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']


def resize_image(image, new_width=100):
    # Maintain aspect ratio
    width, height = image.size
    aspect_ratio = height / 2 / width
    new_height = int(new_width * aspect_ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def grayify(image):
    return image.convert('L')


def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]
    return ascii_str

def convert_image_to_ascii(image, new_width=100):
    # Convert image to grayscale image
    grayscale_image = grayify(resize_image(image, new_width))

    # Convert grayscale image to ASCII characters
    ascii_str = pixels_to_ascii(grayscale_image)

    # Format the ASCII string into appropriate line breaks
    img_width = grayscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i + img_width] + "\n"

    return ascii_img



def convert_image_url_to_ascii(image_url, new_width=100):
    try:
        response = requests.get(
            image_url,
            headers={'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)'}
        )
        image = Image.open(BytesIO(response.content))
    except Exception as e:
        print(f"Unable to open image from URL {image_url}.")
        print(e)
        return

    return convert_image_to_ascii(image, new_width)
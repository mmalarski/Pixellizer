from PIL import Image
import math
from Pixel import Pixel
import argparse


def floor_to_step(value, step):
    return (value // step) * step


def ceil_to_step(value, step):
    return math.ceil(value / step) * step


def common_divisors(a, b):
    return [i for i in range(1, min(a, b) + 1) if a % i == b % i == 0]


def find_all_common_denominators(num1, num2):
    common_denominators = []
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == num2 % i == 0 and i >= 4:
            common_denominators.append(i)
    return common_denominators


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Pixellizer",
        description="Pixellizer is a Python tool that transforms images into pixelated art by dividing them into customizable pixel blocks. It supports command-line arguments for input image, pixel size, and output path, making it ideal for creating retro-style visuals.",
        add_help="Specify the path to the input image. Based on the image you'll be provided with best options for the pixel size to choose from during runtime. The final image is saved to ./output directory."
    )
    parser.add_argument(
        "-p",
        "--path",
        type=str,
        help="Path to the input image.",
        required=True
    )
    args = parser.parse_args()

    source_img = Image.open(args.path)
    source_img = source_img.convert("RGB")

    width = source_img.width
    height = source_img.height
    print(f"Input image width: {width}", f"height: {height}")
    print(f"{find_all_common_denominators(width, height)}")
    single_pixel_size = int(
        input(
            "Choose final pixel size from the list above (default 4): "
        )
    )

    if single_pixel_size < 4:
        print("The minimum pixel size is 4.")
        exit(1)

    print(f"Chosen pixel size: {single_pixel_size}")

    output_img = Image.new("RGB", (width, height), (0, 0, 0))
    new_height = height // single_pixel_size
    new_width = width // single_pixel_size

    # loop with the step of the common denominator
    pixels = []
    for y in range(new_height):
        for x in range(new_width):
            pixels.append(
                Pixel(
                    single_pixel_size,
                    *source_img.getpixel(
                        (x * single_pixel_size, y * single_pixel_size)
                    ),
                )
            )

    # on the normal scaled image put big pixels
    for y in range(new_height):
        for x in range(new_width):
            pixels[y * new_width + x].stamp_pixel(
                output_img, x * single_pixel_size, y * single_pixel_size
            )

    output_img.save("output/output_image.png")
    print(f"Done! Image saved: ./output/output_image.png")

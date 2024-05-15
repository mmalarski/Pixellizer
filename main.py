from PIL import Image, ImageDraw
import math


def floor_to_step(value, step):
    return (value // step) * step


def ceil_to_step(value, step):
    return math.ceil(value / step) * step


def common_divisors(a, b):
    return [i for i in range(1, min(a, b) + 1) if a % i == b % i == 0]


def find_all_common_denominators(num1, num2):
    common_denominators = []
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == num2 % i == 0:
            common_denominators.append(i)
    return common_denominators


class Pixel:
    def __init__(self, pixel_size, r, g, b):
        if pixel_size < 4:
            raise ValueError("Pixel size must be at least 4")

        self.light_part_size = pixel_size - 1
        self.color = [r, g, b]

        # horizontal position
        self.red_start = 0
        self.red_width = self.light_part_size // 3
        self.green_start = self.red_width
        self.green_width = self.light_part_size // 3
        self.blue_start = self.green_start + self.green_width
        self.blue_width = self.light_part_size // 3
        if self.red_width + self.green_width + self.blue_width < pixel_size:
            self.blue_width = self.light_part_size - (self.red_width + self.green_width)

    def stamp_pixel(self, dst_image, x_dst, y_dst):
        for y in range(self.light_part_size):
            for r in range(self.red_start, self.red_width):
                dst_image.putpixel((x_dst + r, y_dst + y), (self.color[0], 0, 0))
            for g in range(self.green_start, self.green_start + self.green_width):
                dst_image.putpixel((x_dst + g, y_dst + y), (0, self.color[1], 0))
            for b in range(self.blue_start, self.blue_start + self.blue_width):
                dst_image.putpixel((x_dst + b, y_dst + y), (0, 0, self.color[2]))


if __name__ == "__main__":

    # load source image and convert source image to RGB
    img_name = "441329144_431002739569269_4988136876459337938_n.png"
    source_img = Image.open(img_name)
    source_img = source_img.convert("RGB")

    width = source_img.width
    height = source_img.height
    print(f"width: {width}", f"height: {height}")
    print(f"all common denominators: {find_all_common_denominators(width, height)}")

    # Choose the pixel size from the above list
    single_pixel_size = int(input("Choose the pixel size from the above list: "))
    print(f"Chosen pixel size: {single_pixel_size}")

    # Main loop
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

    output_img.save("wallpaper\output_image.png")  # Zapisz obrazek
    print(f"Done! Image saved: ./wallpaper/output_image.png")

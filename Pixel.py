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

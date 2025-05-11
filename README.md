# Pixellizer

## Overview

Pixellizer is a Python-based script designed to transform images into pixelated versions with customizable pixel sizes. It simplifies the process of creating pixel art by automating image resizing and pixelation while maintaining control over the output's visual style.

## How it works?

1. Provide the path to the image to process
```
py .\main.py -p '.\Frame 3.jpg'
```
2. The width and height of the image is read automatically and all the common denominators of the dimentions are listed. Those are the preferred pixel size that will cover the whole image without any of the RGB color imbalance.
3. Set the pixel size. 
```
Input image width: 3840 height: 1080
[4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120]
Choose final pixel size from the list above (default 4): 12
```
   - The best pixel size 4 but any multiple of 4 will do as well but the resolution will be lower. 
   - It's best to choose a number from the list. Otherwise the output image will have an empty line where the pixels wouldn't fit.
   - As long as the pixel size is greater than 4 any number will do. 
4. The final `output_image.png` is saved to `./output` directory.

## Notes
- The list of recommended pixel sizes are common denominators of width and height. Any multiple of 4 will result in the pixels components of equal size. Any other size - the blue color will be larger so as to fit the square dimensions of the pixel. 
- There is always `1px` size of black gap between pixels (check out the Graphics section for how an ideal pixel should look like).
- Any pixel size that is not the common denominator will result in a larger gap on the right hand side of the resulting image.

## Graphics

|The visualisation of a single pixel after the script processing |An image with the resolution of iPhone 15 Pro Max| The pixellized version|
|---|---|---|
|![The pixel](single_white_pixel.png)|![The originl image](./Frame%203.jpg)|![The pixellised version](./Frame%203%20pixellized.png)|
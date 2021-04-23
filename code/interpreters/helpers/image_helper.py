#!/usr/bin/env python3
from PIL import Image
import numpy
import os
from math import ceil

g_default_height_pixels = 400
g_default_width_pixels = 640

g_banner_height_pixels = 21
g_banner_width_pixels = 640


g_border_top_height_pixels = 4
g_border_bottom_height_pixels = 4

g_border_left_width_pixels = 4
g_border_right_width_pixels = 6

g_piece_height_pixels = 62
g_piece_width_pixels = 90

g_dosbox_header_height_pixels = 27
g_dosbox_header_width_pixels = 640

def process_game_image(source_image):
    image = source_image
    image = __crop_banner(image, g_dosbox_header_height_pixels, g_dosbox_header_width_pixels)
    image = __crop_banner(image, g_banner_height_pixels, g_banner_width_pixels)
    image = __crop_border(image, g_border_top_height_pixels, g_border_bottom_height_pixels, g_border_left_width_pixels, g_border_right_width_pixels)
    
    return image

def __crop_banner(source_image, banner_height_pixels, banner_width_pixels):
    imgwidth, imgheight = source_image.size
    box = (0, banner_height_pixels, banner_width_pixels, imgheight)
    print(box)

    result = source_image.crop(box)

    return result

def ____crop_border(source_image, border_top_height_pixels, border_bottom_height_pixels, border_left_width_pixels, border_right_width_pixels):
    imgwidth, imgheight = source_image.size
    box = (border_left_width_pixels, 
           border_top_height_pixels, 
           imgwidth - border_right_width_pixels, 
           imgheight - border_bottom_height_pixels)

    result = source_image.crop(box)

    return result

def slice_rectangles(image, height, width):
    iteration = 0

    imgwidth, imgheight = image.size
    cols = ceil(imgwidth // width)
    rows = ceil(imgheight // height)

    pieces = [[0]*cols for _ in range(rows)]
    print(pieces)

    for i in range(0, rows):
        for j in range(0, cols):
            #box – a 4-tuple defining the left, upper, right, and lower pixel coordinate.
            box = (j*width, i*height, j*width + width, i*height + height)
            
            result = image.crop(box)
            print(box)
            pieces[i][j] = result

    return pieces

if __name__ == "__main__":
    test_image_path = "../../../test/puzzle_1_example.png"
    resulting_path = "../../test/output"
    
    for f in os.listdir(resulting_path):
        os.remove(os.path.join(resulting_path, f))

    image = Image.open(test_image_path)
    image.save(os.path.join(resulting_path,"Image-Original.png"))

    image = __crop_banner(image, g_banner_height_pixels, g_banner_width_pixels)
    image.save(os.path.join(resulting_path,"Image-PostCropBanner.png"))

    image = __crop_border(image, g_border_top_height_pixels, g_border_bottom_height_pixels, g_border_left_width_pixels, g_border_right_width_pixels)
    image.save(os.path.join(resulting_path,"Image-PostCropBorder.png"))

    pieces = slice_rectangles(image, g_piece_height_pixels, g_piece_width_pixels)

    for x in range(len(pieces)):
        for y in range(len(pieces[x])):
            pieces[x][y].save(os.path.join(resulting_path,"Rect-%s-%s.png" % (x,y)))

    
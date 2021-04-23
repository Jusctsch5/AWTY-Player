#!/usr/bin/env python3

from helpers import content_grabber
from helpers import image_helper
import os

g_piece_height_pixels = 62
g_piece_width_pixels = 90

def interpret_touch_puzzle():
    image = content_grabber.capture_game_window()
    image = image_helper.process_game_image(image)
    return image

if __name__ == "__main__":
    resulting_path = "../../test/output"
    
    for f in os.listdir(resulting_path):
        os.remove(os.path.join(resulting_path, f))

    image = interpret_touch_puzzle()
    image.save(os.path.join(resulting_path,"Image-TouchPuzzle.png"))

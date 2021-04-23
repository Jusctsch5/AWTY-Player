import pygetwindow
import time
import os
import pyautogui
import PIL

# find new window title


def capture_game_window():
    titles = pygetwindow.getAllTitles()
    dosbox_title = None
    for title in titles:
        if "DOSBox 0.74" in title:
            dosbox_title = title

    if dosbox_title == None:
        raise IOError from None
    

    print(dosbox_title)

    window = pygetwindow.getWindowsWithTitle(dosbox_title)[0]
    if window == None:
        raise IOError from None
    print(window)
    # quarter of screen screensize

    # top-left
    #window.moveTo(0, 0)
    #time.sleep(3)
    window.activate()
    time.sleep(1)

    # save screenshot
    image = pyautogui.screenshot(region=(window.left,
                                         window.top,
                                         window.width,
                                         window.height))


    return image


if __name__ == "__main__":
    image = capture_game_window()
    resulting_path = "../../../test/output"
    image.save(os.path.join(resulting_path,"Image-Window.png"))

import sys

import mouse
from PIL import ImageGrab
import time
from pynput import keyboard


def take_screenshot():
    return ImageGrab.grab()

def in_game(image):
    pixel = image.getpixel((1800,200))
    if (pixel == (6,18,25)):
        return True
    return False

def building_available(image, coords):
    pixel = image.getpixel(coords)
    if(pixel == (164,126,75)):
        return True
    return False

def upgrade_available(image):
    pixel = image.getpixel((1650,300))
    if (pixel == (12,35,48)):
        return True
    return False

def upgrade_buildings(image):
    start_coords = (1680,415)
    coords = start_coords
    for n in range(1,8):
        if(building_available(image, coords)):
            mouse.move(coords[0], coords[1], True, 0)
            mouse.click()
        coords = (coords[0], coords[1] + 64)

def click_cookie():
    position = mouse.get_position()
    if(position != (300,500)):
        mouse.move(300, 500, True, 0)
    mouse.click()

def upgrade():
    scrrenshot = take_screenshot()
    if(upgrade_available(scrrenshot)):
        mouse.move(1650, 300, True, 0)
        mouse.click()
    upgrade_buildings(scrrenshot)


def on_press(key):
    global to_quit
    if key == keyboard.Key.esc:
        to_quit = not to_quit

def run_cookie_clicker():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    for n in range(1,10):
        if(in_game(take_screenshot()) == False):
            if(to_quit == True):
                print("planned quit")
                return
            print(to_quit)
            print("No cookie!")
            if(n==10):
                return
            time.sleep(1)
        else:
            break

    while(True):
        if(to_quit):
            print("planned quit")
            return
        upgrade()
        click_cookie()
        if(in_game(take_screenshot()) == False):
            break


to_quit = False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_cookie_clicker()


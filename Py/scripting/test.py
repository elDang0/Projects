from PIL import ImageGrab
import pyautogui
import time
from random import uniform
import keyboard


while True:
    # Get the current mouse position
    x, y = pyautogui.position()
    
    screen_width, screen_height = pyautogui.size()
    
    mid_x, mid_y = screen_width // 2, screen_height // 2
    mid_y -= 20
    image = ImageGrab.grab()
    px = image.load()
    

    # Check if the middle of the screen is red
    

    if keyboard.is_pressed('0'):  # Change '0' to any key you prefer00
        print(f"Color at ({x}, {y}): {px[x, y]}")



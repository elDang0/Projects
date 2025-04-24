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
    if px[mid_x, mid_y] == (156, 146, 43) or px[mid_x, mid_y] == (252, 122, 112) or px[mid_x,mid_y] == (177, 26, 16) or px[mid_x,mid_y] == (88, 6, 0) or px[mid_x,mid_y] == (231, 85, 74):
        print("Fishing")
        
        time.sleep(uniform(0.058, 0.038))  
        # Click the mouse
        pyautogui.rightClick()
        time.sleep(uniform(1, 1.73))
        pyautogui.rightClick()

    if keyboard.is_pressed('0'):  # Change '0' to any key you prefer0
        print(f"Color at ({mid_x}, {mid_y}): {px[mid_x, mid_y]}")



from PIL import ImageGrab
import time
from random import uniform
import mouse 
import keyboard
import random
import pyautogui


last_fish_time = time.time()
autocast = True
loop = True

def handle_y():
    time.sleep(1)

def handle_ae():
    global loop
    loop = False

def handle_enter():
    global autocast
    print(f"Toggle autocast to {not autocast}")
    autocast = not autocast

keyboard.add_hotkey('y', handle_y)
keyboard.add_hotkey('ä', handle_ae)
keyboard.add_hotkey('enter', handle_enter)

while loop:
    keyboard.press("shift")
    time.sleep(uniform(0.15, 0.5))
    # Randomly jump, move mouse, or move with WASD
    action = random.randint(1, 1000)
    if action == 1:
        keyboard.press('space')
        time.sleep(uniform(0.05, 0.15))
        keyboard.release('space')
    elif action == 2:
        dx = random.randint(-4, 4)
        dy = random.randint(-4, 4)
        x, y = pyautogui.position()
        pyautogui.moveTo(x + dx, y + dy, duration=uniform(0.05, 0.2))
    elif action == 3:
        wasd = random.choice(['w', 'a', 's', 'd'])
        keyboard.press(wasd)
        time.sleep(uniform(0.01, 0.02))
        keyboard.release(wasd)
        
    x, y = pyautogui.position()
    
    screen_width, screen_height = pyautogui.size()
    
    image = ImageGrab.grab()
    px = image.load()
    
    # for debuging
    #if keyboard.is_pressed('0'):  # Change '0' to any key you prefer0
    #    print(f"Color at ({x}, {y}): {px[x,y]}")
    #   print(f"Color at right pos {px[488,389]} ")
    
    
     
    if px[488,389] == (255, 85, 85):
        last_fish_time = time.time()
        time.sleep(uniform(0.015, 0.073))
        print("fish")
        
        # -- pull --
        mouse.press('right') 
        time.sleep(uniform(0.013, 0.14))  
        mouse.release('right')
        time.sleep(uniform(0.2, 1.1)) 
        
        # -- cast --
        if autocast:
            mouse.press('right')  
            time.sleep(uniform(0.023, 0.24))  
            mouse.release('right')
            
    elif time.time() - last_fish_time > 30 and autocast:
        print("No fish detected for 30 seconds, casting rod.")
        mouse.press('right')
        time.sleep(uniform(0.013, 0.14))
        mouse.release('right')
        last_fish_time = time.time()




import pyautogui
import time 

t_end = time.time() + 60 * 2
while time.time() < t_end:

    time.sleep(6)

    # clicks the lever
    pyautogui.click(button='right')

    time.sleep(6)

    pyautogui.click(button='right')
    

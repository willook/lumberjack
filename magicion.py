import time
import random
import pyautogui

def press(key, on, off):
    pyautogui.keyDown(key)
    time.sleep(on)
    pyautogui.keyUp(key)
    time.sleep(off)

print('Start in 2 seconds...')
time.sleep(2)
while True:
    left1 = abs(random.normalvariate(0.05, 0.005)) * 1.20
    left2 = abs(random.normalvariate(0.1, 0.02)) / 4
    press('left', left1, left2)
    right1 = abs(random.normalvariate(0.05, 0.005))
    right2 = abs(random.normalvariate(0.1, 0.02))
    press('right', right1, right2)
    # pyautogui.press("Shift")
    for i in range(5):
        pyautogui.press('ctrl')
        time.sleep(abs(random.normalvariate(15, 4)))
    
    
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
    left1 = abs(random.normalvariate(0.05, 0.005)) * 1.22
    left2 = abs(random.normalvariate(0.1, 0.02)) / 4
    rest = abs(random.normalvariate(10, 2)) / 10
    attack = abs(random.normalvariate(10, 2))
    press('left', left1, left2)
    press('ctrl', attack, rest)
    
    right1 = abs(random.normalvariate(0.05, 0.005))
    right2 = abs(random.normalvariate(0.1, 0.02))
    rest = abs(random.normalvariate(10, 2)) / 10
    attack = abs(random.normalvariate(40, 5))
    press('right', right1, right2)
    press('ctrl', attack, rest)
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

pyautogui.hotkey('alt','tab')
pyautogui.hotkey('f11')
time.sleep(.5)

fight = pyautogui.locateOnScreen('fight.png' , confidence = .95)
if not fight:
    pyautogui.moveTo(x=1263,y=590)
    pyautogui.scroll(-20, x=1263, y=590)
    time.sleep(3)
    fight = pyautogui.locateOnScreen('fight.png' , confidence = .95)
counter = 0
while fight:
    fight_point = pyautogui.center(fight)
    click(fight_point[0],fight_point[1])
    click(fight_point[0],fight_point[1])
    time.sleep(1.5)
    
    start = pyautogui.locateOnScreen('start.png', confidence = .95)
    start_point = pyautogui.center(start)
    click(1361, 990)
    click(1361, 990)
    time.sleep(1)
    buyflags = pyautogui.locateCenterOnScreen('buyflags.png', confidence = .95)
    if buyflags:
        click(buyflags[0],buyflags[1])
        click(buyflags[0],buyflags[1])
        click(buyflags[0],buyflags[1])
        time.sleep(.5)
        click(start_point[0],start_point[1])
        click(start_point[0], start_point[1])
    time.sleep(10)
    
    
                     
    skip = pyautogui.locateCenterOnScreen('skip.png', confidence = .95)
    click(skip[0],skip[1])
    click(skip[0],skip[1])
    time.sleep(1)
    auto = pyautogui.locateCenterOnScreen('auto.png', confidence = .95)
    click(auto[0],auto[1])
    click(auto[0],auto[1])
    click(auto[0],auto[1])
    time.sleep(20)
    
    skip = pyautogui.locateCenterOnScreen('skip.png', confidence = .95)
    click(skip[0],skip[1])
    click(skip[0],skip[1])
    time.sleep(3)
    
    confirm = pyautogui.locateCenterOnScreen('confirm.png', confidence = .95)
    click(1754, 991)
    click(1754, 991)
    time.sleep(3)
    
    counter += 1
    fight = pyautogui.locateOnScreen('fight.png' , confidence = .95)
    if not fight:
        pyautogui.scroll(-5, x=1263, y=590)
        time.sleep(3)
        fight = pyautogui.locateOnScreen('fight.png' , confidence = .95)
print('did ', counter, 'npc battles')
    

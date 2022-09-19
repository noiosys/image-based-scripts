from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.4)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

pyautogui.hotkey('alt','tab')
pyautogui.hotkey('f11')
time.sleep(.5)
percentages = pyautogui.locateOnScreen('percentages.png',confidence=.95,region=(1100, 581, 100, 162))
print(percentages)

while not percentages:
    
    changesubs = pyautogui.locateOnScreen('changesubs.png', confidence = .95)
    changesubs_point = pyautogui.center(changesubs)
    click(changesubs_point[0],changesubs_point[1])
    click(changesubs_point[0],changesubs_point[1])
    
    click(363, 576)
    
    percentages = pyautogui.locateOnScreen('percentages.png',confidence=.95, region=(1100, 581, 100, 162))
    if percentages:
        break
    select = pyautogui.locateOnScreen('select.png', confidence = .95)
    select_point = pyautogui.center(select)
    click(select_point[0],select_point[1])
    click(select_point[0],select_point[1])
    
    
    time.sleep(.5)
percentages_point = pyautogui.center(percentages)
print(percentages_point)
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for  seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    
while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(532, 400)[0] == 0:
        click(532, 400)
    if pyautogui.pixel(632, 400)[0] == 0:
        click(632, 400)
    if pyautogui.pixel(732, 400)[0] == 0:
        click(732, 400)
    if pyautogui.pixel(832, 400)[0] == 0:
        click(832, 400)

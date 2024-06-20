import keyboard
from pyautogui import *
import pyautogui
import time
import numpy as np
import random
import win32api
import win32con
import os
import sys
import psutil


def action(x, y):
    time.sleep(0.1)
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


action(172, 943)
time.sleep(0.1)
keyboard.press_and_release('ctrl + v')
time.sleep(0.1)
keyboard.press_and_release('enter')
time.sleep(0.1)
action(155, 417)
time.sleep(0.1)
keyboard.press_and_release('ctrl + v')
time.sleep(0.1)
keyboard.press_and_release('enter')
time.sleep(0.1)
action(1444, 417)
time.sleep(0.1)
keyboard.press_and_release('ctrl + v')
time.sleep(0.1)
keyboard.press_and_release('enter')
time.sleep(0.1)
action(1475, 932)
time.sleep(0.1)
keyboard.press_and_release('ctrl + v')
time.sleep(0.1)
keyboard.press_and_release('enter')

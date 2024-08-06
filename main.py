from pyautogui import *
import pyautogui
import time
import cv2
import pyscreeze

defiTime = 37

def countdown():
    global defiTime
    while defiTime != -1:
        print(defiTime)
        time.sleep(1)
        defiTime -= 1

    time.sleep(10)
    defiTime = 37

while True:
    try:
        image_location = pyautogui.locateOnScreen("D:\\Desktop\\Timer\\kakaka.png", region=(900, 0, 115, 115), grayscale=True, confidence=0.45)
        if image_location is not None:
            countdown()
        else:
            print("None")
    except pyautogui.ImageNotFoundException:
        print("Image not found")
    time.sleep(1)

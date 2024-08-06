import pyautogui

i = input()
while True:
    if(i == "i"):
        im1 = pyautogui.screenshot(region=(900,0,115,115))
        im1.save(r"D:\Desktop\Timer\savedimage.png")

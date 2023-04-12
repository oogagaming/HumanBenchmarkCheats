import pyautogui

blue = (63, 133, 208)
green = (95, 220, 109)
red = (198, 37, 52)



last = ()

while True:
    # screenshot = pyautogui.screenshot()

    pix = pyautogui.pixel(355, 355)
    # print(pix)
    if pix == blue and last != blue:
        pyautogui.moveTo(355,355)
        pyautogui.click()
    elif pix == green:
        # pyautogui.moveTo(355,355)
        pyautogui.click()
    
    last = pix
        
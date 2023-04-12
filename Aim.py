import pyautogui

x, y, width, height = 615, 350, 690, 205

color = (159, 194, 232)

error_margin_left = 2

for i in range(31):
    stop = False
    s = pyautogui.screenshot(region=(x, y, width, height))

    for i in range(s.width):
        for j in range(s.height):
            if s.getpixel((i, j)) == color:
                pyautogui.click(i+x+error_margin_left, j+y)
                stop = True
                break
        if stop:
            break

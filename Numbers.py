import PIL
import pyautogui
import pytesseract
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def getNum(index):
    # Set the coordinates of the top-left corner of the screenshot and its width and height.
    num_x, num_y, num_width, num_height = 0, 300, 1900, 200

    # Take a screenshot of the specified part of the screen.
    screenshot = pyautogui.screenshot(region=(num_x, num_y, num_width, num_height))

    img = screenshot.convert("L") #Convert to gray-scale
    img = PIL.ImageOps.invert(img) #Invert
    size_factor = 5 #Size factor to resize image
    img = img.resize((img.size[0] * size_factor, img.size[1] * size_factor))
    # Extract text from the screenshot.
    text = pytesseract.image_to_string(img,config='-c tessedit_char_whitelist=0123456789 --psm 10')
    # img.save(str(index)+".png")
    return text


def getTitle():

    # Set the coordinates of the top-left corner of the screenshot and its width and height.
    x, y, width, height = 450, 350, 870, 130

    # Take a screenshot of the specified part of the screen.
    title = pyautogui.screenshot(region=(x, y, width, height))

    # Extract text from the screenshot.
    text = pytesseract.image_to_string(title,config='--psm 10')

    return text

def getAnswerScreen():

    # Set the coordinates of the top-left corner of the screenshot and its width and height.
    x, y, width, height = 450, 250, 870, 80

    # Take a screenshot of the specified part of the screen.
    title = pyautogui.screenshot(region=(x, y, width, height))

    # Extract text from the screenshot.
    text = pytesseract.image_to_string(title,config='--psm 10')

    return text

print(getAnswerScreen())

for i in range(30):
    while getTitle() == "Number Memory\n":
        time.sleep(0.1)
        pyautogui.click(x=948, y=567)

    time.sleep(0.1)
    num = getNum(i)

    print("num", num)

    while getAnswerScreen() != "What was the number?\n":
        # print("wait for asnwer screen")
        pass
    time.sleep(0.1)
    pyautogui.write(num) # \n after number so enter is presssed
    time.sleep(0.1)
    pyautogui.click(x=948, y=567)
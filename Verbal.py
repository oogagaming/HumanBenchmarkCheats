import pyautogui
import pytesseract

# Set the coordinates of the top-left corner of the screenshot and its width and height.
x, y, width, height = 500, 350, 950, 100

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

words = []
last = ""

while True:

    # Take a screenshot of the specified part of the screen.
    screenshot = pyautogui.screenshot(region=(x, y, width, height))

    # Extract text from the screenshot.
    text = pytesseract.image_to_string(screenshot)
    text = text[:-1]
    if last != text:

        if text in words:
            pyautogui.moveTo(880, 499)
            pyautogui.click()
        else:
            words.append(text)
            pyautogui.moveTo(1019, 497)
            pyautogui.click()

    
    last = text
    
# New
# Point(x=1019, y=497)

#seen
#Point(x=880, y=499)
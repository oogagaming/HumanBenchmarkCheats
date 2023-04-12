import time
import pyautogui
import pytesseract


# Set the coordinates of the top-left corner of the screenshot and its width and height.
x, y, width, height = 0, 370, 1900, 180

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

words = []
last = ""

time.sleep(2)

# Take a screenshot of the specified part of the screen.
screenshot = pyautogui.screenshot(region=(x, y, width, height))

# Extract text from the screenshot.
text = pytesseract.image_to_string(screenshot)

text = text.replace("\n", " ")
text = text.replace("|", "I")
print(repr(text))

pyautogui.write(text, 0.01)

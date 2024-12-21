import pyautogui
import pytesseract
from PIL import Image

# Set the path to the Tesseract executable if required (Windows)
# Example: pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define the region to capture (left, top, width, height)
region = (300, 475, 550, 550)  # Adjust the coordinates as needed

# Capture the specified screen area
screenshot = pyautogui.screenshot(region=region)

screenshot.save("test.png")

# Use Tesseract to extract text
text = pytesseract.image_to_string(screenshot)

print("Detected Text:")
print(text)

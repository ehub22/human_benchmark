from PIL import Image
import pytesseract
import numpy as np
import pyautogui
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\E 9\AppData\Local\Tesseract-OCR\tesseract.exe'

filename = 'img.png'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)
pyautogui.write(text)
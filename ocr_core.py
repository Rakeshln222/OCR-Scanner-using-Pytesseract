# ocr_core.py
import cv2
import numpy as np
import pytesseract
from PIL import Image

# if windows: set path here
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def load_image(path):
    return cv2.imread(path)

def preprocess(image):
    # 1. convert to gray
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 2. increase resolution (optional)
    gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    # 3. denoise
    gray = cv2.medianBlur(gray, 3)
    # 4. adaptive threshold
    th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY, 31, 11)
    return th

def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    M = cv2.getRotationMatrix2D((w//2, h//2), angle, 1.0)
    return cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

def ocr_image(image, lang='eng'):
    # config: OEM 3 (default LSTM), PSM 3 (auto) - tweak per doc type
    config = r'--oem 3 --psm 3'
    pil = Image.fromarray(image)
    text = pytesseract.image_to_string(pil, lang=lang, config=config)
    return text

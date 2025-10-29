# OCR Scanner using Pytesseract
## Overview
Extract text from images using OpenCV preprocessing + Tesseract OCR.

## Setup
1. Install Tesseract (link & instructions)
2. pip install -r requirements.txt
3. (Windows) set TESSERACT path in ocr_core.py

## Run
CLI: python main.py samples/doc1.jpg --deskew
GUI:  python gui.py

## Notes
- Use 300 DPI for scanned docs
- Try --psm and --oem configs for different layouts

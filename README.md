
# 🧠 OCR Scanner – Extract Text from Images using Pytesseract

## 📖 Overview
The **OCR Scanner** is a Python-based application that extracts readable text from images using the **Tesseract OCR engine** via the **Pytesseract** library.  
It supports preprocessing techniques using **OpenCV** to improve text recognition accuracy on various image types such as scanned documents, printed pages, and receipts.

---

## 🎯 Key Features
- 🖼️ Image Preprocessing (grayscale, noise removal, thresholding, deskewing)
- 🧩 OCR Text Extraction using Google’s Tesseract engine
- 📂 Multi-format support (`.jpg`, `.png`, `.tiff`, `.pdf`)
- 💬 Output export in `.txt` or `.docx` format
- ⚙️ Configurable OCR parameters (OEM/PSM modes)
- 🖥️ GUI support (Tkinter) and CLI mode for automation

---

## 🧰 Technologies Used
| Component | Description |
|------------|-------------|
| **Language** | Python 3.x |
| **OCR Engine** | Tesseract OCR |
| **Libraries** | OpenCV, Pytesseract, Pillow, NumPy |
| **GUI (Optional)** | Tkinter |

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/OCR-Scanner.git
cd OCR-Scanner
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Install Tesseract Engine

* **Windows:**
  Download and install from [Tesseract OCR GitHub](https://github.com/tesseract-ocr/tesseract).
  Then set the path in your Python script:

  ```python
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  ```
* **Linux / macOS:**

  ```bash
  sudo apt install tesseract-ocr
  ```

---

## 🚀 Usage

### ▶️ Command-Line Mode

```bash
python main.py --image path/to/image.jpg --lang eng --deskew
```

### 🪟 GUI Mode (Optional)

```bash
python gui_app.py
```

---

## 🔍 Workflow Overview

```text
Input Image
   │
   ▼
Preprocessing (Grayscale → Denoise → Threshold → Deskew)
   │
   ▼
Tesseract OCR Engine (via Pytesseract)
   │
   ▼
Postprocessing (Cleanup → Spellcheck)
   │
   ▼
Output Text (.txt / .docx)
```

---

## 📊 Results & Performance

| Test Case    | Input Type     | Accuracy (CER) | Notes                 |
| ------------ | -------------- | -------------- | --------------------- |
| Printed text | 300 DPI Scan   | 97–99%         | Excellent             |
| Photos       | Mobile Capture | 90–94%         | Preprocessing helps   |
| Receipts     | Faded Print    | 85–90%         | Thresholding required |
| Handwriting  | Notes          | <70%           | Limited by Tesseract  |

---

## 🌍 Applications

* Document digitization & archival
* Invoice / receipt scanning
* Data entry automation
* Accessibility for visually impaired users

---

## ⚠️ Limitations

* Struggles with **handwritten or artistic fonts**
* Sensitive to **blurred or skewed images**
* No built-in table or layout recognition

---

## 🧩 Future Enhancements

* Integrate **EasyOCR** or **PaddleOCR** for handwriting support
* Add **Flask API** for cloud-based OCR service
* Implement **PDF-to-searchable PDF** conversion
* Advanced **layout detection and correction**

---

## 🏁 Conclusion

This project demonstrates a modular and efficient OCR pipeline using Python, OpenCV, and Tesseract.
By combining image preprocessing and accurate OCR extraction, the system provides a reliable tool for real-world document recognition.

---

## 📚 References

* [Tesseract OCR Documentation](https://github.com/tesseract-ocr/tesseract)
* [Pytesseract PyPI](https://pypi.org/project/pytesseract/)
* [OpenCV Documentation](https://docs.opencv.org/)
* [EasyOCR GitHub](https://github.com/JaidedAI/EasyOCR)

---

### 👨‍💻 Author

**Rakesh L N**
🎓 Computer Science Engineer | 💡 Python Developer | 🚀 AI & Automation Enthusiast

```
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


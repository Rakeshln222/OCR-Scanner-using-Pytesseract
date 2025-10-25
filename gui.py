# gui.py (very basic)
import tkinter as tk
from tkinter import filedialog, scrolledtext
from ocr_core import load_image, preprocess, ocr_image

def open_file():
    path = filedialog.askopenfilename()
    if not path: return
    img = load_image(path)
    proc = preprocess(img)
    text = ocr_image(proc)
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, text)

root = tk.Tk()
root.title("OCR Scanner")
btn = tk.Button(root, text="Open Image", command=open_file)
btn.pack()
text_area = scrolledtext.ScrolledText(root, width=80, height=20)
text_area.pack()
root.mainloop()

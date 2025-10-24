# main.py
import argparse
from ocr_core import load_image, preprocess, deskew, ocr_image

def main():
    p = argparse.ArgumentParser()
    p.add_argument("image")
    p.add_argument("--lang", default="eng")
    p.add_argument("--deskew", action="store_true")
    args = p.parse_args()

    img = load_image(args.image)
    proc = preprocess(img)
    if args.deskew:
        proc = deskew(proc)
    text = ocr_image(proc, lang=args.lang)
    print(text)

    out = args.image.rsplit(".",1)[0] + ".txt"
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)
    print("Saved ->", out)

if __name__ == "__main__":
    main()
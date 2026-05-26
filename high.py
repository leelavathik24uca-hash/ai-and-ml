from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Full image path
image = Image.open(r"C:\Users\ELCOT\OneDrive\Pictures\pic\krish.jpeg")

text = pytesseract.image_to_string(image)

print(text)
import os
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
config = ('-l urd --oem 1 --psm 7')

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    
    text = pytesseract.image_to_string(Image.open(filename),config=config)
    return text



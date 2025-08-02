import easyocr
import re

reader = easyocr.Reader(['en'], gpu=False)

def recognize_plate_text(image_path: str) -> str:
    result = reader.readtext(image_path)
    
    # Combine all text results
    text = " ".join([r[1] for r in result])

    # Clean and format based on Indian number plate regex
    matches = re.findall(r"[A-Z]{2}[0-9]{1,2}[A-Z]{1,2}[0-9]{3,4}", text.replace(" ", "").upper())
    
    return matches[0] if matches else text.strip()

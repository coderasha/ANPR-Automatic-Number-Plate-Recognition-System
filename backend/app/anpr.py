import cv2
import numpy as np
from PIL import Image
from io import BytesIO
from ultralytics import YOLO
import easyocr

model = YOLO("best.pt")
reader = easyocr.Reader(['en'])

def extract_number_plate(file_bytes):
    image = Image.open(BytesIO(file_bytes)).convert("RGB")
    image_np = np.array(image)
    results = model.predict(source=image_np, conf=0.3, verbose=False)

    if not results or not results[0].boxes:
        return "Plate Not Detected"

    box = results[0].boxes.xyxy[0].cpu().numpy().astype(int)
    x1, y1, x2, y2 = box
    cropped = image_np[y1:y2, x1:x2]

    gray = cv2.cvtColor(cropped, cv2.COLOR_RGB2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    thresh = cv2.adaptiveThreshold(gray, 255,
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 11, 2)

    result = reader.readtext(thresh)
    if result:
        return result[0][-2].replace(" ", "").upper()
    return "Plate Not Detected"

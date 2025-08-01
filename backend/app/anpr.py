import cv2
import numpy as np
import pytesseract
from io import BytesIO
from PIL import Image
from ultralytics import YOLO

model = YOLO('backend/models/yolov8_anpr.pt')

def extract_number_plate(image_bytes):
    image = Image.open(BytesIO(image_bytes)).convert('RGB')
    frame = np.array(image)

    results = model(frame)
    for box in results[0].boxes.xyxy:
        x1, y1, x2, y2 = map(int, box)
        roi = frame[y1:y2, x1:x2]
        text = pytesseract.image_to_string(roi, config='--psm 8')
        return text.strip()
    return "Plate Not Detected"

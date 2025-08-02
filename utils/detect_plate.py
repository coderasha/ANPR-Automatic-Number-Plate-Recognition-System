from ultralytics import YOLO
import cv2

model = YOLO("yolov8/best.pt")  # replace with your model path

def detect_and_crop_plate(image_path):
    results = model(image_path)
    for r in results:
        for box in r.boxes.xyxy:
            x1, y1, x2, y2 = map(int, box)
            img = cv2.imread(image_path)
            cropped = img[y1:y2, x1:x2]
            return cropped

import cv2  
from ultralytics import YOLO  

model = YOLO("models/yolov8_plate.pt")  

def detect_plate(img_path):  
    img = cv2.imread(img_path)  
    results = model.predict(img)  
    plates = []  
    for box in results[0].boxes.xyxy:  
        x1, y1, x2, y2 = map(int, box)  
        plate_img = img[y1:y2, x1:x2]  
        plates.append(plate_img)  
    return plates  
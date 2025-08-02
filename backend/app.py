from flask import Flask, request, jsonify  
from plate_detection import detect_plate  
from image_enhancement import enhance_plate  
from ocr_processing import extract_text  
import os  

app = Flask(__name__)  

@app.route('/upload', methods=['POST'])  
def upload():  
    file = request.files['image']  
    file.save("static/upload.jpg")  
    plates = detect_plate("static/upload.jpg")  
    if plates:  
        enhanced = enhance_plate(plates[0])  
        plate_text = extract_text(enhanced)  
        return jsonify({"plate": plate_text})  
    return jsonify({"error": "No plate detected"})  

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=5000)  
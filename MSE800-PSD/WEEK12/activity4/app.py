import os

from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder='.')
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'svg'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/', methods=['GET', 'POST'])
def load_image():
    image_url = url_for('static', filename='sample.svg')
    message = 'Upload an image to display it here.'

    if request.method == 'POST':
        file = request.files.get('image')
        if file and file.filename:
            if allowed_file(file.filename):
                os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                image_url = url_for('static', filename=f'uploads/{filename}')
                message = f'Showing {filename}'
            else:
                message = 'Please upload a valid image file.'

    return render_template('loadimage.html', image_url=image_url, message=message)


if __name__ == '__main__':
    app.run(debug=True)

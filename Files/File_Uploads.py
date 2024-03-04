import os
from flask import Flask, request, render_template

app = Flask(__name__)
UPLOAD_FOLDER = '/home/pratiyushp/downloads/Codes/PythonWorkspace/RestAPIDemo/rest_app_practice/Files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'the_file' not in request.files:
            return 'No file path'

        f = request.files['the_file']

        if f.filename == '':
            return 'No selected file'

        f.save(os.path.join(UPLOAD_FOLDER, 'uploaded_file.txt'))

        return 'File Successfully uploaded'

    # return '''
    # <!doctype html>
    # <title>Upload new File</title>
    # <h1>Upload new File</h1>
    # <form method="post" enctype="multipart/form-data">
    #   <input type="file" name="the_file">
    #   <input type="submit" value="Upload">
    # </form>
    # '''

    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
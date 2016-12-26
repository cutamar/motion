import os, json
from flask import Flask, send_file, after_this_request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/delete-all")
def deleteImages():
    for file in os.listdir('Captured/'):
        if file.endswith('.jpg'):
            os.remove('Captured/' + file)
    return "ok"

@app.route("/get-images")
def getImages():
    filesList = []
    filesList += [each for each in os.listdir('Captured/') if each.endswith('.jpg')]
    return json.dumps(filesList)

@app.route('/get-images/<filename>')
def download_file(filename):
    file_path = 'Captured/' + filename
    @after_this_request
    def remove_file(response):
        try:
            os.remove(file_path)
        except Exception as error:
            app.logger.error("Error removing or closing downloaded file handle", error)
        return response
    return send_file(file_path, as_attachment=True, attachment_filename=filename)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8081)
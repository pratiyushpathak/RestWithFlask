from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Index Page</h1>"

@app.route('/hello')
def hello():
    return 'Hello'

if __name__ == '__main__':
    app.debug=True
    app.run()
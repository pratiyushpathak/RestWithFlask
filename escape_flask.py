from markupsafe import escape
from flask import Flask

app = Flask(__name__)
@app.route('/<name>')

def hello(name):
    return f"Hello, {escape(name)}!"

if __name__ == '__main__':
    app.run()

# pass the name in the url
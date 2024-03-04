from flask import Flask, request

app = Flask(__name__)

@app.route('/hello', methods=['POST'])
def index():
    return 'Hello, POST request received! now'

with app.test_request_context('/hello', method='POST'):
    assert request.path == '/hello'
    assert request.method == 'POST'

if __name__ == '__main__':
    app.run(debug=True)
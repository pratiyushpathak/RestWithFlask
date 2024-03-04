from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def get_users():
    print("Using jsonify")
    users = [{'id': 1, 'username': 'pratiyush'},
             {'id': 2, 'username': 'pathak'}]
    return jsonify({'users': users})


if __name__ == '__main__':
    app.run(debug=True)
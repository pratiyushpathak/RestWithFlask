from flask import Flask

app = Flask(__name__)

@app.route('/about/')
def about():
    return '<h1>About Page</h1>'

@app.route('/products')
def products():
    return '<h1>Products Page</h1>'


if __name__ == '__main__':
    app.run()
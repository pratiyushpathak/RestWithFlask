from flask import Flask, make_response, render_template

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('index.html'))
    resp.headers['X-Something'] = 'A value'
    return resp

if __name__ == '__main__':
    app.run(debug=True)
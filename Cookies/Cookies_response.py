from  flask import Flask, make_response, render_template

app = Flask(__name__)

@app.route('/')
def index():
    resp = make_response(render_template('index.html', username= 'the_username'))
    resp.set_cookie('username', 'the_username')
    return resp

if __name__ == '__main__':
    app.run(debug=True)
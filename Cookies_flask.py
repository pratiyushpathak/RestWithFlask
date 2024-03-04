from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')

    if username:
        return f'Hello {username}'

    else:
        response = make_response('Unauthorized', 401)
        response.headers['Location'] = '/login'
        print(response.headers)
        return response

@app.route('/login')
def login():
    return 'This is a Login Page'

if __name__ == '__main__':
    app.run(debug=True)
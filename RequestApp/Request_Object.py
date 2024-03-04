from flask import Flask, request, render_template

app = Flask(__name__)

def valid_login(username, password):
    return username == 'admin' and password == 'password'

def log_the_user(username):
    return f'Logged in as {username}'

@app.route('/login', methods = ['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user(request.form['username'])

        else:
            error = 'Invalid username/Password'
    return render_template('login.html', error= error)

if __name__ == '__main__':
    app.run(debug=True)
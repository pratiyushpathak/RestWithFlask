from flask import Flask, session, request, redirect, url_for

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    app.logger.debug('index called')
    if 'username' in session:
        return f'Logged u as {session["username"]}'
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        app.logger.debug('user logged in')
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout')
def logout():
    session.pop('username', None)
    app.logger.debug('user logged out')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

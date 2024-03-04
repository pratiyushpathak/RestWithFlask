
from flask import Flask, request

app = Flask(__name__)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return 'do_the_login()'
#     else:
#         return 'show_the_login_form()'
#

@app.get('/login')
def login_get():
    return 'Its a GET Request'

@app.post('/login')
def login_post():
    return 'Its a POST Request'

if __name__ == '__main__':
    app.run()
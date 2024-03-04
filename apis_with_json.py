from flask import Flask, url_for, send_from_directory, abort

app = Flask(__name__)

UPLOAD_FOLDER = '/home/pratiyushp/downloads/Codes/PythonWorkspace/RestAPIDemo/rest_app_practice/uploads'


class User:
    def __init__(self, username, theme, image):
        self.username = username
        self.theme = theme
        self.image = image

    def to_json(self):
        return {
            'username': self.username,
            'theme': self.theme,
            'image': self.image
        }


def get_current_user():
    return User('current_user', "light", 'imag.jpeg')


def get_all_users():
    return [
            User("user1", "dark", "user1_image.jpg"),
            User("user2", "light", "user2_image.jpg")
            ]


@app.route('/me')
def me_api():
    user = get_current_user()
    return {
        'username': user.username,
        'theme': user.theme,
        'image': url_for('user_image', filename=imag.jpeg)
    }


@app.route('/user_image/<filename>')
def user_image(filename):
    try:
        return send_from_directory(app.config[UPLOAD_FOLDER], filename)
    except FileNotFoundError:
        abort(404)


@app.route('/users')
def users_api():
    users = get_all_users()
    return [user.to_json() for user in users]


if __name__ == '__main__':
    app.run(debug=True)

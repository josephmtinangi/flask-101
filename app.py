from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index'


@app.route('/about')
def about():
    return 'About'


@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'

    return render_template('login.html', error=error)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


def valid_login(username, password):
    return True


def log_the_user_in(username):
    return render_template('home.html', username=username)


if __name__ == '__main__':
    app.run(debug=True)

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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'do the login'
    else:
        return 'show login form'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


with app.test_request_context('/hello', method='POST'):
    assert request.path == '/hello'
    assert request.method == 'POST'

if __name__ == '__main__':
    app.run(debug=True)

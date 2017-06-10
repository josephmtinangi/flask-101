from flask import Flask, session, redirect, url_for, escape, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


app.secret_key = '\x91(a`D\x19{V\xef \xaf\xddH\xe9\x14sFErc\xafk\x91\xbd'

if __name__ == '__main__':
    app.run(debug=True)

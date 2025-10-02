from flask import Flask,redirect,url_for

app = Flask(__name__)
@app.route('/')
def home():
    return "<h1>Hello</h1> Hello, This is the first flask project."

@app.route('/<name>')
def user(name):
    return f"Hello, {name}!"

@app.route('/admin')
def admin():
    return redirect(url_for('user'))
if __name__ == '__main__':
    app.run()
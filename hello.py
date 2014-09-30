from flask import Flask
app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

def hello_world():
    return 'Hello world!'

if __name__ == '__main__':
    app.debug = True
    app.run()
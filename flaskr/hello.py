from flask import Flask,render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
@app.route("/player-name/<name>")
def hello_world(name=None):
    return render_template('index.html', name=name)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

    from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'POST REQUEST CALLED'
    else:
        return 'GET REQUESET CALLED'
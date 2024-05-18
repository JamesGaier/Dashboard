from flask import Flask, redirect, render_template, g
from markupsafe import escape
import pymongo
from pymongo import MongoClient
from data import players, player_index_first_name
import requests
import shutil
app = Flask(__name__, static_url_path='/static')

@app.route("/")
@app.route("/player-name/<name>")
def hello_world(name=None):
    return render_template('index.html', name=name)

@app.route("/player-db/<player_name>", methods=["POST"])
def send_playername(player_name=None):
    player = {'name' : player_name}
    collection.insert_one(player)
    return f"<p>Sent player name {player_name}</p>"

@app.route('/redirect')
def index():
    return redirect(url_for('login'))

@app.route("/me")
def me_api():
    # example logger
    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

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


class HTTPRequest:
    def get(self, endpoint):   
        response = requests.get(endpoint)
        return response

@app.route('/player/<name>', methods=['GET'])
def get_player(name):
    player_id = 0
    for player in players:
        if player[player_index_first_name].lower() == name:
            player_id = player[0]
    
    url = f'https://cdn.nba.com/headshots/nba/latest/1040x760/{player_id}.png'
    response = requests.get(url, stream=True)
    with open(f'flaskr/static/{player_id}.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    
    return 'OK'
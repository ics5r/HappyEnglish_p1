import sqlite3
import json
import flask
from . import db_service, create_db, fill_db

app = flask.Flask(__name__)


@app.route('/search.html', methods=['POST', 'GET'])
def search():
    if flask.request.method == 'POST':
        con = sqlite3.connect('../HappyEnglishSubtitles.db')
        phrase = flask.request.form['phrase']
        fragments = db_service.get_text(con, phrase)
        fragments_json = json.dumps(fragments)
        return flask.Response(fragments_json)
    return flask.render_template('search.html')


# @app.route('/index')
# def index():
#     return flask.render_template("index.html")


@app.route('/index', methods=['POST', 'GET'])
def index():
    if flask.request.method == "POST":
        if 'create_database' in flask.request.form:
            create_db.create_db()
            return 'Database was created'
        elif 'fill_database' in flask.request.form:
            fill_db.fill_db()
            return 'Info was uploaded to database'
        else:
            return flask.redirect(flask.url_for('search'))
    return flask.render_template("index.html")


# def main():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return 'abc'
#     return render_template('login.html', error=error)


app.run()

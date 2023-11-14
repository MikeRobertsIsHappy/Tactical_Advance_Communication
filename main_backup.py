from flask import Flask, redirect, url_for, render_template, request, session
import logging
import jackalbot as jb
from datetime import datetime, timedelta
from pathlib import Path
import pathlib
import os.path



app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=15)

# first step is to get the users name.  This initiates the session
@app.route("/", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		session.permanent = True
		user = request.form["nm"]
		session["user"] = user
		session['game_state_data'] = 'starting new session'

		# define log name and save to session cookie
		now = datetime.now().strftime("%Y_%m_%d_%H_%M")
		app_directory = pathlib.Path().absolute()
		app_directory = os.path.join(str(app_directory), "game_play_logs")
		log_filename = '%s_play.txt' % now
		play_log_file_path = os.path.join(app_directory, log_filename)
		session['play_log_file_path'] = play_log_file_path
		
		return redirect(url_for("game"))
	else:
		if "user" in session:
			return redirect(url_for("game"))

		return render_template("login.html")

@app.route("/game")
def game():
	if "user" in session:
		user = session["user"]
		return render_template("index.html")
	else:
		return redirect("/")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get('msg')
    bot_response, new_game_state_data  = jb.jackalbot_response(user_input, session)
    session['game_state_data'] = new_game_state_data
    return bot_response

@app.route("/moreinfo", methods=["POST"])
def moreinfo():
	if request.method == "POST":
		if "user" in session:
			return redirect(url_for("game"))
		return render_template("login.html")
	else:
		return render_template("moreinfo.html")


@app.route("/logout")
def logout():
	session.pop("user", None)
	return redirect(url_for("login"))



if __name__ == "__main__":
    now = datetime.now().strftime("%Y_%m_%d_%H_%M")
    app_directory = pathlib.Path().absolute()
    app_directory = os.path.join(str(app_directory), "game_play_logs")
    log_filename = '%s_log.txt' % now
    log_file_path = os.path.join(app_directory, log_filename)

    logging.basicConfig(
        filename=log_file_path,
        level=logging.INFO,
        format='%(asctime)s.%(msecs)d %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    app.run(host='127.0.0.1', debug=True, port=8080)  #, debug=True, threaded=True   	 
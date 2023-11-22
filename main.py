from flask import Flask, redirect, url_for, render_template, request, session
import logging
#import jackalbot as jb
import tac_conductor as tac_conductor
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
		user = request.form.get("username")  # Retrieve username from form input
		if not user: return "No username provided", 400  # Or render an error message on the login page
		session["user"] = user
		session['game_state_data'] = 'starting new session'
		session['conversation_history'] = []  # Initialize conversation_history in the session

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
	# Retrieve the current conversation history from the session
    conversation_history = session.get('conversation_history', [])

    bot_response, new_conversation_history = tac_conductor.interact_with_bot(
        user_input, conversation_history, instructions, client, assistant_id, functions
    	)

    # Update the conversation history in the session
    session['conversation_history'] = new_conversation_history
    return bot_response

@app.route("/moreinfo", methods=["POST"])
def moreinfo():
	if request.method == "POST":
		if "user" in session:
			return redirect(url_for("game"))
		return render_template("login.html")
	else:
		return render_template("moreinfo.html")

@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("user", None)
    session.pop("conversation_history", None)  # Clear conversation history
    return redirect(url_for("login"))

def save_score_to_file(data_to_save, path_to_log):
    with open(path_to_log, 'w') as file:   #  session['play_log_file_path'] = play_log_file_path
        file.write(data_to_save)
        file.write("\n")
    file.close()    
    return


if __name__ == "__main__":
    now = datetime.now().strftime("%Y_%m_%d_%H_%M")
    app_directory = pathlib.Path().absolute()
    app_directory /= "game_play_logs"
    app_directory.mkdir(parents=True, exist_ok=True)
    log_filename = f"{now}_log.txt"
    log_file_path = app_directory / log_filename
    log_file_path_str = str(log_file_path)
    save_score_to_file('START SESSION', log_file_path_str)
    instructions, client, conversation_history, assistant_id, functions = tac_conductor.initialize_bot_interaction()
    logging.basicConfig(
        filename=log_file_path,
        level=logging.INFO,
        format='%(asctime)s.%(msecs)d %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    app.run(host='127.0.0.1', debug=True, port=8080)  #, debug=True, threaded=True 
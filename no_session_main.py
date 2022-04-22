# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_flex_quickstart]
import logging
from flask import Flask, render_template, request, session
import jackalbot as jb
from datetime import datetime, timedelta
from pathlib import Path
import pathlib
import os.path
#

app = Flask(__name__)
app.secret_key = "myTestKey"
app.permanent_session_lifetime = timedelta(minutes=90)




@app.route("/")
def home():
    session['persona_session'] = 1
    return render_template("index.html")


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

@app.route("/get")
def get_bot_response():
    user_input = request.args.get('msg')
    bot_response = jb.jackalbot_response(user_input)
    return bot_response

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
    app.run(host='127.0.0.1', port=8080, threaded=True)  

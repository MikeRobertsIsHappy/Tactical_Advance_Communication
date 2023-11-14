
import os
import openai
os.environ['OPENAI_API_KEY'] = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")

def jackalbot_response (user_input, session_data):

    completion = openai.ChatCompletion.create(
    model="gpt-4",
    max_tokens = 250,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input},
        {"role": "assistant", "content": "you always speak in rhyme"}
    ]
    )
    bot_response = completion.choices[0].message['content']
  
    session_data['game_state_data'] = session_data['game_state_data'] + ".   " + user_input + ".  " + bot_response

    return bot_response, session_data['game_state_data']
from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))

client = OpenAI(
   api_key=os.getenv('OPENAI_API_KEY'),
)

# Assuming you have your conversation history defined somewhere, you can import it here
# If it's in your main app file, you may need to find a way to pass it to the function or redesign the code structure
# from app import conversation_history

def chat_with_gpt(question, conversation_history, personality):
    """
    Function to interact with ChatGPT.

    Args:
    - question (str): The question to ask ChatGPT.
    - conversation_history (list): List containing conversation history.

    Returns:
    - str: Answer from ChatGPT.
    """

    # Ensure conversation history doesn't exceed the token limit (e.g., 4096 tokens)
    while sum(len(message['content'].split()) for message in conversation_history) > 24096:
        conversation_history.pop(0)  # Remove the oldest message

    # Create a message with the user's question
    user_message = {"role": "user", "content": question}

    # Add the user's message to the conversation history   ## TODO THIS SHOULD BE BEFORE LINE 27, Check th elength after the new question is added
    conversation_history.append(user_message)

    # Use OpenAI to get an answer
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        seed=1000000, #set a seed for consisten results
        messages=[
             {"role": "system", "content": personality},
              *conversation_history,
            ],
        temperature=0.1,  # Set the temperature for variability
        max_tokens=2000,  # Maximum length of the response
        top_p=0.9  # Nucleus sampling for diversity    
    )

    # Extract the answer from the response
    answer = response.choices[0].message.content

    return answer
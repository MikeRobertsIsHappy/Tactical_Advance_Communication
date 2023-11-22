import json
from openai import OpenAI
import time
from tac_chatgpt import chat_with_gpt
import os
from dotenv import load_dotenv
import logging

def initialize_bot_interaction():
    #get keys from .env file
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    load_dotenv(os.path.join(BASEDIR, '.env'))

    client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    )

    #os.environ['OPENAI_ASSISTANT_ID'] = "asst_E9cCSvS1FFxAD1jbr6m6JGbw"
    assistant_id = os.getenv('OPENAI_ASSISTANT_ID')

    # Prepare a dictionary to map function names from the assistant to your Python functions
    functions = {
        'get_weather': 'sunny'
    }

    return client, assistant_id

# Function to interact with the chatbot
def interact_with_bot(user_input, conversation_history, instructions, client, assistant_id):
    thread = client.beta.threads.create()

    while True:
        if user_input.lower() == "exit":
            print("Exiting the chat.")
            break
        try:
            # Add user message to the thread
            message = client.beta.threads.messages.create(
                thread_id=thread.id,
                role="user",
                content=user_input
            )

            # Run assistant
            run = client.beta.threads.runs.create(
                thread_id=thread.id,
                assistant_id=assistant_id,
                instructions=instructions
            )

            # Display assistant response
            run = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )

           # # Wait until it is not queued
           # count = 0
           # while(run.status == "queued" or run.status == "in_progress" and count < 5):
           #     time.sleep(2)
           #     run = client.beta.threads.runs.retrieve(
           #         thread_id=thread.id,
           #         run_id=run.id
           #
           #  )
           #     count = count + 1

            #if run.status == "requires_action":
            #    # Get the tool outputs by executing the required functions
            #    tool_outputs = execute_required_functions(run.required_action, functions)
            #    # Submit the tool outputs back to the Assistant
            #    run = client.beta.threads.runs.submit_tool_outputs(
            #        thread_id=thread.id,
            #        run_id=run.id,
            #        tool_outputs=tool_outputs
            #    )

            # Wait until it is not queued
            #count = 0
            #while(run.status == "queued" or run.status == "in_progress" or run.status == "requires_action" and count < 5):
            #    time.sleep(2)
            #    run = client.beta.threads.runs.retrieve(
            #        thread_id=thread.id,
            #        run_id=run.id
            #    )
            #    count = count + 1

            # Retrieve messages from thread after run complete
            messages = client.beta.threads.messages.list(
                thread_id=thread.id
            )

            #TODO look for method call in data in messages and execute method
            #print(f"---------------------------------------------")
            #print(f"THREAD MESSAGES: {messages}")
            logging.info(f"THREAD MESSAGES: {messages}")

            # Add the user's message to the conversation history
            #for message in messages:  # Loop through the paginated messages
            #    system_message = {"role": "system", "content": message.content[0].text.value}
            #    conversation_history.append(system_message)  # Append the content attribute of each message to the conversation history
            
            # Get the response from ChatGPT
            answer = chat_with_gpt(user_input, conversation_history, instructions)
            
            # Add the model's response to the chat windows conversation history
            conversation_history.append({"role": "assistant", "content": answer})
            #session_data['conversation_history'] = conversation_history

            return answer, conversation_history
            
        except Exception as e:
            print(f"An error occurred: {e}")

# Function to call the assistant required functions and return their outputs as JSON strings
def execute_required_functions(required_actions, functions):
    tool_outputs = []
    for tool_call in required_actions.submit_tool_outputs.tool_calls:
        func_name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)
        
        # Call the corresponding Python function
        if func_name in functions:
            function = functions[func_name]
            # Assuming all functions take a single dictionary argument
            result = function(**args)  # Calls your function like get_weather(q="Philadelphia PA")

            # Serialize the function's output to JSON
            result_str = json.dumps(result)

            # Add the result to the list of tool outputs
            tool_outputs.append({
                "tool_call_id": tool_call.id,
                "output": result_str,
            })
    return tool_outputs

# Run the interaction
#if __name__ == "__main__":
#    interact_with_bot()

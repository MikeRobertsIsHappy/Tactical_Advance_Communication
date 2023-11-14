
# TAC-GPT-ASSISTANT
TAC Project using OpenAI's  assistant functionality.

===============================================
# Next Steps
- Get it so it connects to Jackalbot
- Update the instructions
- pull out functions ??? maybe ???

===================================================


# Keys
You need to setup an .env file with your OpenAPI key, your RapidApi key, and I also put my assistant id in there as well. You can get your assistant id from the url when you create it.

# Steps to run
```
   cd <to directroy>
   virtualenv env  # for first time
   env\Scripts\activate.ps1
   pip install --upgrade pip
   pip install -r requirements.txt # OR  pip install --no-cache-dir -r requirements.txt   #for first time
   python main.py
```

# Set up new repo
…or push an existing repository from the command line 
```
git init
git remote add origin https://github.com/MikeRobertsIsHappy/tac-gpt-assistant.git
git branch -M main
git push -u origin main
```

## Adding Functions in the Future...
This code sample had some sample functions for weather built in.   I left it in the code if I wanted to use it later.
With functions now you can have it answer things it never could before like so 
(https://github.com/quinny1187/JARVIS/assets/108108975/f9e09ddb-1653-4657-9b9b-b5cbe2a251ec)

#### Function 1
I had to click the stock example for the function to be editable. Then I made mine look like this.
(https://github.com/quinny1187/JARVIS/assets/108108975/f0f1c013-b3d0-48a3-935e-3802adb61271)

For this function I am using a free api you can get access to from rapidapi that gives basic weather data.
(https://github.com/quinny1187/JARVIS/assets/108108975/0cb93317-7661-4f4c-9c2c-571b5aea92f2)

This first method requires you to specify the location where you want the weather from.
Example - Hey Jarvis, can you give me the weather for Los Angeles California today?

### Function 2
I could not get the assistant to work without have at least one parameter for the method so I just pass in the variable q which I do nothing with.
(https://github.com/quinny1187/JARVIS/assets/108108975/e6bda380-2a10-4964-873d-8d8b7912675f)

I then use the same api as above but before I do that I call the get my ip method to gets your public ip and passes it as a parameter in the get_weather() method, which in then returns the weather for that area.
Example - Hey Jarvis, can you me the local weather for today?






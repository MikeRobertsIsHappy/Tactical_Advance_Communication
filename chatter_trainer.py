from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.comparisons import levenshtein_distance #https://chatterbot.readthedocs.io/en/stable/comparisons.html


#from persona_hungry_frustrated import *   # this has the values

chatbot = ChatBot("Jacques", 
                read_only=True, 
                preprocessors=['chatterbot.preprocessors.clean_whitespace'], 
                statement_comparison_function=levenshtein_distance)
trainer = ListTrainer(chatbot)


# --------Catagorize the feelings--------------------------------
#the feeling
FeelingAccuracy0 = ['frustrated']

#for each half of the feeling
FeelingAccuracy1 = ['frustrated and annoyed', ]

#close, but not really
FeelingAccuracy2 = ['frustrated, annoyed and aggravated', 'uncomfortable', 'flustered', 'stimulate', 'displeased', 'exasperated', 'impatient', 'irritated', 'irked', 'perturbed', 'turbulent', 'embarassed', 'depleted', 'unhappy', 'cranky', 'baffled', 'bewildered', 'perplexed', 'distracted', 'agitated', 'turmoil', 'uneasy', 'upset', 'fatigue', 'beat', 'burnt out', 'exhausted', 'lethargic', 'listless', 'yearning', 'confused' ]

# not the feeling
FeelingAccuracy3 = ['energetic', 'worried', 'dismayed', 'troubled', 'distressed', 'absorbed', 'interested', 'hopeful', 'expectant', 'aroused', 'still', 'mistrustful', 'panicked', 'scared', 'angry', 'dazed', 'hesitant', 'lost', 'mystified', 'alarmed', 'discombobulated', 'disconcerted', 'disturbed', 'rattled', 'restless', 'shocked', 'startled', 'surprised', 'unnerved', 'unsettled', 'agony', 'anguished', 'bereaved', 'devastated', 'grief', 'heartbroken', 'depressed', 'discouraged', 'disheartened', 'wretched', 'tense', 'anxious', 'distraught', 'edgy', 'fidgety', 'frazzled', 'irritable', 'jittery', 'nervous', 'overwhelmed', 'restless', 'stressed out', 'Vulnerable', 'fragile', 'guarded', 'helpless', 'insecure', 'leery', 'reserved', 'sensitive', 'shaky']

#really not the feeling
FeelingAccuracy4 =  ['alert', 'curious', 'engrossed', 'intrigued', 'afraid', 'apprehensive', 'dread', 'foreboding', 'frightened', 'petrified', 'suspicious', 'terrified', 'wary', 'disgruntled', 'enraged', 'furious', 'incensed', 'indignant', 'irate', 'livid', 'outraged', 'resentful', 'aversion', 'animosity', 'appalled', 'contempt', 'disgusted', 'dislike', 'hate', 'horrified', 'hostile', 'repulsed', 'ambivalent', 'puzzled', 'torn', 'disconnected', 'alienated', 'aloof', 'apathetic', 'bored', 'cold', 'detached', 'distant', 'indifferent', 'numb', 'removed', 'uninterested', 'withdrawn', 'disquiet', 'ashamed', 'chagrined', 'guilty', 'mortified', 'self-conscious', 'sleepy', 'tired', 'weary', 'worn out', 'hurt', 'lonely', 'miserable', 'regretful', 'remorseful', 'sad', 'despair', 'forlorn' ] 

#these feelings are almost opposite 
FeelingAccuracy5 = ['affectionate', 'compassionate', 'friendly', 'loving', 'open hearted', 'sympathetic', 'tender', 'warm', 'engaged', 'enchanted', 'entranced', 'fascinated', 'spellbound', 'encouraged', 'optimistic', 'confident', 'empowered', 'open', 'proud', 'safe', 'secure', 'excited', 'amazed', 'animated', 'ardent', 'astonished', 'dazzled', 'eager', 'enthusiastic', 'giddy', 'invigorated', 'lively', 'passionate', 'surprised', 'vibrant', 'grateful', 'appreciative', 'moved', 'thankful', 'touched', 'inspired', 'amazed', 'awed', 'wonder', 'joy', 'amused', 'delighted', 'glad', 'happy', 'jubilant', 'pleased', 'tickled', 'exhilerated', 'blissful', 'ecstatic', 'elated', 'enthralled', 'exuberant', 'radiant', 'rapturous', 'thrilled', 'peaceful', 'calm', 'clear headed', 'comfortable', 'centered', 'content', 'equanimous', 'fulfilled', 'mellow', 'quiet', 'relaxed', 'relieved', 'satisfied', 'serene', 'tranquil', 'trusting', 'refreshed', 'enlivened', 'rejuvenated', 'renewed', 'rested', 'restored', 'revived', 'pain', 'dejected', 'despondent', 'disappointed', 'heavy hearted', 'hopeless', 'melancholy', 'envious', 'jealous', 'longing', 'nostalgic', 'pining', 'wistful', 'gloomy' ]

user_messing_around = ["silly", "dumb", "stupid", "I'dont think so", "I don't care", "do you know anything", "not good", "omg", "this is not working", "this is bad", "not what I want", "live help", "get me a rep", "I need a real person", "forget you"]


# -------- Create a response for each catagory

for emotion in FeelingAccuracy0:
    trainer.train([
        f"{emotion}",
        f"That's it!  Yeah,  I feel that feelings.   I'm feeling {emotion} that I can't find a place to eat.  You are super helpful."
    ])

for emotion in FeelingAccuracy1:
    trainer.train([
        f"{emotion}",
        f"That feels like it is partially correct.    I definitely feel {emotion},  but it feels like I have 2nd emotion also.  I wonder what it is?"
    ])

for emotion in FeelingAccuracy2:
    trainer.train([
        f"{emotion}",
        f"hmmmm,  {emotion} kind of close, but it is not quite the right feeling.  I feel a little different than that. Maybe guess again?"
    ])

for emotion in FeelingAccuracy3:
    trainer.train([
        f"{emotion}",
        f"Well, that is an emotion, but {emotion} is not really what I'm feeling.  Thanks for asking, but I wish I could find a restaurant."
    ])

for emotion in FeelingAccuracy4:
    trainer.train([
        f"{emotion}",
        f"That is not right.  I don't feel like {emotion}. "
    ])        

for emotion in FeelingAccuracy5:
    trainer.train([
        f"{emotion}",
        f"No way!  {emotion} is like the opposite of what I'm feeling.   You're wasting my time.  I gotta find a restaurant. "
    ])    

for user_response in user_messing_around:
    trainer.train([
        f"{user_response}",
        f"hmmmmm, \'{user_response}\' It seems like don't want to talk anymore. You are the worst person at NVC that I have ever seen."
    ])    



trainer.export_for_training('twilybot.json')
from textblob.classifiers import NaiveBayesClassifier


def trainer():
    train = [
        ["i am good", "neg"],
        ["are you feeling", "pos"],
        ["does it feel like", "pos"],
        ["do you feel", "pos"],
        ["i wonder if you are feeling", "pos"],
        ["sounds like you're feeling", "pos"],
        ["i'm guessing that", "pos"],
        ["do you feel", "pos"],
        ["do you feel", "pos"],
        ["I feel", "neg"],
        ["i feel", "neg"],
        ["you feel", "pos"],
        ["you experiencing", "pos"],
        ["you're feeling", "pos"],
        ["you're experiencing", "pos"],
        ["to feel", "pos"],
        ["I'm experiencing", "neg"],
        ["doing ok", "pos"],
        ["i am crappy", "neg"],
        ["omg", "neg"],
        ["wtf", "neg"],
        ["you suck", "neg"],
        ["this is not working", "neg"]
            ]

    return NaiveBayesClassifier(train)


if __name__ == "__main__":
    user_input = "you're experiencing"
    #user_input = TextBlob(user_input)
    classy = trainer().prob_classify(user_input)
    print()
    print(f'String:  {user_input}')
    print(f'---------{len(user_input) * "-"}+')
    print(f'Negative probability: {classy.prob("neg")}')
    print(f'Positive probability: {classy.prob("pos")}')

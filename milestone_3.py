import random as r
import string as s
from topics import topics

def random_choice(topic_dict):
    word = r.choice(topic_dict)
    return word

def setup():
    topic_options = [x for x in topics.keys()]
    topic = random_choice(topic_options)
    cap_topic = s.capwords(topic)
    word = random_choice(topics[topic]).lower()
    return word

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} not in the word.")

def ask_for_input():
    while True:
        guess = str(input("Choose a letter..."))
        if len(guess) == 1 and guess.lower().isalpha():
            break
        else:
            print("Please enter a valid selection. (One letter)")
    check_guess(guess)

word = setup()
print(word)

ask_for_input()


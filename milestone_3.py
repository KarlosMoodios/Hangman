import random as r
import string as s
from topics import topics

def random_choice(topic_dict):
    word_to_guess = r.choice(topic_dict)
    return word_to_guess

def setup():
    topic_options = [x for x in topics.keys()]
    topic = random_choice(topic_options)
    cap_topic = s.capwords(topic)
    word_to_guess = random_choice(topics[topic]).lower()
    return word_to_guess

def check_guess(guess):
    guess = guess.lower()
    if guess in word_to_guess:
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

word_to_guess = setup()
print(word_to_guess)

ask_for_input()


import random as r
import string as s
from topics import topics

def random_choice(topic_dict):
    word = r.choice(topic_dict)
    return word

def check_guess(name, word, guess):
    letters = [x for x in s.ascii_lowercase]
    already_tried = []
    turns = 7 # Post, Head, Body, 2 Arms, 2 Legs

    # If guess is not a single character
    if len(guess) != 1 or guess.lower() not in letters: 
        print("Please enter a single character.")
        guess = str('')
        return guess
    else:
        # If guess is in the word
        if guess in word and guess not in already_tried:
            print(f"Good guess! {guess} is in the word.")
            if len(already_tried) == 0:
                already_tried.append(guess)
                print("Letters you've already tried:\n", *already_tried)
            else:
                already_tried.extend(guess)
                print("Letters you've already tried:\n", *already_tried)
        elif guess in already_tried:
            print("You have already tried this letter. please try again")

        # If guess is not in the word
        elif guess not in word:
            print(f"Sorry, {guess} is not in the word. Try again.")
            
            if len(already_tried) == 0:
                already_tried.append(guess)
                print("Letters you've already tried:\n", *already_tried)
            elif guess in already_tried:
                print("You have already tried this letter. Please try again")
            else:
                already_tried.extend(guess)
                print("Letters you've already tried:\n", *already_tried)
            
            if turns > 0:
                print(f"Bad luck! you have {turns} turns remaining.")
                turns -= 1
            
            if turns == 0:
                print(f"Oh no {name}! You have lost the game!")
                print(f"The word was: {word}")

def ask_for_name():
    string = input("What is your name?\n") or "Player 1"
    name = s.capwords(string, sep = None)
    return name

def ask_for_input():
    guess = str(input("\nEnter a letter: "))
    return guess

def setup():
    topic_options = [x for x in topics.keys()]
    topic = random_choice(topic_options)
    cap_topic = s.capwords(topic)
    word = random_choice(topics[topic]).lower()

    print("\nWelcome to a game of hangman!")
    name = ask_for_name()
    print (f"\nGreetings {name}! Time to play hangman!")
    print (f"\nStart guessing to find the word from the topic: {cap_topic}")
    print (f"There are {len(word)} letters in the word.")
    return word, name

def game_loop(name, word):
    guessed_word = ''
    while True:
        failed = 0
        
        for guess in word:
            if guess in guessed_word:
                print(guess, end="") 
            else:
                print("_", end="")
                failed +=1
        if failed == 0:
            print(f"\nWell done {name}! You won!")
            break

        guess = ask_for_input()
        guess = check_guess(name, word, guess)
        guessed_word += guess

def main():
    word, name = setup()
    game_loop(name, word)
    
main()


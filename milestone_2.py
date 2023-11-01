import random as r
import string as s
from topics import topics

def random_choice(topic_dict):
    word = r.choice(topic_dict)
    return word

def main():
    letters = [x for x in s.ascii_lowercase]
    topic_options = [x for x in topics.keys()]
    topic = random_choice(topic_options)
    cap_topic = s.capwords(topic)
    word = random_choice(topics[topic]).lower()
    guessed_word = ''
    turns = 7 # Post, Head, Body, 2 Arms, 2 Legs 

    print("Welcome to a game of hangman!")
    name = input("\nWhat is your name? \n")
    print (f"\nGreetings {name.capitalize()}! Time to play hangman!")
    print (f"Start guessing to find the word from the topic: {cap_topic}")
    print (f"There are {len(word)} letters in the word.")
     
    while turns > 0:
        failed = 0

        for guess in word:
            if guess in guessed_word:
                print(guess, end="" )
            else:
                print("_", end="")
                failed +=1
        
        if failed == 0:
            print(f"\nWell done {name.capitalize()}! You won!")
            break

        guess = str(input("\nChoose a letter: ")).lower()
        
        if len(guess) != 1 or guess.lower() not in letters: 
            print("Please enter a single character.")
            guess = ''
        
        elif guess not in word:
            turns -= 1
            print(f"\nBad luck! you have {turns} turns remaining.")
            if turns == 0:
                print(f"Oh no {name.capitalize()}! You have lost the game!")
                print(f"The word was: {word}")
        
        guessed_word += guess


main()
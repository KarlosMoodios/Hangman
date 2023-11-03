import random as r
import string as s
from topics import topics
import sys

class Hangman:
    def __init__(self, word, num_lives = 7):
        self.word_to_guess = word.lower()
        self.word_guessed = ["_" for element in self.word_to_guess]
        self.num_letters = len(set(self.word_to_guess))
        self.num_lives = num_lives
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word_to_guess.lower():
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word_to_guess.lower()):
                if letter == guess:
                    if index == 0:
                        self.word_guessed[index] = guess.upper()
                    else:
                        self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            print(f"Sorry, {guess} not in the word.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} guesses remaining.")
            if self.num_lives == 0:
                return
        print(*self.word_guessed)
        
    def ask_for_input(self):
        while True:
            guess = str(input("Choose a letter:  ")).lower()
            if guess in self.list_of_guesses:
                print("You have already tried that letter!")
                return
            elif len(guess) == 1 and guess.isalpha():
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                return
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")
                return

def random_choice(topics):
        topic_options = [x for x in topics.keys()]
        topic = r.choice(topic_options)
        print(f"\nThe word is from the topic: {topic}.")
        word = r.choice(topics[topic]).lower()
        return word

def play_game(topics):
    print("\nWelcome to a game of hangman!")
    name = input("Enter your name:\n")
    name = s.capwords(name)
    print(f"\nGreetings {name}, Begin guessing to find the hidden word.")
    game = Hangman(random_choice(topics))
    print(*game.word_guessed)
    while True:
        if game.num_lives == 0:
            print(f"\nSorry {name}, You lost!\n")
            sys.exit()
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives > 0 and game.num_letters == 0:
            print(f"\nWell done {name}, You have won the game!\n")
            sys.exit()

play_game(topics)
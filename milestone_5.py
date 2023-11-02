import random as r
import string as s
from topics import topics

class Hangman:
    def __init__(self, word_list, num_lives = 7):
        self.word_to_guess = random_choice(topics)
        self.word_guessed = ["_" for element in self.word_to_guess]
        self.num_letters = len(set(self.word_to_guess))
        self.num_lives = num_lives
        self.word_list = []
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word_to_guess.lower():
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} not in the word.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} remaining.")

        for index, letter in enumerate(self.word_to_guess.lower()):
            if letter == guess:
                self.word_guessed[index] = guess
        print(*self.word_guessed)
        self.num_letters -= 1
    
    def ask_for_input(self):
        while True:
            guess = str(input("Choose a letter..."))
            if len(guess) != 1 and guess.lower().isalpha() and guess != '\n':
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You have already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
   
def random_choice(topics):
        topic_options = [x for x in topics.keys()]
        topic = r.choice(topic_options)
        word = r.choice(topics[topic]).lower()
        return word

def play_game(topics):
    game = Hangman(random_choice(topics))
    print(*game.word_guessed)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives != 0 and game.num_letters == 0:
            print("Well done! You have won the game!")

# 
# game.ask_for_input()
play_game(topics)
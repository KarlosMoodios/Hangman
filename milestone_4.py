import random as r
import string as s
from topics import topics

word_list = ['Apple', 'Banana', 'Clementine', 'Date', 'Eggplant']

class Hangman:
    def __init__(self, word_list, num_lives = 7):
        self.word_to_guess = random_choice(word_list)
        self.word_guessed = ["_" for i in self.word_to_guess]
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
            print(f"I:{index}, L:{letter}")
            if letter == guess:
                self.word_guessed[index] = guess
                print(*self.word_guessed)
        self.num_letters -= 1
    
    def ask_for_input(self):
        while True:
            guess = str(input("Choose a letter..."))
            if len(guess) != 1 and guess.lower().isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You have already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
   
def random_choice(topic_dict):
        topic_options = [x for x in topics.keys()]
        topic = random_choice(topic_options)
        cap_topic = s.capwords(topic)
        word = random_choice(topics[topic]).lower()
        word = r.choice(topic_dict)
        return word

game = Hangman(word_list)
print(game.word_to_guess)
print(*game.word_guessed)
game.ask_for_input()


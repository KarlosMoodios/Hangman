import random as r
import string as s
from topics import topics
import sys


class Hangman:
    '''
    This class is used to represent a game of Hangman.

    Attributes:
        Private:
            word_to_guess = The word to be guessed.
        Public:
            word_guessed = A list of '_' equal to the length of the word_to_guess.
            num_letters = A counter to check the number of unique letters 
                        left in the word that is guessed so far.
            num_lives = The number of lives or guesses, the player has remaining.
            list_of_guesses = An empty list, where each guess will be appended.
    '''
    
    # Initialise this instance of the class
    def __init__(self, word, num_lives = 7):
        '''
        See help(Hangman) for accurate signature.
        '''
        self._word_to_guess = word.lower()
        self.word_guessed = ["_" for element in self._word_to_guess]
        self.num_letters = len(set(self._word_to_guess))
        self.num_lives = num_lives
        self.list_of_guesses = []
    
    # Checks the guess entered against the correct word
    def check_guess(self, guess):
        '''
        A method within the Hangman class.
        This method is used to check whether the guess entered by the player
        exists within the word that is to be guessed.

        If correct, it will replace the '_' in the word to be guessed, at the 
        correct indices, to that letter(s).
        If incorrect, the number of lives is reduced by 1.
        If number of lives is equal to 0, the function returns to the point it was called.
        After each run of this function, the word to be guessed is printed to the console.
        '''
        # Make guess lowercase
        guess = guess.lower()

        # If guess is in word
        if guess in self._word_to_guess:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self._word_to_guess):
                if letter == guess:
                    if index == 0: # If the first letter
                        # Append the uppercase letter
                        self.word_guessed[index] = guess.upper()
                    else:
                        self.word_guessed[index] = guess
            self.num_letters -= 1
        
        # If guess not in word
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} guesses remaining.")
        print(*self.word_guessed)
        
        # If number of lives is equal to 0
        if self.num_lives == 0:
                return
        
    def ask_for_input(self):
        '''
        A method within the Hangman class.
        This method asks the user to input a single, alphabetical character.

        Firstly, it checks if the guess entered is already in the list of guesses.
        Passing this check, a message in the console will read:
        You have already tried that letter!

        Secondly, it checks if the guess entered is one character in length AND 
        is a letter, not a number. 
        Passing this check, the check_guess function of the Hangman class will 
        be called, then the guess will be appended to the list of guesses.

        Finally, if the prior checks fail, a message in the console will read:
        Invalid letter. Please, enter a single alphabetical character.
        '''
        while True:
            guess = str(input("\nChoose a letter:  ")).lower()
            
            # If guess is in list of already guessed letters
            if guess in self.list_of_guesses:
                print("You have already tried that letter!\n")
                return
            
            # Check if guess is one character long AND is alphabetical
            elif len(guess) == 1 and guess.isalpha():
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                return
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")
                return

def random_choice(topics):
        '''
        This function chooses a random word from a random topic, provided when 
        importing the topics module.
        It uses a list comprehesion to make a list of topics, then uses random.choice()
        to choose a random topic from the list. 
        Once selected, it uses random.choice() on the topics dict with topic as the key. 
        This will select a random value from the list of values at that key.
        The function returns the word chosen.
        '''
        # Create list of topics
        topic_options = [x for x in topics.keys()]
        # Choose a random topic
        topic = r.choice(topic_options)
        print(f"\nThe word is from the topic: {topic}.")
        # Choose a random word from the list in the topics dictionary
        word = r.choice(topics[topic]).lower()
        return word

def play_game(topics):
    '''
    This function ties the hangman class and the random_choice function together.

    A message in the console welcomes the player to a game of Hangman and
    asks the player to enter their name. 
    The name is then converted to capital letters at the beginning of each word entered.
    A message in the console greets the player by name and prompts them to begin 
    guessing to find the hidden word.
    The game is initiated and the word to be guessed is displayed in the console.
    A while loop contains three IF statements as follows:
    if the number of lives is equal to 0: 
        A console message will read: "Sorry, (player name) you lost!"
        system will exit.
    if the number on letters is greater than 0:
        game asks for input
    if the number of lives is greater than 0 AND the number of letters is equal to 0:
        A console message will read: "Well done (player name) You have won the game!"
        system will exit

    '''
    print("\nWelcome to a game of hangman!")
    name = input("Enter your name:\n")
    # Capitalise first letter of each word in name
    name = s.capwords(name)
    print(f"\nGreetings {name}, Begin guessing to find the hidden word.")
    # Create a game of Hangman passing the returned value of random_choice(topics) to the class
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

if __name__ == "__main__":
    play_game(topics)
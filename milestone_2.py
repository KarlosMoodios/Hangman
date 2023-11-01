import random as r
import string as s

def random_choice(fruit_list):
    word = r.choice(fruit_list)
    return word

fruit_list = [
    'Apple', 
    'Banana', 
    'Clementine', 
    'Date', 
    'Eggplant',
    'Oranges', 
    'Mango', 
    'Grapes', 
    'Strawberry', 
    'Melon']

letters = [x for x in s.ascii_lowercase]

word = random_choice(fruit_list).lower()
guessed_word = ''
turns = round(len(word) * 1.5)

name = input("\nWelcome to a game of hangman! What is your name? ")
print (f"Hello {name.capitalize()}! Time to play hangman!")
print ("Start guessing...")

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

    guess = str(input("\nChoose a letter:\t")).lower()
    
    if len(guess) != 1 or guess.lower() not in letters: 
        print("Please enter a single character.")
        guess = ''
    
    elif guess not in word:
        turns -= 1
        print(f"\nBad luck! you have {turns} turns remaining.")
        if turns == 0:
            print(f"Oh no {name.capitalize()}! You have lost the game!")
    
    guessed_word += guess
    
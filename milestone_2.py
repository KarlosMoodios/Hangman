import random as r
import string as s

def random_choice(word_list):
    word = r.choice(word_list)
    return word

word_list = ['Apple', 'Banana', 'Clementine', 'Date', 'Eggplant']
letters = [x for x in s.ascii_lowercase]

print(letters)
print(word_list)

word = random_choice(word_list)
print(word)

guess = str(input("Choose a letter..."))

if len(guess) == 1 and guess.lower() in letters:
    if guess.lower() in word.lower():
        print("Good guess!")
    else:
        print("Not present, try again.")
else:
    print("Please enter a valid selection. (One letter)")
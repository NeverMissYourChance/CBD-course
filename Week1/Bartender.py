"""
Assignment 1: Bartender project
---------------------------------------------------------------------------------
Ask users to enter their taste from the questions list until receive answer "yes"
Then match randomly with the ingredients
Author: Khoi Doan Minh
"""
# Import libraries
import random
# Two given dictionaries
questions = {
    "strong": "Do you like your drinks strong?",
    "salty": "Do you like it with a salty tang?",
    "bitter": "Are you a lubber who likes it bitter?",
    "sweet": "Would you like a bit of sweetness with your opinion?",
    "fruity": "Are you one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tobic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}
# Bartender function
def bartender(questions, ingredients):
    print("What would you like to drink?")
    have_drinked = False
    for taste, question in questions.items():
        print(question)
        answer = input("Enter your answer (y/n)? ")
        # Repeat ask until receive valid answer
        while (answer != 'y') and (answer != 'n'):
            print("Invalid answer. Please re-enter your answer!")
            print(question)
            answer = input("Enter your answer (y/n)? ")
        # Choose randomly the ingredient
        if (answer == 'y'):
            ingredient = random.choice(ingredients[taste])
            print("We choose {} for you.".format(ingredient))
            print("We hope you will enjoy it!")
            have_drinked = True
            break
    # If all answer is "no"
    if (not have_drinked):
        print("If you change your mind, please call us!")
# Main function
if __name__ == '__main__':
    bartender(questions, ingredients)
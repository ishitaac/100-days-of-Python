import random

EASY_LEVEL = 10
HARD_LEVEL = 5

def check(number,answer,turns):
    if number > answer:
        print("To High!")
        return turns-1
    elif number < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


def category_chosen(category):
    if category == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = random.randint(1, 100)
category = input("Choose a difficulty. Type 'easy' or 'hard': ")
turns = category_chosen(category)

guess = False

while guess == False:
# while num!=answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    num = int(input("Make a guess: "))

    turns = check(num,answer,turns)
    if turns == 0:
        print("You've run out of guesses, you lose.")
        guess= True
    elif guess == False :
        print("Guess again!")
import random
from data import dataset
from art6 import logo, vs

def choose_random():
    """ Choosing a random choice from data"""
    return random.choice(dataset)

def formatting(chosen):
    """Format chosen celebrity description into printable format: name, description and country"""
    name = chosen["name"]
    follwer_count = chosen["follower_count"]
    description = chosen["description"]
    country = chosen["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_follower,b_follower):
    """Checks followers against user's guess and returns True if they got it right. Or False if they got it wrong."""
    if a_follower> b_follower:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print(logo)
    print()
    a = choose_random()
    b = choose_random()
    score = 0
    contd = True

    while contd:
        a= b
        b = choose_random()

        while a==b:
            b=choose_random

        print(f"Compare A: {formatting(a)}.")
        print(vs)
        print(f"Against B: {formatting(b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_count = a["follower_count"]
        b_count = b["follower_count"]
        is_correct = check_answer(guess, a_count ,b_count)
            
        if is_correct:
            score +=1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            contd = False
            if input("Type 'Yes' if you want to go again. Otherwise type 'no'. \n").lower() == 'yes':
                game()
            else:
                print("Game over!")


game()
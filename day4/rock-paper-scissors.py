rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
ans = [rock,paper,scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(ans[user])


# computer = random.choice(ans)
computer = random.randint(0,2)
print(computer)
print(ans[computer])

if user>=3 or user<0:
  print("You typed an invalid number. You lose!")
elif user==computer:
  print("It's a tie")
elif user == 0 and computer == 2:
  print("You win!")
# elif user == 2 and computer == 1:
#   print("You win!")
elif user == 2 and computer == 0:
  print("Computer win!")
elif user > computer :
  print("You win!")
elif computer > user:
  print("Computer wins!")
import random

nameAsCSV = input("Enter the names of the people who are going to pay the bills, separated by comma : ")
names = nameAsCSV.split(",")
print(names)
print()
# METHOD I:
# print("{} is going to buy the meal today!".format(random.choice(names)))

# MEHOD II: without choice()
length = len(names)
# print(random.randint(0, length-1))
print("{} is going to buy the meal today!".format(names[random.randint(0, length-1)]))

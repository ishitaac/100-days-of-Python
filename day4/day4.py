# RANDOM MODULES: 

import random

# integer
random_integer = random.randint(1,10)
# for i in range (0,10):
    # print(random_integer)

#  float --> generates random numbers between [0.0 , 1.0) ie 0.00000 -0.99999
random_float = random.random()
# print(random_float)

# to incrase the range of floating points from 0.0000 - 4.9999999
# print(random_float * 5)

# HEADS OR TAILS 
hort = random.randint(0,1)
if hort == 1:
    print("Heads")
else:
    print("tails")

# seed - from where to start genertaing the number seq , cuurent system time which is taken from seconds elasped from 1 jan 1970
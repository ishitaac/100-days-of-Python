import math


def calc(h,w,coverage):
    area=h*w
    print("The number of cans that are required to paint the area {} m-sq is/are {}".format(area,(math.ceil(area/coverage))))

coverage = 5
h =int(input("Height of the wall: "))
w = int(input("Width of the wall: "))

calc(h,w,coverage)



import random

def roll():
    return random.randint(1,6)

def print_histogram(h):
    for i,v in enumerate(h):
        print(i, ":", "*" * v)

histogram = [0] * 7

for i in range(500):
    r = roll()
    histogram[r] += 1

print_histogram(histogram)
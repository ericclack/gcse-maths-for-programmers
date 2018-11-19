# Probability 2: Python model answer by Eric

import random

print("Looking for pairs with two dice.")

experiments = int(input("How many rolls of the dice? "))
successes = 0

def dice_roll(): return random.choice([1,2,3,4,5,6])

for i in range(experiments):
    a = dice_roll()
    b = dice_roll()
    if a == b:
        successes += 1

print("After %s experiments, probability of event is %s" % (experiments, successes/experiments))

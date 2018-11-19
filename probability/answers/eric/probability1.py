# Probability 1: Python model answer by Eric

import random

experiments = int(input("How many rolls of the dice? "))
success = int(input("Which number 1-6? "))
successes = 0

def dice_roll(): return random.choice([1,2,3,4,5,6])

for i in range(experiments):
    if dice_roll() == success:
        successes += 1

print("After %s experiments, probability of event is %s" % (experiments, successes/experiments))

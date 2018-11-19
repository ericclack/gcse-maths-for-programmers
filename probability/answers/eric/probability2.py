# Probability 2: Python model answer by Eric

import random

print("\nLooking for pairs with at least two dice.")
experiments = int(input("How many rolls of the dice? "))
dice = int(input("How many dice? (at least two) "))
assert dice >= 2, "You need at least two dice!"

def dice_roll(): return random.choice([1,2,3,4,5,6])

def is_pair_in_list(alist):
    item_count = { 1:0, 2:0, 3:0, 4:0, 5:0, 6:0 }
    for i in alist:
        item_count[i] += 1
        if item_count[i] >= 2:
            return True
    return False
    
    
successes = 0
for i in range(experiments):
    rolls = [dice_roll() for d in range(dice)]
    if is_pair_in_list(rolls):
        print("Pair in %s" % rolls)
        successes += 1

print("After %s experiments, probability of event is %s" % (experiments, successes/experiments))

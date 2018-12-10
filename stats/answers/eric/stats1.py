# Stats 1: Python model answer by Eric

import random

MIN = 100
MAX = 250
CLASSES = 10
N = 10000

def random_height():
    return random.randint(MIN,MAX-1)

def height_to_class(h):
    """Which class, 0 to CLASSES-1, is this datum in?"""
    frac = (h-MIN) / (MAX-MIN)
    return int(frac * CLASSES)

def class_range(c):
    range = MAX-MIN
    frac = c/CLASSES
    lower = int(MIN + frac*range)
    upper = int(MIN + frac*range + 1/CLASSES*range - 1)
    return ("%s-%s" % (lower, upper))

# - - -  -  -  -  -  -  -  -  -  -  -  -  -  - 

# Start with zeros 
height_classes = [0 for i in range(CLASSES)]

# Collect data
for i in range(N):
    h = random_height()
    c = height_to_class(h)
    height_classes[c] += 1

# Print out:
for i,f in enumerate(height_classes):
    print(class_range(i), ":", f)

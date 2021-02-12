import random

def roll():
    return random.randint(1,6)

def print_frequency_tab(h):
    print("| Value | Freq | Graph")
    print("|-------|------|------")
    for i,v in enumerate(h):
        print("| {:>5} | {:>4} | {}".format(i, v, "*" * v))

frequencies = [0] * 7

for i in range(500):
    r = roll()
    frequencies[r] += 1

print_frequency_tab(frequencies)
# Sets 1: Python model answer by Eric

def make_set(s):
    sp = s.split(",")
    if sp != ['']:
        return sp

def remove_duplicates(aset):
    newset = []
    for a in aset:
        if a not in newset:
            newset.append(a)
    return newset

def union(sets):
    return remove_duplicates(sets[0] + union(sets[1:]))

def intersection(set1, set2):
    newset = []
    for a in set1:
        if a in set2:
            newset.append(a)
    return newset

def complement(aset, universal):
    newset = []
    for a in universal:
        if a not in aset:
            newset.append(a)
    return newset


# - - -  -  -  -  -  -  -  -  -  -  -  -  -  - 

print("Enter sets, as comma separated strings or numbers. Enter nothing when you're done.")
sets = [] # A list of sets (lists)
counter = 1
while True:
    aset = make_set(input("Enter set %s: " % counter))
    if aset:
        sets.append(aset)
        counter += 1
    else:
        break

print()
print("- " * 30)
for (n, s) in enumerate(sets):
    print("Set %s: " % (n+1), s)
universal = union(sets)

op = None
while op != "q":
    print()
    print("What operation to perform on set1 and set2?")
    op = input("C = Complement, I = Intersection, U = Union, Q = Quit  ").lower()
    if op == "c":
        s = int(input("Which set, 1 or 2? "))
        if s == 1:
            print(complement(set1, universal))
        elif s == 2:
            print(complement(set2, universal))
    if op == "i":
        print(intersection(set1, set2))
    elif op == "u":
        print(union(set1, set2))

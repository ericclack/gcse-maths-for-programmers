# Sets 1: Python model answer by Eric

def make_set(s):
    return s.split(",")

def remove_duplicates(aset):
    newset = []
    for a in aset:
        if a not in newset:
            newset.append(a)
    return newset

def union(set1, set2):
    return remove_duplicates(set1 + set2)

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

print("Enter sets, as comma separated strings or numbers")
set1 = make_set(input("Enter set 1: "))
set2 = make_set(input("Enter set 2: "))

print()
print("- " * 30)
print("Set 1: ", set1)
print("Set 2: ", set2)
universal = union(set1, set2)

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

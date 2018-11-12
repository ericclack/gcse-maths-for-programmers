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


# - - -  -  -  -  -  -  -  -  -  -  -  -  -  - 

print("Enter sets, as comma separated strings or numbers")
set1 = make_set(input("Enter set 1: "))
set2 = make_set(input("Enter set 2: "))

print()
print("- " * 30)
print("Set 1: ", set1)
print("Set 2: ", set2)

op = None
while op != "q":
    print()
    print("What operation to perform on set1 and set2?")
    op = input("U = Union, Q = Quit  ").lower()
    if op == "u":
        print(union(set1, set2))

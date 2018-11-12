# Sets

Here are some example sets:

```
pondlife P = { frog, newt, snail, fish, dragonfly }
gardenlife G = { bird, frog, newt, butterfly, dragonfly }
houselife H = { human, dog, cat }
```

We can then use some set operations on these sets...

```
# What lives in the pond *and* the garden? (set intersection)
P ⋂ G = { newt, frog, dragonfly }

# What lives in the pond *or* the garden? (set union)
P ⋃ G = { frog, newt, snail, fish, dragonfly,
          bird, butterfly }

# What doesn't live in the pond? (set complement)
'P = { bird, butterfly, human, dog, cat }

# What lives only in the pond and not in the garden?
...hmmm, that's a bit more tricky...
```

The complement needs the concept of the universal set ξ, which is
for our purposes can be everything we know about in any of the
sets we've defined.

```
ξ = { frog, newt, snail, fish, dragonfly, bird, butterfly,
       human, dog, cat }
```

## Programming Task 1

Write a program that allows the user to input some sets, then display them.

Now enable the user to generate the union of two sets. Make sure you remove any duplicates.

## Programming Task 2

Add set intersection for two sets, then three.

Add complement, first defining the universal set to be everything in all sets
the user has input.

----

## Model answers

* JavaScript
* [Python](answers/eric/python/sets1.py)



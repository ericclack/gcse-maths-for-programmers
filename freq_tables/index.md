# Frequency Tables

We can use frequency tables to see how data is distributed. For
example, if we roll a dice many times, how many 1s, 2s, 3s, 4s, 5s,
and 6s do we get?

## Rolling a dice

Here's a simple function that simulates a dice roll:

```
def roll(): return 3
```

Can you see the problem with it? Try running it and see what happens. 

How can you fix it? Hint: the `random` module and `randint` can help us. 

## Collecting the data

So if we roll our dice lots of times we can collect the results and
draw a frequency table. 

We can store the results in a list, with each item of the list
corresponding to the result of the dice roll. 

We can do this in Python like so: 

```
# Make an empty list
frequencies = [0] * 7

# Roll the dice and collect the results
for i in range(100):
    r = roll()
    frequencies[r] += 1
    
print(frequencies)
```

## Draw a frequency table

Now that we have the data, let's draw a simple text table.

We need do loop through our data, and get the dice number and the 
number of times we saw that result.

Here's how to do it: 

```
def print_frequency_tab(h):
    print("| Value | Freq | Graph")
    print("|-------|------|------")
    for i,v in enumerate(h):
        print("| {:>5} | {:>4} | {}".format(i, v, "*" * v))
```

The parts like `{:>5}` control how the numbers are printed. This
means use a width of 5 characters for the value and right align it.

## Calculating averages

Do you remember the different measures of a set of data? 

* Mode
* Range
* Median
* Mean

How would we determine these from the data table? 

## Types of distributions

### One dice

So, as you increase the number of rolls what happens? And as you reduce the
number of rolls? Why is this? 

### Two dice

Let's now use two dice and add them together, what does this do to the
distribution?

You'll need to change the length of your frequencies array -- to what? 

And you'll need to change the line `r = roll()` to `r = roll() + roll()`.

### Three dice

What happens with 3 dice, or 6 or more? 

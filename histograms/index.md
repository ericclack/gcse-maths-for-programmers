# Histograms

We can use histograms to see how data is distributed. For example, if we 
roll a dice many times, how many 1s, 2s, 3s, 4s, 5s, and 6s do we get? 

## Rolling a dice

Here's a simple function that simulates a dice roll:

```
def roll(): return 3
```

Can you see the problem with it? Try running it and see what happens. 

How can you fix it? Hint: the `random` module and `randint` can help us. 

## Collecting the data

So if we roll our dice lots of times we can collect the results and
draw a histogram. 

We can store the results in a list, with each item of the list
corresponding to the result of the dice roll. 

We can do this in Python like so: 

```
# Make an empty list
histogram = [0] * 7

# Roll the dice and collect the results
for i in range(100):
    r = roll()
    histogram[r] += 1
    
print(histogram)
```

## Draw a histogram

Now that we have the data, let's draw a simple text histogram.

We need do loop through our data, and get the dice number and the 
number of times we saw that result.

Here's how to do it: 

```
def print_histogram(h):
    for i,v in enumerate(h):
        print(i, ":", "*" * v)
```

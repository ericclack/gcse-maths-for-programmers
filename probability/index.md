# Probability

Probability is a measure of how likely it is that something will happen. Mathmatically it's a number between 0 (impossible) to 1 (certain).

For example: there's a 1/6 chance of rolling a six on a regular dice.

In general terms, the probability of an event is defined as:

```
number of successful outcomes
-----------------------------
 number of possible outcomes
```

That's for a single event, what about two *independent* events?

## Two independent events

For example, what's the probability of rolling two sixes? We can make a list of possible outcomes and mark the successful ones, then use the formula above. 

```
1 + 1   2 + 1   3 + 1   4 + 1   5 + 1   6 + 1 
1 + 2   2 + 2   3 + 2   4 + 2   5 + 2   6 + 2 
1 + 3   2 + 3   3 + 3   4 + 3   5 + 3   6 + 3 
1 + 4   2 + 4   3 + 4   4 + 4   5 + 4   6 + 4 
1 + 5   2 + 5   3 + 5   4 + 5   5 + 5   6 + 5 
1 + 6   2 + 6   3 + 6   4 + 6   5 + 6  *6 + 6* 
```

So that's 1 successful outcome in 36 possible outcomes, = 1/36.

Alternatively we can use the formula, as long as the events are independent:

```
P = P1 x P2
```

Where P1 and P2 are the probability of rolling a six, or 1/6.

```
P = 1/6 x 1/6 = 1/36
```


## Experimental vs theoretical probability

We're going to use our programming skills to test out experimental probability by running many thousand experiements. Hopefully the results will approach theoretical probability.

## Programming Task 1

What's the probability of rolling a six with a single die? How does the experimental probability change with 100 experiments, 1000 or 10,000?

## Programming Task 2

What's the probability of rolling a pair with two dice?

What about a pair with three dice?

----

## Model answers

* JavaScript
* [Python](answers/eric/probability1.py)



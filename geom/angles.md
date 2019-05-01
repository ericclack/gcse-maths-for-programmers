# Geometry - Angles

## Task Set Up

Find a turtle library for your chosen programming language, e.g...

### Python

```
import turtle

turtle.forward(100)
turtle.left(45)
turtle.forward(100)
```

### JavaScript

Use the `turtle-canvas` package?

TODO: Examples


## Task 1

Let's explore angles along a path first.

If you move forward 100, then turn 45 degrees, and move forward 100 again, what's the size of the two angles you've created, interior and exterior?

If you repeat the process, how many times until you make a polygon? How many sides does it have?

## Task 2

Try other angles.

Now figure out the formula to convert between the interior and the turn you need to make to make this angle. Put this in a funciton. 

Now you can write this sort of code:

```
sides = 5
for s in range(sides):
    turtle.forward(100)
    turtle.left(interior(60))
```

What shape does that draw? You'll find that the number of sides doesn't match the number of iterations (5). Fix this for 5 sides.

## Task 3

Figure out the relationship between the number of sides 


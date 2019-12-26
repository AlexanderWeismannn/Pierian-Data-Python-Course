import time
from turtle import *
from random import randint, choice


#Set up lines
penup()
goto(-140,140)

rtcounter = Turtle()
rtcounter.penup()
rtcounter.goto(320,120)
rnum = 0

btcounter = Turtle()
btcounter.penup()
btcounter.goto(320,80)
bnum = 0

gtcounter = Turtle()
gtcounter.penup()
gtcounter.goto(320,40)
gnum = 0

ytcounter = Turtle()
ytcounter.penup()
ytcounter.goto(320,0)
ynum = 0

for step in range(16):
    write(step)
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

while True:
    #Turtle #1
    red_turtle = Turtle()
    red_turtle.color("red")
    red_turtle.shape("turtle")
    red_turtle.penup()
    red_turtle.goto(-160,120)
    red_turtle.pendown()
    rtcounter.write(rnum)

    #Turtle #2
    blue_turtle = Turtle()
    blue_turtle.color("dark blue")
    blue_turtle.shape("turtle")
    blue_turtle.penup()
    blue_turtle.goto(-160,80)
    blue_turtle.pendown()
    btcounter.write(bnum)

    #Turtle #3
    green_turtle = Turtle()
    green_turtle.color("spring green")
    green_turtle.shape("turtle")
    green_turtle.penup()
    green_turtle.goto(-160,40)
    green_turtle.pendown()
    gtcounter.write(gnum)

    #Turtle #4
    yellow_turtle = Turtle()
    yellow_turtle.color("orange")
    yellow_turtle.shape("turtle")
    yellow_turtle.penup()
    yellow_turtle.goto(-160,0)
    yellow_turtle.pendown()
    ytcounter.write(gnum)

    #Turtle flourish
    for turn in range(4):
        red_turtle.left(90)
        blue_turtle.left(90)
        green_turtle.left(90)
        yellow_turtle.left(90)

    #Race begins
    #checks for the first to cross the finish line
    while True:
        turtle = choice([red_turtle, blue_turtle, green_turtle, yellow_turtle])
        turtle.forward(randint(1,5))
        if turtle.xcor() > 145:
            break

    turtle.color("gold")

    #declares the winner
    speed(1)
    if turtle == red_turtle:
        turtle.color("red")
        turtle.forward(150)
        turtle.write("Red WINS", align = "right", font = "Arial")
        rnum += 1


    elif turtle == blue_turtle:
        turtle.color("blue")
        turtle.forward(150)
        turtle.write("Blue WINS", align = "right", font = "Arial")
        bnum += 1


    elif turtle == green_turtle:
        turtle.color("green")
        turtle.forward(150)
        turtle.write("Green WINS", align = "right", font = "Arial")
        gnum += 1


    else:
        turtle.color("orange")
        turtle.forward(150)
        turtle.write("Orange WINS", align = "right", font = "Arial")
        ynum += 1


    #Resets the turtles and romoves the lines
    time.sleep(1.5)
    red_turtle.clear()
    red_turtle.hideturtle()
    rtcounter.clear()

    blue_turtle.clear()
    blue_turtle.hideturtle()
    btcounter.clear()

    green_turtle.clear()
    green_turtle.hideturtle()
    gtcounter.clear()

    yellow_turtle.clear()
    yellow_turtle.hideturtle()
    ytcounter.clear()

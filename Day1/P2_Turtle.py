import turtle

turtle.setup(1000,1000)

#part1
goat = turtle.Turtle()
goat.penup()
goat.goto(-300,200)
goat.pendown()
goat.goto(-300,100)
goat.goto(-100,100)
goat.goto(-100,200)
goat.penup()
goat.goto(-200,400)
goat.pendown()
goat.goto(-200,100)
goat.penup()

#part2
goat.goto(100,450)
goat.pendown()
goat.goto(200,350)
goat.goto(300,450)
goat.penup()
goat.goto(100,350)
goat.pendown()
goat.goto(300,350)
goat.penup()
goat.goto(100,350)
goat.pendown()
goat.goto(300,350)
goat.goto(200,350)
goat.goto(200,100)
goat.penup()
goat.goto(150,300)
goat.pendown()
goat.goto(250,300)
goat.penup()
goat.goto(50,250)
goat.pendown()
goat.goto(350,250)



turtle.done()

import turtle
# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Flower Animation")
# Create a turtle
flower = turtle.Turtle()
flower.shape("turtle")
flower.color("white")
# Set the turtle speed
flower.speed(10)
# Draw the flower
for _ in range(36):
    flower.forward(100)
    flower.left(45)
    flower.forward(100)
    flower.left(135)
    flower.forward(100)
    flower.left(45)
    flower.forward(100)
    flower.left(100)
# Hide the turtle
flower.hideturtle()
# Exit the turtle program
turtle.done()
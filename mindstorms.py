import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("blue")
    for i in range(0,24):
        for i in range(0,4):
            brad.forward(100)
            brad.right(90)
        brad.right(15)

    window.exitonclick()

draw_square()

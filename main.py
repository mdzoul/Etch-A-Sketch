from turtle import Turtle, Screen

bob = Turtle()
screen = Screen()


def forward():
	bob.fd(10)
	

def backward():
	bob.back(10)


def right():
	bob.right(10)


def left():
	bob.left(10)
	
	
def reset():
	bob.reset()


screen.listen()

screen.onkeypress(fun=forward, key="w")
screen.onkeypress(fun=backward, key="s")
screen.onkeypress(fun=right, key="d")
screen.onkeypress(fun=left, key="a")

screen.onkey(fun=reset, key="c")

screen.exitonclick()

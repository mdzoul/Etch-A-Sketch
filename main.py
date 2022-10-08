from turtle import Turtle, Screen


def draw():
	"""Allows user to choose a colour and then draw"""
	colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "black"]
	user_color = screen.textinput(title="Color", prompt="""Choose a color:
(red, orange, yellow, green, blue, purple, pink, black)""")
	if user_color in colors:
		bob.color(user_color)
	keystrokes()


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


def keystrokes():
	"""Keystrokes available, including reset"""
	screen.listen()
	
	screen.onkey(fun=draw, key="c")

	screen.onkeypress(fun=forward, key="w")
	screen.onkeypress(fun=backward, key="s")
	screen.onkeypress(fun=right, key="d")
	screen.onkeypress(fun=left, key="a")
	
	screen.onkey(fun=reset, key="r")


bob = Turtle()
screen = Screen()
screen.setup(width=700, height=500)

draw()

screen.exitonclick()

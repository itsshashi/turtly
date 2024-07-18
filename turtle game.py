import turtle
from turtle import Turtle, Screen
is_race=False
screen = Screen()
position=[-80,-40,0,40,80,120]
user=screen.textinput(title='make your bet',prompt='which turtle will win the race? enter color :')
screen.setup(width=500, height=400)
all_turtles=[]
colors=['violet','indigo','blue','green','yellow','orange','red']
for i in range(0,6):

    tim=Turtle(shape='turtle')
    tim.penup()
    tim.goto(x=-230,y=position[i])
    tim.color(colors[i])
    all_turtles.append(tim)
if user:
    is_race=True
import random
turtle.bgpic("road.gif")
while is_race:
    for j in all_turtles:
        if j.xcor()> 230:
            is_race=False
            winner=j.pencolor()
            if winner==user:
                print("you win your bet")
            else:
                print(f'you loose ! the winner is {winner}')

        step=random.randint(0,15)
        j.forward(step)







screen.exitonclick()

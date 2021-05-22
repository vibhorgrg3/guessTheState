import turtle
import pandas as pd

screen = turtle.Screen()
img = 'blank_states_img.gif'
screen.addshape(img)

t = turtle.Turtle()
t.shape(img)
t.penup()
# turtle.write("Home = ", True, align="center")
data = pd.read_csv('50_states.csv')
# print(data.head())
turtle.hideturtle()
turtle.penup()
d = data.to_dict()

dKeys = list(d.keys())
# print(type(dKeys))
# A list with state names
stateNames = list(d[dKeys[0]].values())
stateX = list(d[dKeys[1]].values())
stateY = list(d[dKeys[2]].values())
print(stateY)
print(stateX)
# print(dKeys)
# print(stateY, stateX)
score = 0
ch = 'Texas'
print(stateNames)
while score < 50 or ch != 'exit':
    ch = screen.textinput(f"enter state  {score}/50", 'Enter name')
    if ch.lower() == 'exit':
        break
    if ch.title() in stateNames:
        score += 1

        x_co = stateX[stateNames.index(ch.title())]
        y_co = stateY[stateNames.index(ch.title())]
        turtle.goto(x_co,y_co)
        turtle.write(ch.title(), True, align="center")
        stateNames.remove(ch.title())
s=stateNames.index('Texas')
print(s)
# x_co = stateX[stateNames.index(ch.title())]
# y_co = stateY[stateNames.index(ch.title())]
# turtle.goto(x_co,y_co)
# turtle.write(ch.title(), True, align="center")
x_co = stateX[stateNames.index(ch.title())]
print(x_co)
if score == 50:
    print("YOU WIN")
else:
    print(f"TIme Up you Lose, you guessed {score} states")

screen.exitonclick()

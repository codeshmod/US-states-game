import turtle
from pandas import *



def get_mouse_click_coor(x,y):
    print(x,y)

def loadcsv(path):
    data = pandas.read_csv(path)
    return data

def markstate(name,cor):
    state = turtle.Turtle()
    state.penup()
    state.goto(cor)
    state.hideturtle()
    state.write(name)

screen = turtle.Screen()
screen.title("U.S States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.onscreenclick(get_mouse_click_coor)
data = loadcsv("50_states.csv")
answered_state = []
while len(answered_state) < 50:
    ans = screen.textinput(title=f"{len(answered_state)}/50 guessed",prompt="Enter a state")

    if ans.title() in data.state.values and ans.title() not in answered_state:
        print("Correct")
        pos = data[data.state == ans.title()]
        cor =()
        cor = (pos.iloc[0]["x"],pos.iloc[0]["y"])
        markstate(ans.title(),cor)
        answered_state.append(ans.title())
    if ans.lower() == "exit":
        statestolearn = []
        for state in data.state:
            if state not in answered_state:
                statestolearn.append(state)
        df = DataFrame(statestolearn,columns=["MissingStates"])
        df.to_csv("statestolearn.csv")
        break

# turtle.mainloop()
from turtle import Turtle, Screen
import pandas

# Create a screen object
screen = Screen()
turtle = Turtle()
screen.title("Ghana Regions Game")


# Create a turtle object
image = "us_states_project/us_state.gif"
screen.addshape(image)
turtle.shape(image)
background_turtle = Turtle()
background_turtle.shape(image)

# Hide the turtle
text_turtle = Turtle()
text_turtle.penup()
text_turtle.hideturtle()

# Create the pandas dataset
state = pandas.read_csv("us_states_project/us_state.csv")
all_states = state.State.to_list()
guessed_state = []

# while loop to keep the game up and running until an exit is received
while len(guessed_state) < 50:
    user_answer = screen.textinput(title= f"{len(guessed_state)}/50 state correct", 
                                prompt="What is the state name?")
    if user_answer is None:
        confirm_exit = screen.textinput(title="Exit", prompt="Do you want to exit? Type yes to exit or no to continue.")
        if confirm_exit.lower() == "yes":
        #csv file for all the missing states
            missing_states = [state for state in all_states if state not in guessed_state]
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("us_states_project/missing_states.csv")
        
            break
        else:
            continue
    user_answer = user_answer.title()
    # to guess and append the state name for the user
    if user_answer in all_states:
        guessed_state.append(user_answer)
        t = turtle.hideturtle()
        turtle.penup()
        region_data = state[state.State == user_answer]
        turtle.goto(region_data.x.item(), region_data.y.item())
        turtle.write(user_answer)
    
    
screen.exitonclick()
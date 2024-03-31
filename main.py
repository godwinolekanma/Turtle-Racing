import turtle
from turtle import Turtle, Screen
import random

# Initialize variables
race_on = False

# Set up the screen
screen = Screen()
screen.setup(width=500, height=400)

# Get the number of players from user input
number_player = int(screen.textinput(title="Turtle racing game!", prompt="How many players are in"))
player_input = []
start_position = 70
y_position = []

# Get user input for each player's color and set starting positions
for number in range(0, number_player):
    user_input = screen.textinput(title="Make a bet", prompt=f"player{number + 1}? Enter a different color each: ")
    player_input.append(user_input)
    y_position.append(start_position)
    start_position += -30

all_turtle = []

# Create turtles for each player, set color and starting position
for n in range(0, number_player):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(player_input[n])
    new_turtle.penup()
    new_turtle.goto(-230, y_position[n])
    all_turtle.append(new_turtle)

# If player input exists, start the race
if player_input:
    race_on = True

# Main game loop
while race_on:
    for turtle in all_turtle:
        # Move each turtle forward by a random distance
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        # Check if any turtle has reached the finish line
        if turtle.xcor() > 230:  # get x coordinate of turtle
            race_on = False
            winning_color = turtle.pencolor()
            player_number = all_turtle.index(turtle) + 1
            print(f"The {winning_color} turtle is the winner! player{player_number} won")


# Close the window when clicked
screen.exitonclick()
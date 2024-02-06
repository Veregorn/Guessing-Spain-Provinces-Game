import turtle
import pandas
import tkinter as tk
from tkinter import messagebox

# This function shows a message to the user when the game is finished
def show_win_prompt():
    # Creates a root window and  hides it to only show the message
    root = tk.Tk()
    root.withdraw()  # So the root window doesn't appear

    # Shows the message
    messagebox.showinfo("Congratulations!", "Congratulations! You have guessed all the provinces of Spain")

    # Destroys the window after closing the message
    root.destroy()

# Create the screen
screen = turtle.Screen()
screen.title("Spain Provinces Game")

# Stablish our image as de background
image = "blank_spain_provinces.gif"
screen.addshape(image)
turtle.shape(image)

# Define a function in order to obtain the coordinates in the map for every province
# def get_mouse_click_coor(x, y):
#    print(x, y)

# We pass x-y coordinates to our function
#turtle.onscreenclick(get_mouse_click_coor)

# Keep our screen opened so we can keep clicking on every province
#turtle.mainloop()

# Create a DataFrame object from the CSV file
provinces_data = pandas.read_csv("provinces.csv")

# Let's create a turtle printer
printer = turtle.Turtle()
printer.hideturtle()
printer.color("Black")
printer.penup()

# We need a loop break condition
all_provinces_guessed = False

# Record the correct guesses in a list
correct_guesses = []

# Use a loop to allow the user to keep guessing
while not all_provinces_guessed:
    # Ask the user for the answer
    # Keep track of the score
    answer_province = screen.textinput(title=f"Guess the province: {len(correct_guesses)}/50",prompt="What's another province name?")

    # Convert the guess to Title case
    answer_province_titled = answer_province.title()

    # Check if the guess is among the 50 provinces
    row = provinces_data.loc[provinces_data['province'] == answer_province_titled]

    # Convert the row to a Series format (if not empty)
    if not row.empty:
        row_serie = row.iloc[0]

        # Check if the user have guessed this province before
        if not row_serie.province in correct_guesses:
            # Write correct guesses onto the map
            printer.goto(x=row_serie.x, y=row_serie.y)
            printer.write(row_serie.province, font=('Arial', 10, 'normal'))

            # Save the name in the list
            correct_guesses.append(row_serie.province)

            # Check if the game is over
            if len(correct_guesses) == 50:
                all_provinces_guessed = True

show_win_prompt()

screen.exitonclick()
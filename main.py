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
    
    # Ends the program
    exit()

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
printer.goto(-200, 400)
printer.write("Type 'Exit' to quit the game and save the provinces you left in a CSV file", font=('Arial', 14, 'bold'))

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

    # If the user have typed 'Exit' quit the game
    if answer_province_titled == 'Exit':
        break

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

# If the user has guessed all the provinces, show the winning prompt
if all_provinces_guessed:
    show_win_prompt()

# If not, the user have Exit the program manually, so we save missed provinces in a CSV file
# First we need to separate not guessed provinces
# Let's create a set from the column 'provinces' in the DataFrame
all_provinces = set(provinces_data["province"])

# Now let's create another set with the provinces guessed
provinces_guessed = set(correct_guesses)

# We use the operator ^ to have the diff of the 2 sets
provinces_not_guessed = all_provinces ^ provinces_guessed
print(provinces_not_guessed)

# In order to create a CSV file, we need first to create a DataFrame
my_df = pandas.DataFrame(list(provinces_not_guessed), columns=['Provinces not guessed'])

my_df.to_csv("not_guessed_provinces.csv")
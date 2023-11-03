import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

# Create a list to store game results
game_results = []

# Dictionary to map user choices to numbers
choices = {'rock': 0, 'paper': 1, 'scissors': 2}

# Dictionary to map numbers to choices
inv_choices = {0: 'rock', 1: 'paper', 2: 'scissors'}

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice - computer_choice) % 3 == 1:
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    # Add the game result to the list
    game_results.append(f"You chose: {inv_choices[user_choice]}, Computer chose: {inv_choices[computer_choice]} - {result}")

# Function to handle user's choice
def user_choice(choice):
    user_input = choices[choice]

    # Generate computer choice
    computer_choice = random.randint(0, 2)

    # Determine the winner
    determine_winner(user_input, computer_choice)

    # Update the UI
    update_ui(choice, computer_choice)

# Function to update the UI
def update_ui(user_choice, computer_choice):
    user_choice_label.config(text="You chose: " + user_choice)
    computer_choice_label.config(text="Computer chose: " + inv_choices[computer_choice])
    result_label.config(text=game_results[-1])
    score_label.config(text="Score: User {} - Computer {}".format(user_score, computer_score))

    # Update the Listbox with game results
    results_listbox.delete(0, tk.END)
    for game_result in game_results:
        results_listbox.insert(tk.END, game_result)

# Create a Tkinter window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")

# Create buttons for user's choices
rock_button = tk.Button(window, text="Rock", command=lambda: user_choice('rock'))
paper_button = tk.Button(window, text="Paper", command=lambda: user_choice('paper'))
scissors_button = tk.Button(window, text="Scissors", command=lambda: user_choice('scissors'))

rock_button.pack()
paper_button.pack()
scissors_button.pack()

# Labels to display user and computer choices and result
user_choice_label = tk.Label(window, text="")
computer_choice_label = tk.Label(window, text="")
result_label = tk.Label(window, text="")
score_label = tk.Label(window, text="Score: User 0 - Computer 0")

user_choice_label.pack()
computer_choice_label.pack()
result_label.pack()
score_label.pack()

# Create a Listbox to display game results
results_listbox = tk.Listbox(window, height=10, width=50)
results_listbox.pack()

window.mainloop()

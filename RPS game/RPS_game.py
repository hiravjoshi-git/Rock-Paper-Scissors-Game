import random
import tkinter as tk


# Function to determine the winner
def determine_winner(player_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    # Update images for player's and computer's choices
    player_image_label.config(image=images[player_choice])
    computer_image_label.config(image=images[computer_choice])

    # Determine the result
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
    else:
        result = "You lose!"

    # After a short delay, show the result and then reset
    root.after(1000, lambda: show_result(result))

# Function to display the result
def show_result(result):
    hide_buttons()
    result_label.config(text=result)
    result_label.pack(expand=True)

    # Show result for a moment and then reset
    root.after(2000, reset_game)

# Function to hide buttons and images
def hide_buttons():
    player_image_label.pack_forget()
    computer_image_label.pack_forget()
    button_frame.pack_forget()

# Function to reset the game
def reset_game():
    result_label.pack_forget()
    show_buttons()

# Function to show buttons and images
def show_buttons():
    player_image_label.pack(side="left", padx=10)
    computer_image_label.pack(side="right", padx=10)
    button_frame.pack(expand=True)

# Setup GUI
root = tk.Tk()
root.title("Rock Paper Scissors")
root.configure(bg='black')  # Dark background

# Load images for rock, paper, scissors
rock_img = tk.PhotoImage(file="rock.png")
paper_img = tk.PhotoImage(file="paper.png")
scissors_img = tk.PhotoImage(file="scissor.png")

images = {'Rock': rock_img, 'Paper': paper_img, 'Scissors': scissors_img}

# Frame to hold the buttons
button_frame = tk.Frame(root, bg='black')

# Create stylish buttons for Rock, Paper, Scissors
button_style = {
    'bg': 'gray20', 'fg': 'white', 'activebackground': 'gray40', 'activeforeground': 'white',
    'font': ('Arial', 14, 'bold'), 'relief': 'raised', 'bd': 5, 'padx': 10, 'pady': 5
}

rock_button = tk.Button(button_frame, text="Rock", command=lambda: determine_winner('Rock'), **button_style)
paper_button = tk.Button(button_frame, text="Paper", command=lambda: determine_winner('Paper'), **button_style)
scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: determine_winner('Scissors'), **button_style)

rock_button.pack(side="left", padx=5, pady=5)
paper_button.pack(side="left", padx=5, pady=5)
scissors_button.pack(side="left", padx=5, pady=5)

# Labels to show the images of choices
player_image_label = tk.Label(root, bg='black')
computer_image_label = tk.Label(root, bg='black')

# Label to show the result
result_label = tk.Label(root, text="", font=('Arial', 24, 'bold'), bg='black', fg='white')

# Pack the initial layout
show_buttons()

# Run the GUI event loop
root.mainloop()

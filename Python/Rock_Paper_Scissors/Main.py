import random

def display_instructions():
    print("Welcome to Rock, Paper, Scissors!")
    print("Rock beats Scissors, Scissors beats Paper, Paper beats Rock")

def get_choice(prompt):
    choices = ["rock", "paper", "scissors"]
    while True:
        choice = input(prompt).lower()
        if choice in choices:
            return choice
        print("Invalid choice. Please enter rock, paper, or scissors.")

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    if (user == "rock" and computer == "scissors") or \
       (user == "scissors" and computer == "paper") or \
       (user == "paper" and computer == "rock"):
        return "You win!"
    return "Computer wins!"

def play_game():
    display_instructions()
    while True:
        user_choice = get_choice("Enter your choice (rock, paper, or scissors): ")
        computer_choice = random.choice(["rock", "paper", "scissors"])
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        print(determine_winner(user_choice, computer_choice))
        
        if input("Do you want to play again? (yes/no): ").lower() != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()

import random

#Defining options
options = ['rock', 'paper', 'scissors']

#Function to get the player's choice
def get_player_input():
    while True:
        player_option = input("Enter rock, paper, or scissors: ").lower()
        if player_option in options:
            return player_option
        else:
            print("Invalid input. Please choose rock, paper, or scissors.")

#Function to get the computer's choice
def get_computer_input():
    return random.choice(options)

#Function to determine the winner
def calculate_winner(player_option, computer_option):
    if player_option == computer_option:
        return "It's a tie!"
    elif (player_option == 'rock' and computer_option == 'scissors') or \
         (player_option == 'scissors' and computer_option == 'paper') or \
         (player_option == 'paper' and computer_option == 'rock'):
        return "You win!"
    else:
        return "You lose!"

#game loop
def game_loop():
    print("Welcome to Rock, Paper, Scissors! Your opponent is Diddy")
    
    # Get player's choice
    player_option = get_player_input()
    
    # Get computer's (Diddy's) choice
    computer_option = get_computer_input()
    
    # Print the choices
    print("You chose: ",{player_option})
    print("Diddy chose: ",{computer_option})
    
    # Determine the winner and print the result
    outcome = calculate_winner(player_option, computer_option)
    print(outcome)

#Allow for multiple rounds
def main():
    while True:
        game_loop()
        
        # Ask if the player wants to play again
        play_again = input("Do you want to play Diddy again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
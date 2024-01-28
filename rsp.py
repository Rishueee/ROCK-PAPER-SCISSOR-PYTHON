import random

def user_input():
    player_choosed = input("Enter your choice :- Rock, Paper, or Scissors): ")
    while player_choosed not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter Rock, Paper, or Scissors.")
        player_choosed = input("Enter your choice: ")
    return player_choosed

def winner(player_choosed, computer_choosed):
    if player_choosed == computer_choosed:
        return "It's a Tie!"
    elif (player_choosed == "rock" and computer_choosed == "scissors") or \
         (player_choosed == "scissors" and computer_choosed == "paper") or \
         (player_choosed == "paper" and computer_choosed == "rock"):
        return "You Win!"
    else:
        return "You Lose!"

def start():
    print("Welcome to Rock, Paper, Scissors Game!")
    while True:
        player_choosed = user_input()
        computer_choosed = random.choice(["rock", "paper", "scissors"])
        print(f"You chose: {player_choosed}")
        print(f"Computer chose: {computer_choosed}")
        result = winner(player_choosed, computer_choosed)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again != "yes":
            print("Thank you for playing. Goodbye!")
            break

start()

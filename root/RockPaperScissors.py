import random

def get_player_choice():
    while True:
        player_choice = input("Enter your choice (rock, paper, scissors): ")
        if player_choice in ["rock", "paper", "scissors"]:
            return player_choice
        else:
            print("Invalid choice. Please try again.")
def check_winner(cpu_choice, player_choice):
    if player_choice == cpu_choice:
        winner = "Tie"
    elif cpu_choice == "rock":
        if player_choice == "paper":
            winner = "PLAYER"
        else:
            winner = "CPU"
    elif cpu_choice == "scissors":
        if player_choice == "rock":
            winner = "PLAYER"
        else:
            winner = "CPU"
    elif cpu_choice == "paper":
            if player_choice == "scissors":
                winner = "PLAYER"
            else:
                winner = "CPU"
    return winner

def play_round():
    cpu_choice = get_cpu_choice()
    player_choice = get_player_choice()
    winner = check_winner(cpu_choice, player_choice)
    return winner


player_wins = 0
cpu_wins = 0
ties = 0

while player_wins < 3 and cpu_wins <3:
    winner = play_round()
    if winner == "Tie":
        player_wins += 0
        cpu_wins += 0
        ties += 1
    elif winner == "PLAYER":
        player_wins += 1
        cpu_wins += 0
        ties += 0
    elif winner == "CPU":
        player_wins += 0
        cpu_wins += 1
        ties += 0
    print(f"Score - Player: {player_wins}  CPU: {cpu_wins}  Ties: {ties}")


if player_wins == 3:
    print("Congratulations! You won the tournament!")
else:
    print("WOMP WOMP CPU won, better luck next time bucko!")

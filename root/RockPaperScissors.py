import random

def get_cpu_choice():
    cpu_choice = random.choice(["rock", "paper", "scissors"])
    return cpu_choice

def get_player_choice():
    while True:
        player_choice = input()
        if player_choice in ["rock", "paper", "scissors"]:
            return player_choice

def check_winner(cpu_choice, player_choice):
    if player_choice == cpu_choice:
        winner = "Tie"
    elif cpu_choice == "rock":
        if player_choice == "paper":
            winner = "PLAYER"
        else:
            winner = "CPU"
    elif cpu_choice == "paper":
        if player_choice == "scissors":
            winner = "PLAYER"
        else:
            winner = "CPU"
    elif player_choice == "paper":
        winner = "CPU"
    else:
        winner = "PLAYER"

    return winner

def play_round():
    cpu_choice = get_cpu_choice()
    player_choice = get_player_choice()
    winner = check_winner(cpu_choice, player_choice)
    return winner

player_win = 0
cpu_win = 0
tie = 0

while player_win < 3 and cpu_win < 3:
    winner = play_round()
    if winner == "PLAYER":
        player_win += 1
    elif winner == "CPU":
        cpu_win += 1
    else:
        tie += 1
    print("Player:", player_win, "CPU:", cpu_win, "Ties:", tie)

if player_win == 3:
    print("PLAYER wins tournament")
else:
    print("CPU wins tournament")
import random

def get_cpu_choice():
    cpu_choice = random.choice(["Rock", "Paper", "Scissors"])
    return cpu_choice

def get_player_choice():
    while True:
        player_choice = input()
        if player_choice in ["Rock", "Paper", "Scissors"]:
            return player_choice

def check_winner(cpu_choice, player_choice):
    if player_choice == cpu_choice:
        winner = "Tie"
    elif cpu_choice == "Rock":
        if player_choice == "Paper":
            winner = "Player"
        else:
            winner = "Cpu"
    elif cpu_choice == "Paper":
        if player_choice == "Scissors":
            winner = "Player"
        else:
            winner = "Cpu"
    elif player_choice == "Scissors":
        winner = "Cpu"
    else:
        winner = "Player"

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
    if winner == "Player":
        player_win += 1
    elif winner == "Cpu":
        cpu_win += 1
    else:
        tie += 1
    print("Player:", player_win, "CPU:", cpu_win, "Ties:", tie)

if player_win == 3:
    print("Player wins tournament")
else:
    print("Cpu wins tournament")
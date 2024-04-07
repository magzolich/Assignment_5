# Develop an interactive "Paper, Scissors, Rock" game for player vs computer gameplay (computer uses choices 😉).
# Count points for human and computer. Stop game after one of players has 3 rounds won.


import random
possible_actions = ["rock", "paper", "scissors"]


def get_user_action():
    user_action = input("Choose (rock, paper, scissors): ")
    # possible_actions = ["rock", "paper", "scissors"]
    return user_action


def get_computer_action():
    computer_action = random.choice(possible_actions)
    return computer_action

# user | computer | none


def get_winner(user_action, computer_action):
    if user_action == computer_action:
        return "None"
    elif user_action == "rock":
        if computer_action == "scissors":
            return "User"
        else:
            return "Computer"
    elif user_action == "paper":
        if computer_action == "rock":
            return "User"
        else:
            return "Computer"
    elif computer_action == "scissors":
        if computer_action == "paper":
            return "User"
        else:
            return "Computer"


def main():
    user_wins = 0
    computer_wins = 0
    while user_wins < 3 and computer_wins < 3:
        user_action = get_user_action()
        computer_action = get_computer_action()
        winner = get_winner(user_action, computer_action)
        print(winner)
        if winner == "Computer":
            computer_wins += 1
        elif winner == "User":
            user_wins += 1
    if user_wins > computer_wins:
        print("You won the game")
    else:
        print("You lost the game")


if __name__ == "__main__":
    main()

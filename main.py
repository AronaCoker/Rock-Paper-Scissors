import random

while True:
    def get_choices():
        player_choice = input("Enter a choice (rock, paper, scissors:)")
        option = ["rock", "paper", "scissors"]
        computer_choice = random.choice(option)
        choices = {"player": player_choice, "computer": computer_choice}
        return choices


    def check_win(player, computer):
        print(f"You chose {player}, Computer chose {computer}")
        if player == computer:
            return "It´s a tie!"
        elif player == "rock":
            if computer == "scissors":
                return "Rock smashes Scissors! You Win!"
            else:
                return "Rock got Wrapped by Paper, You Lose"

        elif player == "paper":
            if computer == "rock":
                return "paper wraps rock! You Win!"
            else:
                return "Rock got Wrapped by Paper, You Lose"

        elif player == "scissors":
            if computer == "paper":
                return "Scissors cut Paper, You Win!"
            else:
                return "Rock Smashes scissors, You Lose"


    choices = get_choices()
    result = check_win(choices["player"], choices["computer"])
    print(result)







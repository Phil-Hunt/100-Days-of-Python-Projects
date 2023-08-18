import random

choices = {
    0: "Rock",
    1: "Paper",
    2: "Scissors"
}

comp_choice = random.randint(0, 2)

player_choice = int(input(f"What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors\n"))
print("You Chose " + choices[player_choice])
print("")
print("Computer Chose " + choices[comp_choice])
print("")

if player_choice == comp_choice:
    print("Draw!")
elif (player_choice == 0 and comp_choice == 2) or \
     (player_choice == 1 and comp_choice == 0) or \
     (player_choice == 2 and comp_choice == 1):
    print("You Win!")
else:
    print("Computer Wins!")

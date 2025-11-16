p1_wins: int = 0
p2_wins: int = 0

while True:
    player1_name: str = input("Your name: ")
    if len(player1_name) < 3:
        print("PUT A NAME YOU IDIOT!")
    elif player1_name == "Hacker":
        print("You have been banned from Rock, Paper, and Scissors.")
        continue
    break

while True:
    player2_name: str = input("Your name: ")
    if len(player2_name) < 3:
        print("PUT A NAME YOU IDIOT!")
        continue
    break

while True:
    exit_play: str = input("Do you want to exit or play? ").strip().title()
    if exit_play == "Exit":
        print(f"{player1_name}: {p1_wins}")
        print(f"{player2_name}: {p2_wins}")
        break
    elif exit_play == "Play":
        while True:
            player1_choice: str = input(f"{player1_name}: Rock, Paper, or Scissors? ").strip().title()

            if not (player1_choice == "Rock" or player1_choice == "Paper" or player1_choice == "Scissors"):
                print("Wrong option.")
                continue
            break

        for _ in range(20):
            print()

        while True:
            player2_choice: str = input(f"{player2_name}: Rock, Paper, or Scissors? ").strip().title()

            if not (player2_choice == "Rock" or player2_choice == "Paper" or player2_choice == "Scissors"):
                print("Wrong option.")
                continue
            break

        if player1_choice == "Paper" and player2_choice == "Rock":
            print(f"{player1_name} Won!")
            p1_wins = p1_wins + 1
        elif player1_choice == "Paper" and player2_choice == "Scissors":
            print(f"{player2_name} Won!")
            p2_wins = p2_wins + 1
        elif player1_choice == "Rock" and player2_choice == "Scissors":
            print(f"{player1_name} Won!")
            p1_wins = p1_wins + 1
        elif player2_choice == "Paper" and player1_choice == "Rock":
            print(f"{player2_name} Won!")
            p2_wins = p2_wins + 1
        elif player2_choice == "Paper" and player1_choice == "Scissors":
            print(f"{player1_name} Won!")
            p1_wins = p1_wins + 1
        elif player2_choice == "Rock" and player1_choice == "Scissors":
            print(f"{player2_name} Won!")
            p2_wins = p2_wins + 1
        elif player1_choice == player2_choice:
            print("Tie")

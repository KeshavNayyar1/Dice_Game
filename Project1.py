import random

def roll_dice():
    return random.randint(1, 6)

def get_number_of_players():
    while True:
        players = input("Enter the number of players (2 - 6): ")
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 6:
                return players
            else:
                print("You can only have 2 - 6 players.")
        else:
            print("Not Valid")

def main():
    max_score = 50
    num_players = get_number_of_players()
    player_scores = [0] * num_players

    while max(player_scores) < max_score:
        for player_index in range(num_players):
            print(f"\nPlayer {player_index + 1}'s turn has just started!")
            print(f"Your total score is: {player_scores[player_index]}\n")
            current_score = 0

            while True:
                should_roll = input("Would you like to roll (y)? ")
                if should_roll.lower() != "y":
                    break

                value = roll_dice()
                if value == 1:
                    print("You lost all your points because you rolled a one")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print(f"You rolled a: {value}")

                print(f"Your score is: {current_score}")

            player_scores[player_index] += current_score
            print(f"Your total score is: {player_scores[player_index]}")

    max_score = max(player_scores)
    winning_players = [i + 1 for i, score in enumerate(player_scores) if score == max_score]
    if len(winning_players) == 1:
        print(f"Player {winning_players[0]} is the winner with a score of: {max_score}")
    else:
        print(f"Players {', '.join(map(str, winning_players))} are tied as winners with a score of: {max_score}")

if __name__ == "__main__":
    main()

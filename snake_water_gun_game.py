import random

# 2D list containing game results
# 0 = Snake
# 1 = Water
# 2 = Gun

choices = ["Snake", "Water", "Gun"]

rules = [
    ["Draw", "Computer Wins", "Player Wins"],   # Computer: Snake
    ["Player Wins", "Draw", "Computer Wins"],   # Computer: Water
    ["Computer Wins", "Player Wins", "Draw"]    # Computer: Gun
]


def play_game():
    player_score = 0
    computer_score = 0

    print("\n🐍 SNAKE - 💧 WATER - 🔫 GUN")
    print("-----------------------------")

    while True:

        print("\nChoose:")
        print("0. Snake 🐍")
        print("1. Water 💧")
        print("2. Gun 🔫")
        print("3. Quit")

        try:
            player = int(input("Enter your choice: "))

            if player == 3:
                break

            if player not in [0, 1, 2]:
                print("❌ Invalid choice!")
                continue

            computer = random.randint(0, 2)

            print(f"\nYou chose: {choices[player]}")
            print(f"Computer chose: {choices[computer]}")

            # Accessing result from 2D list
            result = rules[computer][player]

            if result == "Draw":
                print("🤝 It's a Draw!")

            elif result == "Player Wins":
                print("🎉 You Win!")
                player_score += 1

            else:
                print("💻 Computer Wins!")
                computer_score += 1

            print(f"Score → You: {player_score} | Computer: {computer_score}")

        except ValueError:
            print("❌ Please enter a number.")

    print("\n==========================")
    print("        GAME OVER")
    print("==========================")
    print(f"Your Score: {player_score}")
    print(f"Computer Score: {computer_score}")


if __name__ == "__main__":
    play_game()
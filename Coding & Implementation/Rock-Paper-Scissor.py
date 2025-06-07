import random

def get_user_choice():
    print("\nChoices: rock, paper, scissors")
    user = input("Enter your choice: ").lower()
    while user not in ['rock', 'paper', 'scissors']:
        user = input("Invalid input. Enter rock, paper or scissors: ").lower()
    return user

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("🎮 Welcome to Rock-Paper-Scissors!")
    user_score = 0
    computer_score = 0

    for round in range(1, 4):  # Play 3 rounds
        print(f"\n--- Round {round} ---")
        user = get_user_choice()
        computer = get_computer_choice()

        print(f"You chose: {user}")
        print(f"Computer chose: {computer}")

        result = determine_winner(user, computer)
        print(result)

        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1

    print("\n🏁 Final Scores:")
    print(f"You: {user_score} | Computer: {computer_score}")

    if user_score > computer_score:
        print("🎉 Congratulations! You are the overall winner.")
    elif user_score < computer_score:
        print("💻 The computer wins this time. Try again!")
    else:
        print("🤝 It's a draw overall!")

if __name__ == "__main__":
    play_game()

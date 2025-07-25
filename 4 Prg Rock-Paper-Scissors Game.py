import random

def play_rps():
    print("🎮 Rock-Paper-Scissors Game")
    choices = ['rock', 'paper', 'scissors']
    score = {'user': 0, 'computer': 0}

    while True:
        user = input("Choose rock/paper/scissors (or 'exit' to stop): ").lower()
        if user == 'exit':
            break
        if user not in choices:
            print("❗ Invalid choice.")
            continue

        comp = random.choice(choices)
        print(f"Computer chose: {comp}")

        if user == comp:
            print("It's a tie!")
        elif (user == 'rock' and comp == 'scissors') or \
             (user == 'paper' and comp == 'rock') or \
             (user == 'scissors' and comp == 'paper'):
            print("✅ You win!")
            score['user'] += 1
        else:
            print("❌ You lose!")
            score['computer'] += 1

        print(f"Score → You: {score['user']} | Computer: {score['computer']}\n")

play_rps()

import random

print("===== Number Guessing Game =====")
print("I have selected a number between 1 and 100.")
print("You have 7 attempts to guess it.")

secret_number = random.randint(1, 100)
max_attempts = 7

for attempt in range(1, max_attempts + 1):

    try:
        guess = int(input(f"\nAttempt {attempt}/{max_attempts} - Enter your guess: "))

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        if guess < secret_number:
            print("Too low!")

        elif guess > secret_number:
            print("Too high!")

        else:
            print(f"Congratulations! You guessed the number in {attempt} attempts.")
            break

    except ValueError:
        print("Invalid input. Please enter a number.")

else:
    print(f"\nGame Over! The correct number was {secret_number}.")
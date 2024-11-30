import random

def main():
    print("Welcome to the High-Low Game!")
    
    # Initialize the score
    score = 0
    rounds = 5

    # Play 5 rounds
    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}")
        
        # Generate random numbers for the player and the computer
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number is: {player_number}")

        # Get the player's guess
        guess = input("Do you think your number is higher or lower than the computer's? (Enter 'higher' or 'lower'): ").strip().lower()

        # Check the truth
        if (guess == "higher" and player_number > computer_number) or \
           (guess == "lower" and player_number < computer_number):
            print("You guessed correctly!")
            score += 1
        else:
            print("Sorry, you guessed wrong.")
        
        # Reveal the computer's number
        print(f"The computer's number was: {computer_number}")
    
    # End of game
    print(f"\nGame over! Your final score is: {score}/{rounds}")

# Call the main function
if __name__ == "__main__":
    main()
